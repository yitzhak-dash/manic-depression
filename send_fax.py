import keyring
from twilio.rest import Client

account_sid = keyring.get_password("twilly", "account_sid")
auth_token = keyring.get_password("twilly", "auth_token")

client = Client(account_sid, auth_token)

from_num = '+97237207764'

fax = client.fax.v1.faxes.create(
    from_=from_num,
    to="",
    media_url="https://www.twilio.com/docs/documents/25/justthefaxmaam.pdf")

print(fax.sid)
