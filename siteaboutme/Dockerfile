# инструкции для сборки Docker образа для приложения flask
FROM python:3.13.5-slim
RUN groupadd -r groupflask && useradd -r -g groupflask userflask

RUN pip install --upgrade pip
WORKDIR /app/www/easysite-docker
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 4000

COPY . .
USER userflask
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:4000", "main:app"]
#CMD ["python", "main.py"]