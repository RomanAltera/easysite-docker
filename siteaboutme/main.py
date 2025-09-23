from flask import Flask, render_template
import psycopg2 # драйвер для подключения БД PostgreSQL из Python
import os # модуль для работы с ОС, в частности доступ к переменным окружения

app = Flask(__name__) # точка входа в проект

@app.route("/") # декоратор, для обработки корня сайта /
def index():
    conn = psycopg2.connect(
        dbname=os.environ['DATABASE_NAME'],
        user=os.environ['DATABASE_USERNAME'],
        password=os.environ['DATABASE_PASSWORD'],
        host=os.environ['DATABASE_HOST']
    )

    cursor = conn.cursor() # объект для взаимодействия с БД

    cursor.execute('SELECT * FROM table1 LIMIT 10')
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", records=records)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/articles")
def articles():
    return render_template("articles.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000) # включить собственный сервер flask
