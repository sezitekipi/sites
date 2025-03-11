from flask import Flask
from flask import url_for, render_template
from random import randint as rd
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=rd(1, 100))


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)


@app.route('/que')
def queue():
    return render_template('queue.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
