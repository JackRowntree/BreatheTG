# BreatheTG
## Requirements
* To get the containerised kafka ecosystem working, you will need access to the AWS assets for the project.
* Download AWS CLI, and add AWS config params to env vars
## Dev Setup
* Spin up the kafka ecosystem with `docker-compose up`
* This starts data ingestion /stream creation, and runs telegram bot 
* `docker attach tgbot` to see telegram bot output
* `docker exec -it <container> bash` to open a shell in a given container and debug
## Notes
* get aws creds as terraform at some point