import requests
import json
import pandas as pd
import time



#read user info from auth.json (placed in project root)
user_info = json.loads(open('./auth.json').read())
headers = {'user-agent':user_info['user-agent']} #giant bomb api rejects requests without a unique user-agent

#load in platforms, create api filter based on platforms used
platforms = pd.read_csv('./data/platforms.csv')
platform_filter='platforms:'
for p in platforms.sort_values('id')['id']:
    platform_filter = platform_filter + str(p) + '|'

#determine the total number of games we will be querying

touch_params = {
    'api_key':user_info['api_key'],
    'format':'json',
    'filter':'platforms:19',
    'limit':1
}

touch_request = requests.get('https://giantbomb.com/api/games/', headers=headers, params=touch_params)
n = json.loads(touch_request.text)['number_of_total_results']




#set general parameters for games query, leaving offset to be iterated by loop
games_params = {
    'api_key':user_info['api_key'],
    'format':'json',
    'fields_list':'guid,id,name,platforms,description,number_of_user_reviews,original_game_rating,original_release_date',
    'filter':'platforms:19',
    'limit':'100'
}

idx = 0
games_df = pd.DataFrame(columns=games_params['fields_list'].split(','))
print(games_df.head())
while idx <= n:

    games_params['offset'] = str(idx)
    games_request = requests.get('https://giantbomb.com/api/games/', headers=headers, params=games_params)
    result_df = pd.DataFrame(json.loads(games_request.text)['results'])
    games_df = games_df.append(result_df)
    idx += 100
    print(idx)
    time.sleep(18)


print(games_df)
print(games_df.shape)

games_df.to_csv('./data/ps2.csv')
    




