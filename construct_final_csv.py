import pandas as pd 

data = pd.read_csv("/Users/tsanakts/Desktop/external_users_output.csv") 
final =  data.groupby(['userId', 'clientId', 'countryCode'])['clientId'].count().reset_index(name="count")
final.to_csv("/Users/tsanakts/Desktop/external_users_output_final.csv",index=False)

        
    
