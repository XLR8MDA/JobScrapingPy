import requests
import json
import openai
import random

# Set up your OpenAI API key
openai.api_key = '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'

# Generate a joke using the OpenAI API
def generate_joke():
    lang = ['python', 'java', 'html', 'rust', 'c++', 'html', 'css', 'javascript', 'go', 'flutter']
    # Select a random language
    lang = random.choice(lang)
    print(lang)
    prompt = "Tell me a joke in " + lang + "?"

    max_tokens = 60  # Maximum length of the joke 
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.6
    )
    
    joke = response.choices[0].text.strip()
    return joke

# Call the function to generate a joke
joke = generate_joke()
print(joke)

# Set the API endpoint URL
url = 'https://api.linkedin.com/v2/ugcPosts'

# Set the access token for authentication
access_token = 'AQW7Ho2mEejtGoIewNFiciJkN-ZFlZlif2gXVoOcIPXdj51em1xG2UuZ1h_T4Zdg0c42L68IR56nuaknYOJ6vlNOEhwTJ9hOlD5oBoUJnXEilg23It9JPPvbDl-xd7XDV2hn1Ot_M0AQTur9vhiPG-aQ2VxgIZBrlBB5zy56q6YgcteFfPt1uEy8wDVV63TP7XitiMF8w0ISh4Eu5dvNuWT0YgzH3e5OSyDCi49UGx5fXvBtWI_nfbbqT8i7ZUiBSMEZ9nss9FzJkUNIpqT3oyKxStkbEpr4NgfV4cRquzVVOw2Me3-NFfdUYWJl4_1W0oVbN_RrqBefA7lIjHSOjaGKF9aCQg'

# Set the headers for the API request
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}

# Set the payload for the API request
payload = {
    'author': 'urn:li:person:memes-ai',
    'lifecycleState': 'PUBLISHED',
    'specificContent': {
        'com.linkedin.ugc.ShareContent': {
            'shareCommentary': {
                'text': "HI, I'M BACK!"  # Use the generated joke as the text
            },
            'shareMediaCategory': 'NONE'
        }
    },
    'visibility': {
        'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC'
    }
}

# Convert the payload to a JSON string
json_payload = json.dumps(payload)

# Send the API request
response = requests.post(url, headers=headers, data=json_payload)

# Check if the response was successful (status code 201)
if response.status_code == 201:
    # Print a success message if the post was created successfully
    print('Post created successfully!')
else:
    # Print an error message if the post creation was unsuccessful
    print('Error: ' + str(response.status_code))
