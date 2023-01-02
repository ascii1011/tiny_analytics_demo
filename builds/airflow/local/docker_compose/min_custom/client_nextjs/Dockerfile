FROM node:10.16.0-alpine

WORKDIR /usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY app/. /usr/src/app/.

RUN npm install

EXPOSE 3000
CMD ["npm", "run", "dev"]
