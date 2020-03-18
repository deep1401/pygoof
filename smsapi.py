import requests
url = "https://www.fast2sms.com/dev/bulk"
message = "Hello testing from sms api"
payload = f"sender_id=FSTSMS&message={message}&language=english&route=p&numbers=7021320212,9757199266"

headers = {
'authorization': "API Key",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)