import pandas as pd 

data = pd.read_csv("matomo_output.csv") 
final =  data.groupby(['userId', 'clientId'])['clientId'].count().reset_index(name="count")
final.to_csv("final.csv",index=False)

        
    
