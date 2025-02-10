import requests

url = 'https://www.tu.ac.th'
conn = requests.get(url)

print(conn.status_code)

data = conn.content
print(len(data))
print(data[:200])

for key in conn.headers:
    print("{} : {}".format(key, conn.headers[key]))
