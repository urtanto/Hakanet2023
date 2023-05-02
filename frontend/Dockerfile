FROM node:19.9-alpine3.17
LABEL authors="urtanto"

RUN mkdir front
WORKDIR front

ADD package.json /front/

RUN npm install --global --force yarn
RUN yarn install
RUN export PATH="/front/node_modules/.bin"

ADD . /front/

ENTRYPOINT yarn run dev