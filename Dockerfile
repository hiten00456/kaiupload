FROM python:3.9.7-slim-buster

RUN apt update && apt upgrade -y \
  && apt -y install python3-pip \
  && pip3 install glob \
  && pip3 install zipfile \
  && pip3 install humanize 

WORKDIR .
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "start.sh"]
