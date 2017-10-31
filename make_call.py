from twilio.rest import Client
import time
import sys
import threading
import keyring

account_sid = keyring.get_password("twilly", "account_sid")
auth_token = keyring.get_password("twilly", "auth_token")

client = Client(account_sid, auth_token)

# from_num="+97237207764"
from_num = '+972733948111'

to_numbers = ["+972733948313",
              "+972733949364",
              "+972733949357",
              "+972733948243",
              "+972733949359",
              "+972733949364",
              "+972733948428",
              "+972733949370",
              "+972733948378",
              "+972733948378",
              "+972733949354",
              "+972733949329",
              "+972733948031",
              "+972733948173",
              "+972733948150",
              "+972733948117",
              "+972733948382",
              "+972733948193",
              "+972733948176",
              "+972733948168",
              ]


# Make the call
def make_call(to):
    call = client.api.account.calls \
        .create(to=to,
                from_=from_num,
                url="http://demo.twilio.com/hellomonkey/monkey.mp3")
    return call


def call_wait_end(to_num, sec):
    print('calls to {0}'.format(to_num))
    call = make_call(to_num)
    if sec is not None:
        time.sleep(sec)
        call.update(status="completed")
        print('[*] call to {0} ended'.format(call.to))


if __name__ == '__main__':
    sleep_sec = None
    if len(sys.argv) > 1:
        sleep_sec = int(sys.argv[1])
    for to_num in to_numbers:
        try:
            t = threading.Thread(target=call_wait_end, args=(to_num, sleep_sec))
            t.start()
        except:
            print('Error')
