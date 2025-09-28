# Default param values
# You can also a pass a default value for a parameter in a function. If a value is provided for that parameter when the function is called, it will use the provided value. If no value is provided, the function will use the default value.

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

users = {
    "user1":{
        "name":"john",
        "greeting":"Hey"
    },
    "user2":{
        "name":"vikas",
        "greeting":"Namaskar"
    },
    "user3":{
        "name":"Anna"
    }
}

for key,value in users.items():
    if "greeting" in value:
        greet(name=value["name"],greeting=value["greeting"])
    else:
        greet(name=value["name"])

