FROM mysql:5.7

COPY ./bd/ /docker-entrypoint-initdb.d/