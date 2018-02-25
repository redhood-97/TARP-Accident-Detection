#This is sending SMS using twillio 

from twilio.rest import Client

account_sid = "ACfb32763b6b8d047b86df7534a70245e0"
auth_token = "f4e3fd3210a3e056d355d17eec5dad82"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+917660066152",
    from_="+15024437038 ",
    body="An Accident has occures at the location: (12.9718° N, 79.1589° E)")


# from twilio.rest import Client

# # Find these values at https://twilio.com/user/account
# account_sid = "ACfb32763b6b8d047b86df7534a70245e0"
# auth_token = "your_auth_token"

# client = Client(account_sid, auth_token)

# client.api.account.messages.create(
#     to="+12316851234",
#     from_="+15555555555",
#     body="Hello there!")