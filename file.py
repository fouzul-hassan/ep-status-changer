# import requests

# def generate_access_token(client_id, client_secret, redirect_uri, authentication_type):
#     auth_url = "https://auth.aiesec.org/oauth/token"
#     payload = {
#         "client_id": client_id,
#         "client_secret": client_secret,
#         "redirect_uri": redirect_uri,
#         "grant_type": "authorization_code",
#         "authentication_type": authentication_type
#     }
    
#     response = requests.post(auth_url, data=payload)
    
#     if response.status_code == 200:
#         access_token = response.json().get('access_token')
#         return access_token
#     else:
#         print("Failed to generate access token.")
#         return None

# # Replace these values with your actual credentials
# client_id = "ed49400689754839e34e8b172d0a11940a9398b10635188b3d5eaeb396cf8d14"
# client_secret = "14a2489b3539579435c721648f2f333362842661ba9f42ac3cc096066a3a5263"
# redirect_uri = "https://eplore.aiesec.lk/"
# authentication_type = "login"

# access_token = generate_access_token(client_id, client_secret, redirect_uri, authentication_type)
# if access_token:
#     print("Access token:", access_token)
# else:
#     print("Failed to generate access token.")
