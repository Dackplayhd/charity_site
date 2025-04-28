from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang=\"uk\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Добро Поруч 🐾</title>
    <style>
        body { font-family: 'Helvetica Neue', sans-serif; margin: 0; background-color: #fff8f0; color: #333; }
        header { background-color: #fff; border-bottom: 2px solid #f4a261; padding: 1.5em 0; text-align: center; }
        .logo { font-size: 2.5em; font-weight: bold; color: #e76f51; letter-spacing: 2px; }
        .logo span { font-size: 0.7em; display: block; color: #2a9d8f; margin-top: 0.5em; }
        nav { margin-top: 1em; }
        nav a { color: #264653; margin: 0 1em; text-decoration: none; font-weight: 600; }
        nav a:hover { text-decoration: underline; }
        #hero { text-align: center; padding: 5em 1em; background: linear-gradient(#ffe8d6, #fff8f0); color: #264653; }
        .btn { display: inline-block; margin-top: 1em; padding: 1em 2em; background-color: #2a9d8f; color: #fff; text-decoration: none; font-weight: bold; border-radius: 50px; transition: all 0.3s ease; }
        .btn:hover { background-color: #21867a; transform: scale(1.05); }
        section { padding: 4em 1em; max-width: 800px; margin: auto; text-align: center; }
        section h2 { font-size: 2em; margin-bottom: 0.5em; color: #e76f51; position: relative; }
        section h2::after { content: '\ud83d\udc3e'; position: absolute; right: -1.5em; top: 0; font-size: 0.9em; }
        .actions { display: flex; flex-direction: column; gap: 1.5em; align-items: center; margin-top: 2em; }
        .action-btn { display: inline-block; padding: 1em 2em; background-color: #f4a261; color: #fff; text-decoration: none; font-weight: bold; border-radius: 50px; transition: all 0.3s ease; width: 280px; text-align: center; }
        .action-btn:hover { background-color: #e76f51; transform: scale(1.05); }
        .highlight { background-color: #fef6e4; padding: 1em; border-left: 4px solid #f4a261; margin: 2em 0; border-radius: 8px; }
        footer { text-align: center; padding: 2em; background-color: #fff; border-top: 2px solid #f4a261; color: #777; font-size: 0.9em; }
    </style>
</head>
<body>
    <header>
        <div class=\"logo\">🐾 Добро Поруч
            <span>Благодійна допомога тваринам</span>
        </div>
        <nav>
            <a href=\"#about\">Про нас</a>
            <a href=\"#help\">Як допомогти</a>
            <a href=\"#contact\">Контакти</a>
        </nav>
    </header>

    <section id=\"hero\">
        <h2>Подаруй тепло та надію тваринам 🐾</h2>
        <p>Разом ми можемо змінити життя на краще!</p>
        <a href=\"#help\" class=\"btn\">Долучитися</a>
    </section>

    <section id=\"about\">
        <h2>Про нас</h2>
        <p>\"Добро Поруч\" — це благодійна організація, що з любов'ю рятує безпритульних тварин, забезпечує їх лікування, догляд та шукає для кожного люблячий дім. Ми прагнемо створити світ, де кожна тварина знайде турботливу родину.</p>
        <div class=\"highlight\">
            Ваша підтримка допомагає нам щодня рятувати життя тварин та дарувати їм нову надію!
        </div>
    </section>

    <section id=\"help\">
        <h2>Як допомогти</h2>
        <div class=\"actions\">
            <a href=\"https://send.monobank.ua/jar/88ABvbfGqS\" target=\"_blank\" class=\"action-btn\">Переказати донат</a>
            <a href=\"https://happypaw.ua/ua\" target=\"_blank\" class=\"action-btn\">Допомогти тваринам</a>
            <a href=\"https://dogcat.com.ua/\" target=\"_blank\" class=\"action-btn\">Прихистити тварину</a>
        </div>
        <div class=\"highlight\">
            Кожен внесок має значення! Разом ми творимо великі зміни. 🐾
        </div>
    </section>

    <section id=\"contact\">
        <h2>Контакти</h2>
        <p>Email: help@dobroporuch.org</p>
        <p>Instagram: @dobroporuch</p>
    </section>

    <footer>
        <p>&copy; 2025 \"Добро Поруч\". Всі права захищені. 🐾 Благодійна організація допомоги тваринам.</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
