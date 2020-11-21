import json

def readPublicKey():
    with open("public_key.json", "r") as file:
        res = json.load(file)
        file.close()
        return res

def writePublicKey(data):
    with open('public_key.json', 'w') as file:
        json.dump(data, file, indent=4)
        file.close()

def readTxt(file):
    with open(file, 'r', encoding='utf-8') as doc:
        read = doc.readlines()
        doc.close()
        return read

def writeTxt(file, lines):
    with open(file, 'w', encoding='utf-8') as doc:
        doc.writelines(lines)
        doc.close()