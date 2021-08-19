-- ksql> SET 'auto.offset.reset' = 'earliest';
SET 'auto.offset.reset' = 'earliest';
CREATE STREAM my_stream (site   VARCHAR,
                                                  name VARCHAR,
                                                  lat        double,
                                                  long double,
                                                  species VARCHAR)
WITH (KAFKA_TOPIC='airquality',
   VALUE_FORMAT='JSON');
-- https://kafka-tutorials.confluent.io/working-with-json-different-structure/ksql.html