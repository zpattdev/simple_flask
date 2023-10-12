FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 3000

CMD [ "python", "app.py" ]