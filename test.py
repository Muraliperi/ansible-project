#!/usr/bin/env python3
import json

ansible_facts =  {
        "ansible_all_ipv4_addresses": [
            "192.168.xx.1"
        ],
        "ansible_all_ipv6_addresses": [
            "xxyyzz"
        ],
        "ansible_apparmor": {
            "status": "disabled"
        },
}

print(json.dumps(ansible_facts, indent=4))
