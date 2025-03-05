# import requests
# city = 'london'
# url='https://api.api-ninjas.com/v1/timezone?city={}'.format(city)
# respuesta=requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY'})

# try: 
#     respuesta.status_code != 200
# except requests.Timeout:
#     print("Error: el tiempo de espera ha finalizado")

# datos=respuesta.json()
# import requests

# city = 'london'
# api_url = 'https://api.api-ninjas.com/v1/timezone?city={}'.format(city)
# response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
# if response.status_code == requests.codes.ok:
#     print(response.text)
# else:
#     print("Error:", response.status_code, response.text)

import urllib3


jsonreq = urllib3.request("http://api.open-notify.org/iss-now.json")
response = urllib3.urlopen(jsonreq)
obj = json.loads(response.read())
print (obj['timestamp'])
print (obj['iss_position']['latitude'], obj['data']['iss_position']['latitude'])