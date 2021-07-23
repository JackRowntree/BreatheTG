-- SET 'auto.offset.reset' = 'latest';

CREATE STREAM airquality_stream(
              site VARCHAR,
              name VARCHAR,
              lat VARCHAR,
              long  VARCHAR,
              species STRUCT )
WITH (KAFKA_TOPIC='airquality',
      VALUE_FORMAT='json');