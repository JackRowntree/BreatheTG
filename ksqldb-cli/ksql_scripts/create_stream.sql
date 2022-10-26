-- ksql> SET 'auto.offset.reset' = 'earliest';
SET 'auto.offset.reset' = 'earliest';
CREATE STREAM IF NOT EXISTS my_stream (site   VARCHAR,
                                                  name VARCHAR,
                                                  ts VARCHAR,
                                                  lat        double,
                                                  long double,
                                                  species VARCHAR)
WITH (KAFKA_TOPIC='airquality',
   VALUE_FORMAT='JSON',
   timestamp = 'ts',                        -- the column to use as a timestamp
    timestamp_format = 'yyyy-MM-dd HH:mm:ss' -- the format to parse the timestamp);
    )
;
-- https://kafka-tutorials.confluent.io/working-with-json-different-structure/ksql.html