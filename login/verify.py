import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from rest_framework.response import Response
import pdb
client = Client('AC057eb0fda66b130a042ed7196ba0ffa9', '99d77deff0b0c761c5efed9915daaca7')
verify = client.verify.services('VAefd96c6b41c05b078b506a9e8c4ab6f4')


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