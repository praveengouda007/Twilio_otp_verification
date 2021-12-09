import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from rest_framework.response import Response
import pdb
client = Client('AC057eb0fda66b130a042ed7196ba0ffa9', '0577b4fe219bdfe4aef82665477c7bea')
verify = client.verify.services('VAfdd5dabf289d15ffcbc869163e22eae3')


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