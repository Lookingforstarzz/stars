from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC075c61a242926d2a747344634c0bb374"
auth_token = "556cb68e012ab927fb5648fa29d79a34"
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body="Terra Restore is wonderful.",
    to="+8860965013839",
    from_="+16502854887")
print(message.sid)
