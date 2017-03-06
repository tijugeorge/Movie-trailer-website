from twilio.rest import TwilioRestClient

account_sid = "ACe074a39331e32fd9663153bf624422ef" # Your Account SID from www.twilio.com/console
auth_token  = "0a9df2a83b7dce883cd907d7067866e6"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
	body="Hello this is a test message",
    to="+18067892481",    # Replace with your phone number
    from_="+18068535372") # Replace with your Twilio number

print(message.sid)