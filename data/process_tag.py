def process():
    filePath = "tag.txt"
    des = "pro_tag"
    data = []
    with open(filePath,"r") as file :
        raw_data = file.readlines()
    print(raw_data)
    with open(des,"w") as file:
        for line in raw_data:
            line = line.strip()
            if line == "":
                file.write("\n")
                continue
            else:
                arr = line.split(" ")
                if arr[2] == "WET":
                    arr[2] = "O"
                if("_" in arr[0]):
                    subarr = arr[0].split("_")
                    for word in subarr:
                        file.write("{} {}\n".format(word.lower(),arr[2]))
                else:
                    file.write("{} {}\n".format(arr[0].lower(), arr[2]))

def process_time():
    filePath = "tag.txt"
    des = "pro_tag"
    with open(filePath, "r") as file:
        raw_data = file.readlines()
    print(raw_data)
    with open(des, "w") as file:
        for line in raw_data:
            line = line.strip()
            if line == "":
                file.write("\n")
                continue
            else:
                arr = line.split(" ")
                if arr[2] == "WET" or arr[2] == "LOC":
                    arr[2] = "O"
                if ("_" in arr[0]):
                    subarr = arr[0].split("_")
                    for word in subarr:
                        file.write("{} {}\n".format(word.lower(), arr[2]))
                else:
                    file.write("{} {}\n".format(arr[0].lower(), arr[2]))

process()