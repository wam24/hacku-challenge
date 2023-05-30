FROM python:3.9-alpine3.17
RUN apk add --no-cache --virtual .build-deps \
                      curl
RUN curl https://bootstrap.pypa.io/get-pip.py -o /get-pip.py  \
    && python /get-pip.py \
    && pip3 install --upgrade pip
WORKDIR /www

COPY /www .

RUN  pip install -r requirements.txt

ENV VIRTUAL_ENV=/env \
    PATH=/env/bin:$PATH \
    NAME=app \
    DJANGODIR=/www \
    DJANGO_WSGI_MODULE=hacku.wsgi \
    NUM_WORKERS=2 \
    DJANGO_SETTINGS_MODULE=hacku.settings.local \
    DJANGO_SECRET_KEY=xnZADbBeju69lkaXfAP2m58Cui2Wvsc3Em4TQa56uSRCuZtqgVV079DVcrDFMARu \
    RUNDIR=/www


RUN ["chmod", "+x", "deployment.sh"]

RUN ["sh", "/www/deployment.sh"]


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]