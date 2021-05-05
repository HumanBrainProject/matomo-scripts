#  Copyright 2018 - 2021 Swiss Federal Institute of Technology Lausanne (EPFL)
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0.
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  This open source software code was developed in part or in whole in the
#  Human Brain Project, funded from the European Union's Horizon 2020
#  Framework Programme for Research and Innovation under
#  Specific Grant Agreements No. 720270, No. 785907, and No. 945539
#  (Human Brain Project SGA1, SGA2 and SGA3).
#

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