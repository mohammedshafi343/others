def shorten_url(url, url_map):
    """Shorten a URL."""
    short_url = f"http://short.ly/{len(url_map) + 1}"
    url_map[short_url] = url
    return short_url

def url_shortener():
    url_map = {}
    
    print("Welcome to the URL Shortener!")
    
    while True:
        url = input("Enter a URL to shorten (or 'exit' to quit): ")
        if url.lower() == 'exit':
            print("Goodbye!")
            break
        
        short_url = shorten_url(url, url_map)
        print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    url_shortener()
