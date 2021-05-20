FROM python:latest

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org flask redis

EXPOSE 80

ENV NAME test

CMD ["python3","/app/app.py"]