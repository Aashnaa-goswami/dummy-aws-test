FROM python:3.8-slim

WORKDIR /flask_app

COPY . /flask_app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","-m","flask","--app","app.py","run","--host=0.0.0.0"]
