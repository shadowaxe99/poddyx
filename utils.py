import requests


def send_notification(message):
    # Send a notification using an external API
    response = requests.post('https://api.example.com/notifications', json={'message': message})
    if response.status_code == 200:
        return True
    else:
        return False
