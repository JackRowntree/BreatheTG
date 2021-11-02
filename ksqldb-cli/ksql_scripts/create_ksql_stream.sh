#!/bin/bash
echo -e "\n\n⏳ Waiting for KSQL to be available before launching CLI\n"
while [ $(curl -s -o /dev/null -w %{http_code} http://ksqldb:8088/) -eq 000 ]
do
  echo -e $(date) "KSQL Server HTTP state: " $(curl -s -o /dev/null -w %{http_code} http://ksqldb:8088/) " (waiting for 200)"
   sleep 5
done
echo -e "\n\n-> Running KSQL commands\n"
cat scripts/create_stream.sql | ksql http://ksqldb:8088
cat scripts/create_table.sql <(echo 'EXIT') | ksql http://ksqldb:8088
echo -e "\n\n-> sleeping…\n"
sleep infinity