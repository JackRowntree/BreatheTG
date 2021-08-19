# BreatheTG

##Dev Setup
* Spin up the kafka ecosystem with`docker-compose up --build`
* Begin data ingest with `docker exec kafkacat get_data.sh`
* Create ksqldb stream with `docker-compose exec ksqldb-cli ksql http://ksqldb:8088 && RUN SCRIPT blah.sql`
* Attach to tgbot container to check logging with
