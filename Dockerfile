
FROM python:3.8-slim-buster
# FROM tiangolo/uwsgi-nginx:python3.8

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y git
RUN pip install Cython
RUN pip install gevent
RUN pip install -r requirements.txt
EXPOSE 5001

# ENTRYPOINT [ "python" ]
# CMD [ "index.py" ]
ENTRYPOINT ["sh","gunicorn_starter.sh"]

USER root