-- SET 'auto.offset.reset' = 'latest';
CREATE TABLE last_readings AS
select site,
MAX(rowtime) as last_rowtime
from my_stream
group by site
emit changes;

select
site,
LATEST_BY_OFFSET(ts),
LATEST_BY_OFFSET(lat),
LATEST_BY_OFFSET(long),
LATEST_BY_OFFSET(species)
from my_stream
group by site
emit changes;

--docker-compose exec ksqldb-cli ksql http://ksqldb:8088

-- https://stackoverflow.com/questions/50102662/confluent-4-1-0-ksql-stream-table-join-table-data-null/50103660#50103660