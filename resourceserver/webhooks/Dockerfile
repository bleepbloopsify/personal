FROM python:3.6-alpine

RUN apk --update --no-cache add git openssh

WORKDIR /opt/

COPY ./requirements.txt ./

RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt

COPY ./ ./

CMD ["python", "app.py"]