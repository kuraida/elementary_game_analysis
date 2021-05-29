import ast 
import pandas as pd
import numpy as np


'''
***THIS IS A PRELIMINARY SCRIPT - AT A LATER DATE THIS SECTION OF THE PROJECT WILL OCCUPY ITS OWN JUPYTER NOTEBOOK***



Many of the fields in the GiantBomb API query results are formatted as json references to separate API resources. Since querying the full content of those resources is beyond the scope of this project and would constitute undue strain
on GiantBomb's api, here we will simply pull relevant details out of the json string and export them to their own .csvs. Because these will come from the data we have queried for this project, this will not be a complete representation
of the data hosted on GiantBomb, but rather a catalog of the field values appearing in this project's data.

Here we will identify the columns we want to parse, convert the json strings to dicts, pull out the relevant info, and replace the values in the source dataframe/csv/table with the id reference to cut down on redundancy.

'''




def parse_json(in_df, fields):

    #games details - future goal is to make this function generic so that it can be run against all api query csvs
    for field in fields: #columns from data source that are formatted as api references
        
        out_df = pd.DataFrame()
        for idx in in_df.index: #needs to be run for each record to capture all unique values for each field
            
            item_list = []
            

                
            json_string = in_df.loc[idx][field]
            
            try:
                json_eval = ast.literal_eval(json_string) #returns json object as python dict
            except:
                continue

            #replace api references in source data with python list of unique ids,  append record dicts to output dataframe
            for item in json_eval:
                item_list.append(item['id'])
                out_df = out_df.append(item, ignore_index=True)
            
            in_df.at[idx, field] = item_list

       
        out_df.drop_duplicates().to_csv('./data/' + field + '.csv', index=False) #only export unique records

    return in_df





def main():
    
    df = pd.read_csv('./data/game_details.csv')
    field_list = ['platforms', 'franchises', 'developers']
    parsed_df = parse_json(df, field_list)
    parsed_df.to_csv('./data/game_details_parsed.csv', index=False)

main()
