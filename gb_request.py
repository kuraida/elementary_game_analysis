import requests
import json
import pandas as pd



user_info = json.loads(open('./auth.json').read())

headers = {'user-agent':user_info['user-agent']} #giant bomb api rejects requests without a unique user-agent


payload = {
    'api_key':user_info['api_key'],
    'format':'json',
    'field_list':'name,original_release_date',
    'sort':'',
    'filter':'',
    'limit':'5'

}


r = requests.get('https://www.giantbomb.com/api/games/', headers=headers, params=payload)



data = json.loads(r.text)

print(data)
# with open('./data/gb_test.json', 'w') as out_file:
#     json.dump(json.loads(r.text), out_file)
#gb_df = pd.DataFrame(json.loads(r.text))


#gb_df.to_csv('./data/gb_test.csv')

