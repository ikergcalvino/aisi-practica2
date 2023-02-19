FROM python:3.11.1-alpine3.17
ENV FLASK_APP counter.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_DEBUG True
RUN pip install flask && pip install redis
RUN apk --no-cache add curl
WORKDIR /src
COPY src /src
EXPOSE 5000/tcp
ENTRYPOINT ["flask", "run"]
