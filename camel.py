def camel_to_snake(name: str) -> str:
    return name.lower().replace(" ", "_")

string = input("Enter a camelCase string: ")
print(camel_to_snake(string))