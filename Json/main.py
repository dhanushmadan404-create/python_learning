# {
#   "name":"Alex",
#   "age":25,
#   "isStudent":true,
#   "skills":["python","SQL"],
#   "address":{
#     "city":"chennai",
#     "pinCode":600100
#   }
# }
# import json

# person_str = '{"name": "Alex","age": 25,"isStudent": true,"skills": ["python", "SQL"],"address": {"city": "chennai","PinCode": 600100}"}'
# loads
# person = json.loads(person_str)
# print(person['address']['city'])
# print(person['skill'])

# dumps
# import json
# person_str={"name": "Alex","age": 25,"isStudent": True,"skills": ["python", "SQL"],"address": {"city": "chennai","PinCode": 600100}}
# a=json.dumps(person_str)
# print(type(a))

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and
# 
# 
# import json
# import requests
# # Step 1: Make a GET request to the API
# response = requests.get("https://randomuser.me/api/")
# # Step 2: Convert response JSON → Python dict
# data = response.json()
# # Step 3: Extract some values
# user = data["results"][0]
# name = user["name"]["first"]
# email = user["email"]
# city = user["location"]["city"]
# print("Name:", name)
# print("Email:", email)
# print("City:", city)

# nums = [1, 2, 3, 2, 2, 4]
# target = 2
# count = 0
# for i in range(nums):
#     if nums[i] == target:
#         count += 1
# print(count)

# text = "I love Python"
# count = 1
# for ch in text:
#     if ch == " ":
#         count += 1
# print("Words:", count)

# text = "banana"
# for ch in text:
#     c = 0
#     for i in range(len(text)):
#         if text[i] == ch:
#             c = c + 1
#     print(ch, ":", c)