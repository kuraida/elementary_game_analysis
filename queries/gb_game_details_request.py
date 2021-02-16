import requests
import json
import pandas as pd
import time


games_df = pd.read_csv('../data/games.csv').sort_values('guid', ascending=True)



#set headers & static params
headers = {

}

query_params = {

    'api_key':user_info['api_key'],
    'format':'json',
    'field_list':'',
    'filter': '',
    'limit':'100',
    'sort':'guid'
}

games_details_df = pd.DataFrame(columns=[])

query_idx = 0
while query_idx < games_df.shape[0]

    #fetch details for 100 games, iterate idx
    query_params['offset'] = str(query_idx)
    
    guid_filter = games_df[query_idx, query_idx+100]['guid'].to_string(index=False)
    guid_filter = 'guid:' + guid_filter.replace('\n', '|')
    query_params['filter'] = guid_filter

    games_request = requests.get('https://giantbomb.com/api/games/', headers=headers, params=games_params)
    

    time.sleep(18) #space out requests so as not to violate GiantBomb's rate limits
    query_idx += 100





