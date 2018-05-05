import re
import pycrfsuite
from pyvi.pyvi import ViTokenizer, ViPosTagger

def no_accent_vietnamese(s):
    s = re.sub(u'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(u'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(u'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(u'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(u'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(u'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(u'[ìíịỉĩ]', 'i', s)
    s = re.sub(u'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(u'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(u'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(u'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(u'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(u'[Đ]', 'D', s)
    s = re.sub(u'[đ]', 'd', s)
    return s

def check_accent(s):
    s = s.lower()
    charater = []

    a = list('àáạảãâầấậẩẫăằắặẳẵ')
    e = list('èéẹẻẽêềếệểễ')
    o = list('òóọỏõôồốộổỗơờớợởỡ')
    i = list('ìíịỉĩ')
    u = list('ùúụủũưừứựửữ')
    y = list('ỳýỵỷỹ')
    d = list('đ')
    charater.append(a)
    charater.append(e)
    charater.append(o)
    charater.append(i)
    charater.append(u)
    charater.append(y)
    charater.append(d)
    for i in range(len(charater)):
        for j in range(len(charater[i])):
            if charater[i][j] in s:
                return True
    return False

def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],
    }
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],
        })
    else:
        features['BOS'] = True

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],
        })
    else:
        features['EOS'] = True

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for token, postag, label in sent]

def sent2tokens(sent):
    return [token for token, postag, label in sent]

def ner_crf(question):
    text = ViPosTagger.postagging(question)
    detect = []
    ar = []
    for i in range(len(text[0])):
        l = []
        l.append(text[0][i])
        l.append(text[1][i])
        ar.append(tuple(l))
    detect.append(ar)
    X_detect = [sent2features(s) for s in detect]
    tagger = pycrfsuite.Tagger()
    tagger.open('./adapter/crf_ner_no_accent/crf.model')
    y_detect = [tagger.tag(xseq) for xseq in X_detect]
    pred = []
    for i in range(len(detect[0])):
        k = detect[0][i][0]
        v = y_detect[0][i]
        kv = []
        kv.append(k)
        kv.append(v)
        pred.append(tuple(kv))
    return pred
