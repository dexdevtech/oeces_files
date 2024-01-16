import requests

def send_message(phone_number, message, authorization_token):
    # Change url
    url = 'http://192.168.1.43:8082'
    template = {
        "to": phone_number,
        "message": message
    }

    headers = {
        'Authorization': authorization_token
    }

    try:
        response = requests.post(url, json=template, headers=headers)
        response.raise_for_status()  # Raise an exception if the request was not successful
        print("SMS sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send SMS: {e}")

# Replace 'TOKEN' with the actual authorization token you have.
authorization_token = 'e9265c1f-1faf-4502-a468-aa831c4eb397'

# # Replace '{phone}' and '{message}' with the phone number and the message you want to send.
# phone_number = '09953167142'
# message = 'Your SMS message here'

# send_message(phone_number, message, authorization_token)
