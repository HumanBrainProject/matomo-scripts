import json
import requests


with open('/Users/tsanakts/Desktop/external_users.json', 'r') as userFile, open('/Users/tsanakts/Desktop/external_users_output.json', 'w') as fileMatomo:
    userData = json.load(userFile)
    result = []
    for user in userData:
        md5 = user["md5"]
        url="https://stats.humanbrainproject.eu/index.php?module=API&method=Live.getLastVisitsDetails&idSite=3&period=range&date=2019-07-01,today&filter_limit=-1&segment=userId=={}&format=json&token_auth=<>".format(md5)
        data = requests.get(url).json()
        result = result + data
    json.dump(result, fileMatomo)
