import requests
import json


# 1. Define a REST API endpoint
base_url = "https://jsonplaceholder.typicode.com/posts"

# 2. GET request to fetch data (Reading from REST API)
print("GET Request Example:")
response = requests.get(f"{base_url}/1")
# print(response.text)
if response.status_code == 200:
    print(response.text) #To check JSON format data
    post_data = response.json()  # Parsing JSON
    print(post_data)
    print("Title:", post_data['title'])
    print("User ID",post_data['userId'])
    print("Body:", post_data['body'])
else:
    print("Failed to GET data")

print("\n" + "-"*50 + "\n")

# 3. POST request to create data (Sending JSON to REST API)
# print("POST Request Example:")
# new_post = {
#     "title": "Teaching REST API",
#     "body": "This is a post created from Python.",
#     "userId": 105
# }
# response = requests.post(base_url, json=new_post)
# if response.status_code == 201:#For Creation
#     created_post = response.json() #Parsing JSON  Data
#     print("New Post ID:", created_post['title'])
#     print("UserId:",created_post['userId'])
# else:
#     print("Failed to POST data")
# print("\n" + "-"*50 + "\n")

# 4. PUT request to update data
# print("PUT Request Example:")
# update_data = {
#     "id": 1,
#     "title": "Updated Title",
#     "body": "Updated body text.",
#     "userId": 1
# }
# response = requests.put(f"{base_url}/1", json=update_data)
# if response.ok:
#     print("Updated Post:", response.json())
#     created_post=response.json()
#     print("New Post ID:", created_post['body'])
# else:
#     print("Failed to update")

# print("\n" + "-"*50 + "\n")

# # 5. DELETE request to remove data
# print("DELETE Request Example:")
# response = requests.delete(f"{base_url}/1")
# if response.status_code == 200:
#     print("Post deleted successfully")
# else:
#     print("Failed to delete")

# print("\n" + "-"*50 + "\n")

# 6. Creating and writing your own JSON
# print("Creating and Writing JSON to File:")
# person = {
#     "name": "Asif",
#     "skills": ["Python", "Django", "API"],
#     "teacher": True
# }
# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4)
# print("JSON written to 'person.json'")

# # # 7. Reading and parsing JSON from file
# print("\nParsing JSON from File:")
# with open("person.json") as file:
#     data = json.load(file)  #Converts this into Python Dictionary
#     print("Name:", data["name"])
#     print("Skills:", data["skills"])


# import json

# # Python dictionary (Python object)
# person = {
#     "name": "Asif",
#     "age": 30,
#     "skills": ["Python", "Django"]
# }
# print("Dictionary Format=",person)
# # # 1. Convert Python object to JSON string using json.dumps()
# person_json = json.dumps(person, indent=4)
# print("JSON String (using dumps):")
# print(person_json)

# # print("\n" + "-"*50 + "\n")

# # # # # 2. Convert JSON string back to Python object using json.loads()
# person_dict = json.loads(person_json)
# print("Python Dictionary (using loads):")
# print(person_dict)
