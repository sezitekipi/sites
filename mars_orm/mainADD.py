from flask import Flask
from data import db_session
from data.users import User

db_session.global_init("db/blogs.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_sess = db_session.create_session()

    user = User()
    user.name = "Scott"
    user.surname = "Ridley"
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Бабахван"
    user.surname = "Максон"
    user.age = 145
    user.position = 'диктатор экваториальной гвинеи'
    user.speciality = 'sockLord'
    user.address = 'module_88'
    user.email = 'тфеуршппукы@mars.org'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Егор"
    user.surname = "Богданов"
    user.age = 133
    user.position = 'ыыы'
    user.speciality = 'быолог'
    user.address = 'module_14'
    user.email = 'ыыы@mars.org'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Степа"
    user.surname = "Заполем"
    user.age = 119
    user.position = 'лентяй'
    user.speciality = 'металлист'
    user.address = 'module_2009'
    user.email = 'mashinehead@mars.org'

    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()
