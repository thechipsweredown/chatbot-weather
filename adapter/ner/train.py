import subprocess
import setting
import os
import re
from nltk.tag.stanford import StanfordNERTagger
from nltk import word_tokenize
from collections import defaultdict

def train():
    script_train = "java -cp stanford-ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop stanford-ner/config.prop"
    subprocess.call(script_train, shell=True)


def detector_ner(msg,st):
    sentence = word_tokenize(msg.lower())
    print(sentence)
    return st.tag(sentence)


def pass_entity(list_entity):
    result = {}
    result['LOC'] = []
    result['TIME'] = []
    for tup in list_entity :
        if tup[1] == "LOC" :
            result['LOC'].append(tup[0])
        if tup[1] == "TIME":
            result['TIME'].append(tup[0])
    return result


def main():
    classifier = 'model/chatbot-ner.ser.gz'
    jar = 'stanford-ner/stanford-ner.jar'
    st = StanfordNERTagger(classifier, jar)
    while True :
        msg = input("human : ")
        if msg == "":
            print("bot : bạn nhập tin nhắn đi !")
        else :
            result = detector_ner(msg,st)
            print(result)
            print(pass_entity(result))
            print("\n")


if __name__ == "__main__" :
    # creat_train_ner(setting.TRAIN_NER_FILE,setting.RAW_TRAIN_NER_FILE)
    # preprocess_train_ner(setting.TRAIN_NER_FILE)
    # train()
    # main()
    # creat_raw_train_ner(setting.RAW_TRAIN_NER_FILE)
    pass