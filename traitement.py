import re

ponctuation = re.compile(r'[^\w\s]')

def readfile(filename):
    with open(filename,encoding="utf-8") as f:
        return f.read()

def countspace(content):
    espace=0
    for element in content:
        if element==" ":
            espace+=1
    return espace

def countcaractere(content):
    caractere=0
    for element in content:
        caractere+=1
    return caractere

def countword(content):
    for ponct in ponctuation.findall(content):
        content = content.replace("'", "’")
        if ponct !="’":
            content= content.replace(ponct,"\spec+") 
        elif ponct =="’":
            pass
    content=content.replace("\n", "\spec+")
    content=content.replace("\spec+", " ")
    return len(content.split())

def clean(content):
    for ponct in ponctuation.findall(content):
        content= content.replace(ponct,"\spec+")
    content=content.replace("\n", "\spec+")
    content=content.replace("\spec+", " ")
    
    return content.lower()

def findkeyword(content,total):
    cleancontents=content.split()
    with open("stopwords.txt" , encoding="utf-8") as stopwords:
        g=stopwords.read()
        nb=0
        ocurence = []
        r=clean(g).split()
        for i in range(len(cleancontents)):
            if cleancontents[i] in r:
                    pass
            else:
                for j in range(len(cleancontents)):
                    if cleancontents[i]==cleancontents[j] :
                        nb+=1
                element={
                        "mot":cleancontents[i] ,
                        "occurence": nb,
                        "frequence": round((nb/total)*100,3)
                        }
                if element not in ocurence:
                    ocurence.append(element)
            nb=0
    return sorted(ocurence,key=lambda x:  x["occurence"],reverse=True)[:8]

def getsentence(content):
    # c = content.replace("\n"," ")
    # splited = c.split(". ")
    # print(splited)
    splited = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', content)

    return len(splited)
# def getparagraphe
# content = readfile("file.txt")
# print(f"Nombre de caractere : {countcaractere(content)}")
# print(f"Nombre d'espace : {countspace(content)}")
# print(f"Nombre de mots : {countword(content)}")
# print(f"Mot clés : {findkeyword(clean(content))}")
# print(getsentence(content))

