FROM python:3.9-alpine

RUN apk add --no-cache gcc musl-dev build-base linux-headers

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY src /

ENV TITLE=FlaskFileHosting

EXPOSE 5000

CMD python /main.py "${TITLE}"
