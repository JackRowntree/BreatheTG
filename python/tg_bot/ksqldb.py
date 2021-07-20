from ksql import KSQLAPI
client = KSQLAPI('http://ksqldb:8088')

def get_latest_airquality_data_for_location(tg_lat,tg_long):
    query = f"""
    select *,  geo_distance({tg_lat}, {tg_long}, rct_lat, rct_long, 'm') AS dist_to_site 
    from airquality
    where dist_to_repairer_km() = min
    """
    query = client.query('select * from table1')
    data=next(query)
    return parse_kqsl_output(data)

def parse_kqsl_output(data):
    """
    Makes sense of ksql output
    :param data:  ksql data
    :return:
    """
    return data