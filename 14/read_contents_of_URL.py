from  http.client import HTTPConnection
conn = HTTPConnection("example.com")
conn.request("GET","/")
result = conn.getresponse()

# retrives the entire contents
contents = result.read()
print(contents)