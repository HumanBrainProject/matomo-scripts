import json
import requests


with open('user_md5.json', 'r') as userFile, open('matomo_dump.json', 'w') as fileMatomo:
    userData = json.load(userFile)
    result = []
    for user in userData:
        md5 = user["rmd5"]
        url="https://stats.humanbrainproject.eu/index.php?module=API&method=Live.getLastVisitsDetails&idSite=3&period=range&date=FROM,TILL&filter_limit=-1&segment=userId=={}&format=json&token_auth=YOUR_TOKEN".format(md5)
        data = requests.get(url).json()
        result = result + data
    json.dump(result, fileMatomo)
