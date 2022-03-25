FROM nginx:1.21.6-alpine

RUN rm /etc/nginx/conf.d/default.conf
RUN rm /usr/share/nginx/html/*.html

COPY plugins/nginx/default.conf /etc/nginx/conf.d/
COPY plugins/nginx/*.html /usr/share/nginx/html/