#!/bin/bash
#upgrade- wait til topic existss
# sleep 60 
while [ 1 -eq 1 ];
do
    curl --show-error --silent http://api.erg.ic.ac.uk/AirQuality/Hourly/MonitoringIndex/GroupName=London/Json |
		jq --compact-output \
		  --raw-output\
		   --arg sep $'\x1c' \
         '.HourlyAirQualityIndex.LocalAuthority[]| select(.Site!= null) |.Site | if type == "array" then .[] else . end| {site: .["@SiteCode"], name: .["@SiteName"], lat:.["@Latitude"],long:.["@Longitude"], ts:.["@BulletinDate"], species:.Species} | [.site +$sep, tostring] | join("")' |
        kafkacat -b broker:29092 -t  airquality -K$'\x1c' -P -T
     sleep 3600
done

#read up on listeners etc -zookeper?
#kafkacat container -kafkacat command - broker container port 29092, airquality topic, -P receive data from STDIN (pipe), -T echo input to stdout
#https://stackoverflow.com/questions/32950503/can-i-have-100s-of-thousands-of-topics-in-a-kafka-cluster
#many partitions preferred over many topics
#running this in background and getting data as well
#
#key values. timestamp key? partitions too.https://rmoff.net/2020/09/30/setting-key-value-when-piping-from-jq-to-kafkacat/
#don't tihnk I actually need a key...

#https://www.markhneedham.com/blog/2019/05/23/deleting-kafka-topics-on-docker/ we got to delete the volume..
#docker exec broker kafka-topics --delete --zookeeper zookeeper:2181 --topic airquality