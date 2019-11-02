FROM python:3.7.3

ADD requirements.txt /setup/
WORKDIR /setup
RUN pip install -r requirements.txt
RUN rm -fr /setup

ADD app /app/
