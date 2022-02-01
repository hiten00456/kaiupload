FROM python:3.9.7-slim-buster

WORKDIR .
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "start.sh"]
