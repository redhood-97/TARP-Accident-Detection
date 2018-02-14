
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+12316851234",
    from_="+15555555555",
    body="Hello there!")