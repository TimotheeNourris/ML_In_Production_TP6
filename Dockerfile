FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .


CMD [ "python", "app.py"]
EXPOSE 5000
#docker image build -t pre-weather .