SET 'ksql.query.pull.table.scan.enabled'='true';
CREATE table if not exists latest_results as
select site, LATEST_BY_OFFSET(name) as name,LATEST_BY_OFFSET(lat) as lat,LATEST_BY_OFFSET(long) as long,LATEST_BY_OFFSET(species) as species
from my_stream
group by site
emit changes;
