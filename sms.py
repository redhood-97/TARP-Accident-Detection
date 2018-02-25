#This is sending SMS using twillio 

from twilio.rest import Client

account_sid = "ACfb32763b6b8d047b86df7534a70245e0"
auth_token = "###"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+918309594362",
    from_="+15024437038 ",
    body="An Accident has occures at the location: (12.9718° N, 79.1589° E)")
