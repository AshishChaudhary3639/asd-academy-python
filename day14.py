import requests

# 1. Define REST API endpoint
base_url = "https://reqres.in/api/users"

# 2. GET request to fetch user data
# print("GET Request Example:")
# response = requests.get(f"{base_url}/1")
# print(response)
# if response.status_code == 200:
#     user_data = response.json()
#     print("ID:", user_data['data']['id'])
#     print("Name:", user_data['data']['first_name'], user_data['data']['last_name'])
#     print("Email:", user_data['data']['email'])
# else:
#     print("Failed to GET data")

# print("\n" + "-" * 50 + "\n")

# 3. POST request to create user
# print("POST Request Example:")
# new_user = {
#     "name": "Asif Farooq",
#     "job": "Teacher"
# }
# response = requests.post(base_url, json=new_user)
# print(response.status_code)
# print(response.text)
# print("Requesting URL:", response.request.url)
# if response.status_code == 201:
#     created_user = response.json()
#     print("Name:", created_user['name'])
#     print("Job:", created_user['job'])
#     print("ID:", created_user['id'])
#     print("Created At:", created_user['createdAt'])
# else:
#     print("Failed to POST data")

# print("\n" + "-" * 50 + "\n")

# # 4. PUT request to update user
# print("PUT Request Example:")
# updated_user = {
#     "name": "Asif Farooq",
#     "job": "Senior Teacher"
# }
# response = requests.put(f"{base_url}/2", json=updated_user)
# print(response.text)
# if response.ok:
#     updated_data = response.json()
#     print("Updated Name:", updated_data['name'])
#     print("Updated Job:", updated_data['job'])
#     print("Updated At:", updated_data['updatedAt'])
# else:
#     print("Failed to update")

# print("\n" + "-" * 50 + "\n")

# 5. DELETE request to remove user
# print("DELETE Request Example:")
# response = requests.delete(f"{base_url}/2")
# print(response.text)
# if response.status_code == 204:
#     print("User deleted successfully")
# else:
#     print("Failed to delete user")

# print("\n" + "-" * 50 + "\n")


import requests

base_url = "https://reqres.in/api/users"

# Step 1: GET Request
print("GET Request Example:")
response = requests.get(f"{base_url}/1")
print("Status Code:", response.status_code)

if response.status_code == 200:
    user_data = response.json()
    first_name = user_data['data']['first_name']
    last_name = user_data['data']['last_name']
    email = user_data['data']['email']

    print("ID:", user_data['data']['id'])
    print("Name:", first_name, last_name)
    print("Email:", email)

    print("\n" + "-" * 50 + "\n")

    # Step 2: POST Request using the same data
    print("POST Request Example:")
    post_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }

    response = requests.post(base_url, json=post_data)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code == 201:
        created_user = response.json()
        print("Created First Name:", post_data['first_name'])
        print("Created Last Name:", post_data['last_name'])
        print("Email:", post_data['email'])
        print("Returned ID:", created_user.get('id', 'N/A'))
        print("Created At:", created_user.get('createdAt', 'N/A'))
    else:
        print("Failed to POST data")

else:
    print("Failed to GET data")

print("\n" + "-" * 50 + "\n")

