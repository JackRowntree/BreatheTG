#!/bin/bash
kafkacat -b broker:29092 \
         -t airquality \
         -C \
         -f 'Key: %k, payload: %s\n'
#consuming https://github.com/edenhill/kafkaca
# kafkacat -b broker:29092 -L