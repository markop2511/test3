import requests

APIKey = "01000412b0da673c7cd9ff12855afdf9"
url1 = "https://api.trello.com/1/boards/"
url2 = "https://api.trello.com/1/cards"
APIToken = "ATTA0d8707a7636623c4ba7bcf88210c0393626b49a351c4cb2683a8e1108a71d814266A984D"
idList = "66474426fca3e614c0264515"
idBoard = "66474426fca3e614c026450e"

headers = {
    "Accept": "application/json"
}

query = {
    'key': f"{APIKey}",
    'token': f"{APIToken}",
}

response = requests.get(
    url1 + f"{idBoard}/cards",
    headers=headers,
    params=query
)

board=response.json()
i = 1

for card in board:

    print(f"Card {i}:")
    print("Name:"+card["name"])
    print("Description:"+card["desc"])
    print("-----------------")
    i += 1


def make_card(name, desc):
    query1 = {
        'key': f"{APIKey}",
        'token': f"{APIToken}",
        'idList': f"{idList}",
        'name': f"{name}",
        'desc': f"{desc}"
    }

    response1 = requests.post(
        url2,
        headers=headers,
        params=query1
    )


make_card("New Card2", "New Desc 3")
