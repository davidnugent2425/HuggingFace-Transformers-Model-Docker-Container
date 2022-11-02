# syntax=docker/dockerfile:1

FROM python:3.8

RUN python3 -m venv /opt/venv
COPY requirements.txt requirements.txt
RUN /opt/venv/bin/pip install -r requirements.txt

COPY app.py /app.py

EXPOSE 5000
ENTRYPOINT ["/opt/venv/bin/python", "/app.py"]
