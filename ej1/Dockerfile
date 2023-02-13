FROM XXX

RUN apt-get update \
	&& apt-get install -y wget make gcc \
	&& XXX


ENV REDIS_DATA /data
RUN mkdir $REDIS_DATA && chown redis:redis $REDIS_DATA
WORKDIR	$REDIS_DATA
USER XXX
EXPOSE XXX
ENTRYPOINT XXX
