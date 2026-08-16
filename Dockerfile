FROM python:3.11-slim

RUN apt-get update -y && apt-get upgrade -y

COPY . /app/
WORKDIR /app/

RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD ["bash", "start"]

