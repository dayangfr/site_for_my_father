from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


@app.route('/')
def home():

    photos = [
        {"url": "/static/images/photo1.jpg", "caption": "Наши фотки с Турции, помнишь как там прикольно арбузы нарезали?"},
        {"url": "/static/images/photo2.jpg", "caption": "Было классно ходить там по игровым автоматам"},
        {"url": "/static/images/photo3.jpg", "caption": "Ты, кствти, самый сильный из всех этих богатырей"},
        {"url": "/static/images/photo4.jpg", "caption": "Надо как нибудь ещё так покататься"},
        {"url": "/static/images/photo5.jpg", "caption": "Любимая турбаза)"},
        {"url": "/static/images/photo6.jpg", "caption": "Просто забавная фотка"},
        {"url": "/static/images/photo7.jpg", "caption": "А это с аквапарка нашего"},
        {"url": "/static/images/photo8.jpg", "caption": "Ты главный пример в моей жизни"},
    ]


    congratulation_text = (
        "Дорогой папа! В этот особенный день я хочу сказать тебе спасибо за твою поддержку, "
        "мудрость и тепло, которое ты даришь нашей семье каждый день. Ты — моя главная опора и лучший пример того, "
        "каким должен быть настоящий мужчина. Желаю тебе крепкого здоровья, неиссякаемой энергии и чтобы каждый день приносил только радость. С днем рождения!"
    )

    return render_template('index.html', photos=photos, text=congratulation_text)


if __name__ == '__main__':
    app.run(debug=True)

