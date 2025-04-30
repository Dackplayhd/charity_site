from flask import Flask

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Захист тварин</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0; padding: 0;
        }
        header {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 1em;
        }
        nav a {
            margin: 0 15px;
            color: white;
            text-decoration: none;
        }
        #banner {
            background: #e67e22;
            color: white;
            text-align: center;
            padding: 3em 1em;
        }
        section {
            padding: 2em;
        }
        .btn {
            display: inline-block;
            padding: 0.5em 1em;
            background-color: #c0392b;
            color: white;
            border-radius: 5px;
            text-decoration: none;
        }
        footer {
            background-color: #ecf0f1;
            text-align: center;
            padding: 1em;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <header>
        <h1>Захист тварин</h1>
        <nav>
            <a href="#about">Про нас</a>
            <a href="#activities">Діяльність</a>
            <a href="#support">Підтримати</a>
        </nav>
    </header>
    <main>
        <section id="banner">
            <h2>Допоможіть тваринам просто зараз</h2>
            <p>Кожен внесок рятує життя</p>
            <a href="#support" class="btn">Підтримати</a>
        </section>
        <section id="about">
            <h2>Про нас</h2>
            <p>Ми — ініціатива, що рятує та захищає тварин по всій Україні. Працюємо з 2016 року.</p>
        </section>
        <section id="activities">
            <h2>Діяльність</h2>
            <ul>
                <li>Порятунок тварин із гарячих точок</li>
                <li>Лікування та реабілітація</li>
                <li>Пошук нових домівок</li>
                <li>Правовий захист прав тварин</li>
            </ul>
        </section>
        <section id="support">
            <h2>Підтримати нас</h2>
            <p>Ваша підтримка допомагає продовжувати нашу місію. Ви можете зробити разовий чи щомісячний внесок.</p>
            <a href="#" class="btn">Зробити внесок</a>
        </section>
    </main>
    <footer>
        <p>© 2025 Захист тварин. Усі права захищені.</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def index():
    return html_template

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def home():
    return render_template_string(html_template)
