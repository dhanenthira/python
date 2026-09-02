import json
# x='{"name":"dhane","age":"21"}'
# y = json.loads(x)


# print(y["age"])

x={
    "name":"dhaen",
    "age ":21,
    "married":False,
    "company name":"toto sportz",
    "pets":"dogs",
    "cars": [
    {"model": "BMW 230", "mpg": 27.5},]
}
y=json.dumps(x)
print(y)