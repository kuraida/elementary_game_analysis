import requests
import json 
import pandas as pd 


headers = user_info = json.loads(open('./auth.json').read())

headers = {'user-agent':user_info['user-agent']} #giant bomb api rejects requests without a unique user-agent

platforms_query_params = {


    
    'api_key':user_info['api_key'],
    'format':'json',
    'field_list':'id,guid,company,name,description,deck,release_date,original_price,install_base',
    'filter':'company:995|62|90|340,release_date:1988-01-01 00:00:00|2014-01-01 00:00:00>'


}


platform_request = requests.get('https://www.giantbomb.com/api/platforms/', headers=headers, params=platforms_query_params)

platform_df = pd.DataFrame(json.loads(platform_request.text)['results'])
platform_df.to_csv('./data/platforms.csv', index=False)
print(platform_df.sort_values('release_date', ascending=True)[['guid','name', 'release_date']])

