from flask import Flask,request,render_template
from traitement import *
app= Flask(__name__)
@app.route('/' , methods=['GET','POST'])
def index():
    if request.method=="GET":
        content= "Inserer une phrase"
        data = {
            'content':content,
            'space':count_space(content),
            'caractere':count_caractere(content),
            'word':count_word(content),
            'keyword':findkeyword(count_word()),
            'sentence':get_sentence(content),
            'paragraph':count_paragraphs(content),
            'ner':ner(content),
        }
        return render_template('index.html',content=data)
    if request.method == 'POST':
        file=request.files['file']
        content = file.read().decode('utf-8')
        data = {
            'content':content,
            'space':count_space(content),
            'caractere':count_caractere(content),
            'word':count_word(content),
            'keyword':find_keyword(content,count_word(content)),
            'sentence':get_sentence(content),
            'paragraph':count_paragraphs(content),
            'ner':ner(content),
        }
        return render_template('index.html',content=data)
    return render_template('index.html',content=data)


if __name__ == '__main__':
    app.run()