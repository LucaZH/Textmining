from flask import Flask,request,render_template
from traitement import *
app= Flask(__name__)
@app.route('/' , methods=['GET','POST'])
def index():
    if request.method=="GET":
        content= "Inserer une phrase"
        countedspace = countspace(content)
        countedword= countword(content)
        keyword = findkeyword(clean(content),countedword)
        sentence = getsentence(content)
        
        data = {
            'space':countedspace,
            'content':content,
            'word': countedword,
            'keyword':keyword,
            'sentence': sentence

        }
        return render_template('index.html',content=data)
    if request.method == 'POST':
        file=request.files['file']
        content = file.read().decode('utf-8')
        countedspace = countspace(content)
        countedword= countword(content)
        keyword = findkeyword(clean(content),countedword)
        sentence = getsentence(content)
        
        data = {
            'space':countedspace,
            'content':content,
            'word': countedword,
            'keyword':keyword,
            'sentence': sentence

        }
        return render_template('index.html',content=data)
    return render_template('index.html',content=data)


if __name__ == '__main__':
    app.run()