FROM node:10-alpine

RUN yarn global add knex

WORKDIR /opt/

RUN apk update && apk upgrade\
  && apk add --no-cache git \
  && apk --no-cache add --virtual builds-deps build-base python

COPY package.json yarn.lock ./

RUN yarn install

COPY ./ ./

CMD /bin/sh