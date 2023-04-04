import requests
import json

# Set the API endpoint URL
url = 'https://api.linkedin.com/v2/ugcPosts'

# Set the access token for authentication
access_token = 'AQUelWDZJgqgdHsakO0KLCG61xB7Oe5pTDZq1D34GESfuXgqI2IGU8GU1K1_0E5-X8yEaeA1pYshv4i5-ydN6lJWoJvtiOy9y_ITaHLIRZFDOsCBJaOrZk9PBhUUtvFTSwIu0LFzJdWtsggrKxnL4lNnwkHKRv6P3BqFty8OsvoYuEnYZCHaSnwGGUAnP6AG7KZzC08Dw8raOKJYspeCQbqsMBFgI29gafOAYntm1WVUwXodSGviOY80CKkQP4JdBy78alefNaEvE3hnvYVRM-8QxS8NF2DnMlsW5enENOzA1X3tomPbR8aJa1tWxjFYXS1IH4cQuqrP7LDtYv0MiRFj4MdmQQ'

# Set the headers for the API request
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}

# Set the payload for the API request
payload = {
    'author': 'urn:li:page:https://www.linkedin.com/company/memes-ai/',
    'lifecycleState': 'PUBLISHED',
    'specificContent': {
        'com.linkedin.ugc.ShareContent': {
            'shareCommentary': {
                'text': 'Hello, LinkedIn!'
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
