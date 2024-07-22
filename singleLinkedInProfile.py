import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_linkedIn_data():
    api_key = os.environ['PROXYURL_API_KEY']
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    linkedin_profile_url = 'www.linkedin.com/in/aousaf-sulaman'

    response = requests.get(api_endpoint,
                            params={'url': linkedin_profile_url},
                            headers=headers)

    with open('response.txt', 'w') as responseFile:
        responseFile.write(response.text)

def varify_linkedIn_data():
    response = requests.get(os.environ['MY_GIST']).json()
    data ={
        k: v
        for k, v in response.items() if v not in ([], "", "", None) and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == '__main__':
    # get_linkedIn_data()
    data = varify_linkedIn_data()