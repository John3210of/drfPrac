from django.test import TestCase
import json
# Create your tests here.

import json

maData = [{
    "name": "asdf",
    "age": 1,
    "active": True,
    "list": [
        {
            "lst1": "123",
            "lst2": "234",
            "len": 2
        }

    ]
},
{
    "name": "asdf",
    "age": 1123,
    "active": True,
    "list": [
        {
            "lst1": "121233",
            "lst2": "234",
            "len": 2123
        }

    ]
}
]

for i in maData:
    print(i["name"])


