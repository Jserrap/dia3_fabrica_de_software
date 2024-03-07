import requests

manaira = requests.gets("https:viacep.com.br/ws/58038420/json/")

json = manaira.json()

print(json.get("cep", "não tem cep"))