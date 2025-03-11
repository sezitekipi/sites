from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Заготовка')


@app.route('/training/<prof>')
def training(prof):
    number = 0
    path = url_for('static', filename='img/sc.jpg')
    if 'инженер' in prof or 'строитель' in prof:
        number = 1
        path = url_for('static', filename='img/it.jpg')
    return render_template('training.html', number=number, url_img=path)


# @app.route('/promotion')
# def prom():
#     sp = ['Человечество вырастает из детства.',
#             'Человечеству мала одна планета.',
#             'Мы сделаем обитаемыми безжизненные пока планеты.',
#             'И начнем с Марса!',
#             'Присоединяйся!']
#     return '</br>'.join(sp)
#
#
# @app.route('/image_mars')
# def image_mars():
#     return f"""<!doctype html>
#                 <html lang="en">
#                   <head>
#                     <meta charset="utf-8">
#                     <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
#                     <title>Привет, Яндекс!</title>
#                   </head>
#                   <body>
#                     <h1>Жди нас, Марс!</h1>
#                     <img src="{url_for('static', filename='img/mars.jpg')}
#                     alt="здесь должна была быть картинка, но не нашлась">
#                     <p>Вот она какая, красная планета!<p/>
#                   </body>
#                 </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')