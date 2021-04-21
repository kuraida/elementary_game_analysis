import requests
import json
import pandas as pd
import time


games_df = pd.read_csv('./data/games.csv').sort_values('guid', ascending=True)

#read user info from auth.json (placed in project root)
user_info = json.loads(open('./auth.json').read())
headers = {'user-agent':user_info['user-agent']} #giant bomb api rejects requests without a unique user-agent


query_params = {

    'api_key':user_info['api_key'],
    'format':'json',
    'field_list':'',
    'filter': '',
    'limit':'100',
    'sort':'guid'
}

#game_details_df to be used in final data structure, query_results_df for error checking
game_details_df = pd.DataFrame(columns=[])
query_results_df = pd.DataFrame(columns=[])

number_of_requests = games_df.shape[0]
idx = 0
failed_requests = []

for guid in games_df.loc[games_df['guid']>'']['guid']:

    print('Running request ' + str(idx) + ' of ' + str(number_of_requests) + ' [GUID ' + str(guid) + '].')

    game_details_request = requests.get('https://giantbomb.com/api/game/' + str(guid) + '/', headers=headers, params=query_params)

    #if no data returned, append guid to error list and continue
    try:
        query_results = json.loads(game_details_request.text)
        query_results_df = query_results_df.append(query_results, ignore_index=True)
        game_details_df = game_details_df.append(query_results['results'], ignore_index = True)
    
    except:
        failed_requests.append(guid)
        continue

    #every 500 requests, export df
    if (idx > 0 and idx % 500 == 0 ):
        print('\nWriting progress')

        query_results_df.to_csv('./data/game_details_query_results.csv' , index=False)
        print('game_details_query_results.csv written to ./data/')

        game_details_df.to_csv('./data/game_details.csv', index=False)
        print('game_details.csv written to ./data/\n')



    
    time.sleep(1.2) #space out requests so as not to violate GiantBomb's rate limits
    idx += 1



#final exports, export error list
print('\nWriting final .csv files')
game_details_df.to_csv('./data/game_details.csv', index=False)
query_results_df.to_csv('./data/game_details_query_results.csv', index=False)
pd.Series(failed_requests).to_csv('./data/failed_detail_requests.csv')