CREATE table latest_results as
select 1 as placeholder, site, LATEST_BY_OFFSET(name),LATEST_BY_OFFSET(lat),LATEST_BY_OFFSET(long),LATEST_BY_OFFSET(species)
from my_stream
group by placeholder, site
emit changes;