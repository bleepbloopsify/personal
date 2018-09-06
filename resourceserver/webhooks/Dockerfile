FROM python:3.6-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache git openssh

WORKDIR /opt/

COPY ./requirements.txt ./

RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt
RUN rm -rf /root/.cache

COPY ./ ./

RUN ln -s $(pwd)/ssh.config /root/.ssh/config
# to set perms for ssh config

CMD ["python", "app.py"]