from python:3
MAINTAINER cb-developer-network@vmware.com

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install -r tests/requirements.txt
