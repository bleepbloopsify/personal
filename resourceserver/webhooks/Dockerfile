FROM python:3.6-alpine

RUN apk --update add git openssh && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

WORKDIR /opt/

COPY ./requirements.txt ./

RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt

COPY ./ ./

CMD ["python", "app.py"]