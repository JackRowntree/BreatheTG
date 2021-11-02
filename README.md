# BreatheTG

## Dev Setup
* Spin up the kafka ecosystem with `docker-compose up`
* This starts data ingestion /stream creation, and runs telegram bot 
* `docker attach tgbot` to see telegram bot output
* `docker exec -it <container> bash` to open a shell in a given container and debug
