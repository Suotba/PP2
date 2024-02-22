import json

file = open('sample-data.json','r')
data = json.loads(file.read())

total_count = data["totalCount"]
imdata = data["imdata"]

interfaces_list = []

for i in imdata:
    k = i["l1PhysIf"]["attributes"]

    interface_info = {
        "dn": k['dn'],
        "descr": k['descr'],
        "speed": k['speed'],
        "mtu": k['mtu']
    }
    interfaces_list.append(interface_info)

print("Interface Status")
print("="*68)
print("DN\t\t\t\t\t   Description\t Speed\t MTU")
print("-"*42,"-"*12,"-"*7,"-"*4)


for i in interfaces_list:
    print(f"{i['dn']}\t{i['descr']}\t{i['speed']}\t{i['mtu']}")

