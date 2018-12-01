import requests

prc_bottle = 0.5
prc_can = 0.6
prc_glass = 0.4


def getObjectType():
    '''



    :return: String | Most probably object
    '''
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

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    # print(response.json())
    maxprob = 0
    maxprobtype = ''
    for project in response.json()['predictions']:
        if project['probability'] > maxprob:
            maxprob = project['probability']
            maxprobtype = project['tagName']
    return maxprobtype


def getObjectDetection(data):
    url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/f8f2f5c1-3f93-4a67-ab5c-6d1998961457/image"

    querystring = {"iterationId": "07f8a4d6-8602-471f-b14d-bc97b6fb3f27"}

    headers = {
        'prediction-key': "e46e7620ef0448e19fb945f23248506c",
        'content-type': "application/octet-stream",
        'cache-control': "no-cache",
        'postman-token': "782a434f-c206-3e04-c95e-012ed968db49"
    }

    response = requests.request("POST", url, data=data, headers=headers, params=querystring)
    qtybottle = 0
    qtycan = 0
    qtyglass = 0

    for prediction in response.json()['predictions']:
        if prediction['probability'] <= 0.33:
            continue

        if prediction['tagName'] == 'bottle':
            qtybottle = qtybottle + 1
        elif prediction['tagName'] == 'can':
            qtycan = qtycan + 1
        elif prediction['tagName'] == 'glass':
            qtyglass = qtyglass + 1

    print("There are %d bottle" % (qtybottle))
    print("There are %d can" % (qtycan))
    print("There are %d glass" % (qtyglass))
    total = (prc_bottle * qtybottle) + (prc_can * qtycan) + (prc_glass * qtyglass)
    print("Total is %d " % total)
    return_dict = {'Total': total, 'qty_bottle': qtybottle, 'prc_bottle': prc_bottle, 'qty_can': qtycan, 'prc_can': prc_can,'qty_glass': qtyglass, 'prc_glass': prc_glass}

    return return_dict


if __name__ == '__main__':
    data = open('C:/Users/warit.b/Downloads/used plastic bottle _ Google Search/444.jpg', 'rb').read()
    print(getObjectDetection(data)['Total'])
