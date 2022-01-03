from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from rest_framework.response import Response
import pdb
client = Client('AC057eb0fda66b130a042ed7196ba0ffa9', 'a7a6cc1b25d1b4fb7d63b407817f26c5')
verify = client.verify.services('VA9260e4baf262c81d1240ad3ead0117ee')


def send(phone):
    #pdb.set_trace()
    verify.verifications.create(to=phone, channel='sms')


def check(phone, code):
    # pdb.set_trace()
    try:
        result = verify.verification_checks.create(to=phone, code=code)

    except TwilioRestException:
        print('no')
        return False

    return result.status == 'approved'