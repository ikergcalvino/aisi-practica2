FROM debian:buster-slim

RUN apt-get update \
	&& apt-get install -y wget make gcc \
	&& wget -O redis.tar.gz https://download.redis.io/releases/redis-7.0.7.tar.gz \
	&& mkdir redis && tar -xzf redis.tar.gz -C redis --strip-components=1 \
	&& cd redis && make && make install && rm -r reids* \
	&& apt-get purge -y --autoremove wget gcc make && apt-get clean all \
	&& groupadd -r redis && useradd -r -g redis redis


ENV REDIS_DATA /data
RUN mkdir $REDIS_DATA && chown redis:redis $REDIS_DATA
WORKDIR	$REDIS_DATA
USER redis
EXPOSE 6379/tcp
ENTRYPOINT exec: redis-server --protected-mode no
