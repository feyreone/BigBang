import json

result = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        result.append("BIGBANG")
    elif i % 3 == 0:
        result.append("BIG")
    elif i % 5 == 0:
        result.append("BANG")
    else:
        result.append(str(i))

with open('output.json', 'w') as file:
    json.dump(result, file)
