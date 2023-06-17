import re
import spacy

nlp = spacy.load("fr_core_news_md")

ponctuation = re.compile(r'[^\w\s]')

def readfile(filename):
    with open(filename,encoding="utf-8") as f:
        return f.read()

def count_space(content):
    espace=0
    for element in content:
        if element==" ":
            espace+=1
    return espace

def count_caractere(content):
    caractere=0
    for element in content:
        caractere+=1
    return caractere

def count_word(content):
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

def find_keyword(content,total):
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

def count_paragraphs(content):
    paragraphs = content.split("\n\n")
    return len(paragraphs)
def count_verbs(content):
    doc = nlp(content)
    verbs = [token for token in doc if token.pos_ == "VERB"]
    return len(verbs)
def ner(content):
    doc = nlp(content)
    entities = [(word, word.ent_iob_, word.ent_type_) for word in doc]
    return entities
def get_sentence(content):
    doc = nlp(content)
    sentences = list(doc.sents)
    return len(sentences)

