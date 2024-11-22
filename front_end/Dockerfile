FROM node

EXPOSE 3000

WORKDIR /front-end

COPY ./package-lock.json ./package.json ./
RUN npm install

COPY . .

RUN npm run build

CMD [ "npm", "start" ]
