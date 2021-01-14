import json
import csv

with open('/Users/tsanakts/Desktop/external_users_output.json', encoding='utf-8') as matomoJson, open('/Users/tsanakts/Desktop/external_users_output.csv', 'w') as output:
    data = json.load(matomoJson)
    result = csv.writer(output, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    result.writerow(["userId", "countryCode", "siteName", "clientId", "url", "count"])

    for item in data:
        userId = item["userId"]
        countrycode = item["countryCode"]
        siteName = item["siteName"]
        action_details = item["actionDetails"]
        for action in action_details:
            eventAction = action["eventAction"]
            url = action["url"]
            result.writerow([userId, countrycode, siteName, eventAction, url])