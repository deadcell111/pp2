import json
json_data = """
{
    "totalCount": "400",
    "imdata": [
        {
            "l1PhysIf": {
                "attributes": {
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/33]",
                    "descr": "",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/34]",
                    "descr": "",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/35]",
                    "descr": "",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        }
    ]
}
"""
data = json.loads(json_data)
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 80)
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else ""
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<10}")
