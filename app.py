from flask import Flask, request, render_template
from traitement import *

app = Flask(__name__)

def highlight_entities(content, entities):
    highlighted_content = ""
    index = 0

    for word, iob, ent_type in entities:
        if iob == "B":
            highlighted_content += content[index:word.idx] + f'<mark class="{ent_type}">{word.text}</mark>'
            index = word.idx + len(word.text)
        else:
            continue

    highlighted_content += content[index:]
    return highlighted_content

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        content = "Voici un simple test de madagascar"
        data = {
            'content': content,
            'space': count_space(content),
            'caractere': count_caractere(content),
            'word': count_word(content),
            'keyword': find_keyword(content, count_word(content)),
            'sentence': get_sentence(content),
            'paragraph': count_paragraphs(content),
            'ner': ner(content),
            'nbverbs':len(verbs(content)),
            'verb_occurence': verb_occurence(content),
        }
        return render_template('index.html', content=data)

    if request.method == 'POST':
        file = request.files['file']
        content = file.read().decode('utf-8')
        data = {
            'content': content,
            'space': count_space(content),
            'caractere': count_caractere(content),
            'word': count_word(content),
            'keyword': find_keyword(content, count_word(content)),
            'sentence': get_sentence(content),
            'paragraph': count_paragraphs(content),
            'ner': ner(content),
            'nbverbs':len(verbs(content)),
            'verb_occurence': verb_occurence(content),
        }
        highlighted_content = highlight_entities(content, data['ner'])
        data['highlighted_content'] = highlighted_content
        return render_template('index.html', content=data)

    return render_template('index.html', content=data)


if __name__ == '__main__':
    app.run()
