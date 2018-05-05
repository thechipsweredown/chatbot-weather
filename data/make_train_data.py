import re
import random
import time


def read_file(filePath):
    with open(filePath,"r") as file :
        data = file.readlines()
    data2 = []
    for line in data:
        line = line.strip()
        if line != "":
            data2.append(line)
    return data2


def creat_raw_train_ner(filePath):
    raw_data = read_file(filePath)
    data = []
    with open(filePath,"a") as file:
        for line in raw_data :
            line = line.strip()
            dline = re.sub("phải không","như thế nào",line)
            dline = re.sub("có mưa","mưa",dline)
            file.write(dline + "\n")


def creat_train_ner(filePath,raw_filePath):
    raw_data = read_file(raw_filePath)
    with open(filePath,"w") as file:
        for line in raw_data:
            arr = line.strip().split(" ")
            for word in arr :
                file.write(word + "\n")
            file.write("\n")


def preprocess_train_ner(filePath):
    raw_data = read_file(filePath)
    with open(filePath,"w") as file :
        for line in raw_data:
            line = line.strip()
            arr = line.split(" ")
            if len(arr)==1:
                line = arr[0] + " O"
            file.write(line +"\n")


def make_raw_train_ner():
    data = read_file("raw_train_ner3")
    mua = read_file("mưa")
    tai = ["ở","xung quanh","xung quanh khu vực"]
    nhu_the_nao = ["ra sao","ra làm sao"]
    vao = ["vào tầm","khoảng","lúc","vào lúc","tại"]
    TIME = read_file("TIME")
    LOC = read_file("LOC")
    data = replace_word(data,"mưa",mua)
    data = replace_word(data,"tại",tai)
    data = replace_word(data,"như thế nào",nhu_the_nao)
    data = replace_word(data,"vào",vao)
    data = x3(data)
    with open("train_ner","w") as file:
        for line in data:
            arr = line.split(" ")
            for word in arr:
                if word=="TIME":
                    i = random.randint(0,len(TIME)-1)
                    tword = TIME[i]
                    tarr = tword.split(" ")
                    for i in tarr:
                        file.write(i + " TIME\n")
                elif word=="LOC":
                    i = random.randint(0, len(LOC)-1)
                    lword = LOC[i]
                    larr = lword.split(" ")
                    for i in larr:
                        if i=="," or i=="và" or i=="hoặc":
                            file.write(i + " O\n")
                        else:
                            file.write(i + " LOC\n")

                else :
                    file.write(word.lower() + " O\n")
            file.write("\n")


def replace_word(data,word,rwords):
    data2 = []
    for line in data:
        data2.append(line)
        if word in line:
            for rword in rwords:
                dline = re.sub(word, rword, line)
                data2.append(dline)
    return data2


def x3(data):
    data2 = []
    for i in data:
        data2.append(i)
        data2.append(i)
        data2.append(i)
    return data2


if __name__ == "__main__":
    make_raw_train_ner()
    # while True:
    #     i = random.randint(0,50)
    #     print(i)
    #     time.sleep(1)