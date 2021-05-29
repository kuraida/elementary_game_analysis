import requests
import json 
import pandas as pd 


headers = user_info = json.loads(open('./auth.json').read())

headers = {'user-agent':user_info['user-agent']} #giant bomb api rejects requests without a unique user-agent

genres_query_params = {


    
    'api_key':user_info['api_key'],
    'format':'json'
    #'field_list':,
    #'filter':'company:995|62|90|340,release_date:1988-01-01 00:00:00|2014-01-01 00:00:00>'


}


genres_request = requests.get('https://www.giantbomb.com/api/genres/', headers=headers, params=genres_query_params)

genres_df = pd.DataFrame(json.loads(genres_request.text)['results'])
genres_df.to_csv('./data/genres.csv', index=False)
print(genres_df.sort_values('name', ascending=True)[['guid', 'name', 'description']])

