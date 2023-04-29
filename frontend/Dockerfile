FROM node:19.9
LABEL authors="vlada"

RUN mkdir front
WORKDIR front

ADD package.json /front/

RUN npm install --global --force yarn
RUN yarn install
RUN export PATH="/front/node_modules/.bin"

ADD . /front/

ENTRYPOINT yarn run dev