import re

phoneNumberRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

example = "The number is 123-456-7890."

result = phoneNumberRegex.search(example)

if result:
    print(example)
    print("Phone number found:", result.group())
    print("Area code:", result.group()[0:3])
    
    