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
