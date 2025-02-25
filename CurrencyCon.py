import http.client
import json

conn = http.client.HTTPSConnection("api.fxratesapi.com")
while (1):
    f = open("input.txt", "r")
    x = f.read()
    f.close
    if (x != None):
        try:
            origin, destination, amount = x.split()
        except ValueError:
                continue
        conn.request("GET", f"/convert?from={origin}&to={destination}&amount={amount}")
        res = conn.getresponse()
        datajson = res.read()
        try:
            data = json.loads(datajson)
            conversion_result = data.get("result", "Error: No result found")
        except json.JSONDecodeError:
            conversion_result = "Error"
        f = open("input.txt", "w")
        if (conversion_result == None):
             f.write("Error")
             f.close
        else:
            conversion_result = str(round(conversion_result, 2))
            f.write(f"{conversion_result}")
            f.close