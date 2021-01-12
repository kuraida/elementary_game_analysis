import requests
import json
import pandas as pd



user_info = json.loads(open('./auth.json').read())

headers = {'user-agent':user_info['user-agent']} #giant bomb api rejects requests without a unique user-agent


payload = {


    
    'api_key':user_info['api_key'],
    'format':'json',
    'field_list':'guid,id,name'

}

games_query = {

    'api_key':user_info['api_key'],
    'format':'json',
    'field_list':'guid,id,name,platforms,deck,original_release_date,original_game_rating',
    'limit':'10',
    'sort':'name',
    'filter':'platforms:19'

}







games_request = requests.get('https://www.giantbomb.com/api/games/', headers=headers, params=games_query)


#platform_request = requests.get('https://www.giantbomb.com/api/platforms/', headers=headers, params=payload)


results = pd.DataFrame(json.loads(games_request.text))
data_df = pd.DataFrame(json.loads(games_request.text)['results'])
data_df.to_csv('./data/games_sample.csv')

print(results)
print(data_df)
# with open('./data/gb_test.json', 'w') as out_file:
#     json.dump(json.loads(r.text), out_file)
#gb_df = pd.DataFrame(json.loads(r.text))


#gb_df.to_csv('./data/gb_test.csv')

