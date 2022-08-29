FROM python:3.8-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 1337

ENTRYPOINT [ "python" ]
CMD ["main.py" ]
