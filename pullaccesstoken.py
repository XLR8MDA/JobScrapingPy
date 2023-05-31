import requests

# Set the API endpoint URL
url = 'https://api.linkedin.com/v2/organizations'

# Set the access token for authentication
access_token = 'AQW7Ho2mEejtGoIewNFiciJkN-ZFlZlif2gXVoOcIPXdj51em1xG2UuZ1h_T4Zdg0c42L68IR56nuaknYOJ6vlNOEhwTJ9hOlD5oBoUJnXEilg23It9JPPvbDl-xd7XDV2hn1Ot_M0AQTur9vhiPG-aQ2VxgIZBrlBB5zy56q6YgcteFfPt1uEy8wDVV63TP7XitiMF8w0ISh4Eu5dvNuWT0YgzH3e5OSyDCi49UGx5fXvBtWI_nfbbqT8i7ZUiBSMEZ9nss9FzJkUNIpqT3oyKxStkbEpr4NgfV4cRquzVVOw2Me3-NFfdUYWJl4_1W0oVbN_RrqBefA7lIjHSOjaGKF9aCQg'

# Set the headers for the API request
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}

# Send the API request
response = requests.get(url, headers=headers)

# Check if the response was successful (status code 200)
if response.status_code == 200:
    # Print the response content (LinkedIn profile information)
    print(response.json())
else:
    # Print an error message if the request was unsuccessful
    print('Error: ' + str(response.status_code))
