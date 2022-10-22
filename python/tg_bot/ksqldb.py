from ksql import KSQLAPI
import pandas as pd
import json
client = KSQLAPI('http://ksqldb:8088')

COLS = ['sitecode','sitename','species','distance']
def get_latest_airquality_data_for_location(tg_lat,tg_long):
    #TODO whats going on hre
    query = f"""
    select site,name,species,geo_distance({tg_lat},{tg_long},lat,long) from latest_results
    """
    query_output = client.query(query,stream_properties =  {'ksql.query.pull.table.scan.enabled':'true'})
    return get_closest_site(query_output)

def get_closest_site(query_output):
    df_out = parse_kqsl_output(query_output)
    closest_site_dict = _get_closest_site(df_out)
    return closest_site_dict

def parse_kqsl_output(data):
    """
    Makes sense of ksql output
    :param data:  ksql data
    :return:
    """
    out = []
    out_str = ''
    try:
        next(data)
        for i in data:
            print(type(i))
            print(i)
            print((json.loads(i.strip(',\n').rstrip(']'))['row']['columns']))
            vals = (json.loads(i.strip(',\n').rstrip(']'))['row']['columns'])
            row = dict(zip(COLS,vals))
            row['species'] = json.loads(row['species'])
            out.append(row)
            print(out)
    except (RuntimeError, StopIteration) as e:
        pass
    # for i in data:
    #     out_str+= i.strip(',\n')
    # print(out_str)
    # vals = json.loads(out_str)
    # print(vals)
    # vals = [dic['row']['columns'] for dic in vals]
    # print(vals)
    # row = dict(zip(COLS,vals))
    # print(row)
    # row['species'] = json.loads(row['species'])
    # print(row)
    return pd.DataFrame(out)

def _get_closest_site(df_out):
    return df_out.sort_values('distance', ascending=True).head(1).to_dict('records')[0]

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
