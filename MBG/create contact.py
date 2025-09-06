import requests

url = "https://app.mbgcart.com/api/contacts"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
data = {
    "phone": "+1234567890",
    "email": "test@test.com",
    "first_name": "John",
    "last_name": "Smith",
    "gender": "male",
    "actions": [
        {"action": "add_tag", "tag_name": "VIP"},
        {"action": "set_field_value", "field_name": "membership_level", "value": "Gold"},
        {"action": "send_flow", "flow_id": 12345}
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code, response.json())
