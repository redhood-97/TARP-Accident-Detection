#this is messaging using nexmo

import nexmo
client = nexmo.Client(key='38094c1f', secret='85537034ad5c8b8e')
client.send_message({'from': 'Nexmo', 'to': '918309594362', 'text': 'Hello world'})

