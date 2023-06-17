import spacy

nlp = spacy.load("fr_core_news_md")
with open("file.txt", "r", encoding="utf-8") as file:
    text = file.read()
    doc = nlp(text)

    for ent in doc.ents:
        print(ent.text, ent.label_)
import re
import spacy

nlp = spacy.load("fr_core_news_md")
class TextAnalyzer:
    def __init__(self, content):
        self.content = content
        self.ponctuation = re.compile(r'[^\w\s]')
    def clean(self,content):
        for ponct in self.ponctuation.findall(content):
            content= content.replace(ponct,"\spec+")
        content=content.replace("\n", "\spec+")
        content=content.replace("\spec+", " ")
        return content.lower()
    def count_space(self):
        espace = 0
        for element in self.content:
            if element == " ":
                espace += 1
        return espace

    def count_caractere(self):
        caractere = 0
        for element in self.content:
            caractere += 1
        return caractere

    def count_word(self):
        content = self.content
        for ponct in self.ponctuation.findall(content):
            content = content.replace("'", "’")
            if ponct != "’":
                content = content.replace(ponct, "\spec+")
            elif ponct == "’":
                pass
        content = content.replace("\n", "\spec+")
        content = content.replace("\spec+", " ")
        return len(content.split())

    def get_sentence(self):
        doc = nlp(self.content)
        sentences = list(doc.sents)
        return len(sentences)

    def findkeyword(self,total):
        cleancontents=self.content.split()
        with open("stopwords.txt" , encoding="utf-8") as stopwords:
            g=stopwords.read()
            nb=0
            ocurence = []
            r=self.clean(g).split()
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
    def count_paragraphs(self):
        paragraphs = self.content.split("\n\n")
        return len(paragraphs)

    def count_verbs(self):
        doc = nlp(self.content)
        verbs = [token for token in doc if token.pos_ == "VERB"]
        return len(verbs)

    def ner(self):
        doc = nlp(self.content)
        entities = [(word, word.ent_iob_, word.ent_type_) for word in doc]
        return entities
# with open("file.txt", encoding="utf-8") as f:
#     content = f.read()

# analyzer = TextAnalyzer(content)

# print("Nombre d'espaces :", analyzer.count_space())
# print("Nombre de caractères :", analyzer.count_caractere())
# print("Nombre de mots :", analyzer.count_word())
# print("Nombre de phrases :", analyzer.getsentence())
# print("Nombre de paragraphes :", analyzer.count_paragraphs())
# print("Nombre de verbes :", analyzer.count_verbs())
# print("Entités nommées :", analyzer.ner())
# print("Mot clés:", analyzer.findkeyword(analyzer.count_word()))

# doc = nlp(content)
# for ent in doc.ents:
#     print(ent.text, spacy.explain(f"{ent.label_}")()