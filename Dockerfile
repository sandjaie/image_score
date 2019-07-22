FROM python:3.7

RUN mkdir /app
WORKDIR /app

COPY . .

RUN python setup.py install
ENTRYPOINT ["imagescore"]