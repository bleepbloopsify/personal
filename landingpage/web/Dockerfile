FROM python:3.6-alpine

WORKDIR /opt/

COPY ./requirements.txt ./

RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt

COPY ./ ./

CMD ["python", "app.py"]