import json
import yaml

with open('myfile_12244568.json', 'r') as json_file:
    ourjson = json.load(json_file)

print(ourjson)

print("The access token is: {}".format(ourjson['access_token']))
print("The token expires in {} seconds.".format(ourjson['expires_in']))

print("\n\n---")
print(yaml.dump(ourjson))

print("\nScript created by :\n\n - Name: Adil NOUIRI\n - Studen id: 12244568\n")
