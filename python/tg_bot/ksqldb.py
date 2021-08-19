from ksql import KSQLAPI
client = KSQLAPI('http://ksqldb:8088')

def get_latest_airquality_data_for_location(tg_lat,tg_long):
    query = f"""
    select
    site,
    geo_distance({tg_lat}, {tg_long}, LATEST_BY_OFFSET(lat), LATEST_BY_OFFSET(long), 'm'),
    LATEST_BY_OFFSET(species)
    from my_stream
    group by site
    emit changes;
    """
    query_output = client.query(query)
    return parse_kqsl_output(query_output)

def parse_kqsl_output(data):
    """
    Makes sense of ksql output
    :param data:  ksql data
    :return:
    """
    out = []
    for row in out:
        out.append(row)
        print(row)
    return out