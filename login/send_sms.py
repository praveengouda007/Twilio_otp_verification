# import os
# from twilio.rest import Client
#
#
# account_sid = "AC057eb0fda66b130a042ed7196ba0ffa9"
# auth_token = "3c2a08f683130d6037b2ae6d20542c7c"
# client = Client(account_sid, auth_token)
#
# verification = client.verify \
#                      .services('VA451b54da0c28392025a024aa83ca51d8') \
#                      .verifications \
#                      .create(to='+919398618818', channel='sms')
#
# print(verification.sid)
