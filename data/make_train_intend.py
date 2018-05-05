import re

def read_file(filePath):
    with open(filePath,"r") as file :
        data = file.readlines()
    data2 = []
    for line in data:
        line = re.sub("\?","",line)
        line = line.strip()
        if line != "":
            data2.append(line)
    return data2


def make_train_wh_weather():
    filePath = "wh_weather"
    raw_data = read_file(filePath)
    data = []
    data.extend(raw_data)
    print(len(data))
    for line in raw_data:
        if "như thế nào" in line:
            line1 = re.sub("như thế nào","ra sao",line)
            data.append(line1)
    print(len(data))
    raw_data = []
    raw_data.extend(data)
    for line in raw_data:
        line1 = "cho hỏi " + line
        line2 = "dự báo " + line
        line3 = "cho hỏi dự báo " + line
        line4 = "dự báo thời tiết " + line
        data.append(line1)
        data.append(line2)
        data.append(line3)
        data.append(line4)
    print(len(data))

    with open(filePath,"w") as file:
        for line in data:
            file.write(line + "\n")


def make_train_yesno_weather():
    filePath = "yesno_weather"
    raw_data = read_file(filePath)
    data = []
    data.extend(raw_data)

    print(len(data))
    for line in raw_data:
        line1 = "cho hỏi " + line
        line2 = "dự báo " + line
        line3 = "cho hỏi dự báo " + line
        line4 = "dự báo thời tiết " + line
        data.append(line1)
        data.append(line2)
        data.append(line3)
        data.append(line4)
    print(len(data))

    with open(filePath,"w") as file:
        for line in data:
            file.write(line + "\n")


if __name__ == "__main__" :
    # make_train_wh_weather()
    make_train_yesno_weather()



