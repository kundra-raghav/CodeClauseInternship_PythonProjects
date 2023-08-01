import requests

API_BASE_URL = 'https://cleanuri.com/api/v1/shorten'

def shorten_url(long_url):
    data = {
        'url': long_url,
    }

    try:
        response = requests.post(API_BASE_URL, data=data)
        if response.status_code == 200:
            return response.json().get('result_url')
        else:
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    long_url = input("Enter the URL you want to shorten: ")
    short_url = shorten_url(long_url)
    if short_url:
        print(f"Shortened URL: {short_url}")
    else:
        print("Failed to shorten URL.")

if __name__ == "__main__":
    main()
