FROM node:10-alpine

WORKDIR /app

COPY ./package.json ./
RUN yarn install

COPY ./ ./

CMD ["npm", "start"]
