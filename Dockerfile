FROM python:alpine3.7
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && apk del build-dependencies
RUN pip install -r requirements.txt
EXPOSE 80
CMD python ./index.py
