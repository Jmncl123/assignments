from unicodedata import name


person = {
    "name": "John",
    "age": 30,
    "city": {
        "name": "New York",
        "country": "USA"
    }
}

person["name"] = "John"
person["height"] = 14.6

a = {}

a["key"] = 1
a["age"] = 20

# print("Second: ",a)  # Accessing values in a dictionary

# del a["age"]

# a.clear()

# print(a)  # Accessing values in a dictionary
# a.get("age")  # Output: 20

# print("Fourth: ", a)  # Accessing values in a dictionary

# del a # This will raise an error if you try to access 'a' after this line

collection = ["Guy", "Mkpouto", "Miracle", "Ikpa", 12, 153.1, True, [1, "yosix", 12, ["Mandem"]] ]

