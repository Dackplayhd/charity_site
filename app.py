from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Добро поруч</title>
    <style>
        body { font-family: 'Helvetica Neue', sans-serif; margin: 0; background-color: #fff; color: #111; }
        header { background-color: #fff; border-bottom: 1px solid #ddd; padding: 1.5em 0; text-align: center; }
        .logo { font-size: 2em; font-weight: bold; color: #000; letter-spacing: 2px; }
        nav { margin-top: 0.5em; }
        nav a { color: #000; margin: 0 1em; text-decoration: none; font-weight: 500; }
        nav a:hover { text-decoration: underline; }
        #hero { text-align: center; padding: 4em 1em; background-color: #f9f9f9; color: #000; }
        .btn { display: inline-block; margin-top: 1em; padding: 0.75em 1.5em; background-color: #000; color: #fff; text-decoration: none; font-weight: bold; border-radius: 4px; transition: background 0.3s; }
        .btn:hover { background-color: #333; }
        section { padding: 3em 1em; max-width: 800px; margin: auto; text-align: center; }
        section h2 { font-size: 1.8em; margin-bottom: 0.5em; color: #000; }
        .actions { display: flex; flex-direction: column; gap: 1em; align-items: center; margin-top: 2em; }
        .action-btn { display: inline-block; padding: 0.75em 1.5em; background-color: #4CAF50; color: #fff; text-decoration: none; font-weight: bold; border-radius: 8px; transition: background 0.3s; width: 250px; text-align: center; }
        .action-btn:hover { background-color: #45a049; }
        footer { text-align: center; padding: 1.5em; background-color: #fff; border-top: 1px solid #ddd; color: #555; }
    </style>
</head>
<body>
    <header>
        <div class="logo">Добро Поруч</div>
        <nav>
            <a href="#about">Про нас</a>
            <a href="#help">Як допомогти</a>
            <a href="#contact">Контакти</a>
        </nav>
    </header>

    <section id="hero">
        <h2>Допоможи тваринам знайти дім</h2>
        <p>Разом ми творимо добро щодня.</p>
        <a href="#help" class="btn">Долучитися</a>
    </section>

    <section id="about">
        <h2>Про нас</h2>
        <p>Ми — благодійна організація, яка рятує безпритульних тварин і допомагає їм знайти нову родину.</p>
    </section>

    <section id="help">
        <h2>Як допомогти</h2>
        <div class="actions">
            <a href="https://www.uanimals.org/donate" target="_blank" class="action-btn">Переказати донат</a>
            <a href="https://happypaw.ua/ua/volunteer" target="_blank" class="action-btn">Стати волонтером</a>
            <a href="https://dogcat.com.ua/" target="_blank" class="action-btn">Прихистити тварину</a>
        </div>
    </section>

    <section id="contact">
        <h2>Контакти</h2>
        <p>Email: help@dobroporuch.org</p>
        <p>Instagram: @dobroporuch</p>
    </section>

    <footer>
        <p>&copy; 2025 Добро поруч</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)
