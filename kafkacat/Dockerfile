FROM edenhill/kafkacat:1.6.0
COPY *.sh scripts/
WORKDIR scripts
RUN chmod +x .
RUN apk add --no-cache bash
RUN apk add jq;
RUN apk add curl;	