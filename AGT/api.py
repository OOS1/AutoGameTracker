import requests

def get_twitch_user_info(username, client_id, oauth_token):
    base_url = "https://api.twitch.tv/helix/users"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {oauth_token}",
    }
    params = {
        "login": username,
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        user_info = response.json()
        return user_info
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Print the response content for more details
        return None

# Example usage
twitch_username = "skybenn"
your_client_id = "mjqvf2it2wlqmys6vf9usplwr3hx29"
your_oauth_token = "AIzaSyCT6xow_Z4Mf58DpruMeltm0mxVtj0jT0M"  # Replace with your actual OAuth token

user_info = get_twitch_user_info(twitch_username, your_client_id, your_oauth_token)

if user_info:
    print(f"Twitch User ID: {user_info['data'][0]['id']}")
    print(f"Twitch Display Name: {user_info['data'][0]['display_name']}")
