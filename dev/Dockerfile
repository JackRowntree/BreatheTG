FROM edenhill/kafkacat:1.6.0
COPY *.sh /kafka/
WORKDIR kafka
RUN chmod +x /kafka/
RUN apk add --no-cache bash
