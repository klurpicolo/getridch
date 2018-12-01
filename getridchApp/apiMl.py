import requests
import json

# ML API setting

url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/1358c02e-1370-4c30-afee-730cbb960af5/url"

querystring = {"iterationId": "a633a484-891c-47bc-8c4f-9d5e86a2ce7f"}

payload = "{\"Url\": \"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWYF4eeDbeh8co7TmNP2rLTgpexfmqwgDFNuYNba4BE8WwIpan\"}"
headers = {
    'prediction-key': "e46e7620ef0448e19fb945f23248506c",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "1c429c57-1a28-1a9f-43f7-df508e588b91"
}


def getObjectType():
    '''



    :return: String | Most probably object
    '''
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    # print(response.json())
    maxprob = 0
    maxprobtype = ''
    for project in response.json()['predictions']:
        if project['probability'] > maxprob:
            maxprob = project['probability']
            maxprobtype = project['tagName']
    return maxprobtype


if __name__ == '__main__':
    print(getObjectType())
