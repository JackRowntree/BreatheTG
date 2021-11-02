from ksql import KSQLAPI
import pandas as pd
import json
client = KSQLAPI('http://ksqldb:8088')

COLS = ['sitecode','sitename','species','distance']
def get_latest_airquality_data_for_location(tg_lat,tg_long):
    #TODO whats going on hre
    query = f"""
    select site,name,species,geo_distance({tg_lat},{tg_long},lat,long) from queryable_latest_results
    """
    query_output = client.query(query,stream_properties =  {'ksql.query.pull.table.scan.enabled':'true'})
    print(f'{query_output=}')
    return parse_kqsl_output(query_output)

def parse_kqsl_output(data):
    """
    Makes sense of ksql output
    :param data:  ksql data
    :return:
    """
    out = []
    try:
        next(data)
        for i in data:
            vals = (json.loads(i.strip(',\n'))['row']['columns'])
            row = dict(zip(COLS,vals))
            row['species'] = json.loads(row['species'])
            out.append(row)
    except RuntimeError:
        pass
    return pd.DataFrame(data)
    #
    # select
    # site,
    # name,
    # geo_distance(51.536455, -0.140526, LATEST_BY_OFFSET(lat), LATEST_BY_OFFSET(long), 'km'),
    # LATEST_BY_OFFSET(species)
    # from my_stream
    # group by site,name
    # emit changes;
    #
