# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
FROM tiangolo/node-frontend:10 as build-stage

#Если не получается - поменять на "frontend-desktop", наверное
WORKDIR /.

COPY package*.json /.

RUN npm install

COPY ./ /.

ARG FRONTEND_ENV=production

ENV REACT_APP_ENV=${FRONTEND_ENV}

# Comment out the next line to disable tests
# RUN npm run test:unit

RUN npm run build


# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.23

# COPY --from=build-stage /app/dist/ /usr/share/nginx/html
COPY --from=build-stage /dist/ /usr/share/nginx/html

COPY --from=build-stage /nginx.conf /etc/nginx/conf.d/default.conf
COPY ./nginx-backend-not-found.conf /etc/nginx/extra-conf.d/backend-not-found.conf
