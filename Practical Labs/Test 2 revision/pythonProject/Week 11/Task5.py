def update_website_url(url):
    if url.startswith("www.") and not url.startswith("http://www."):
        new_url = url.replace("www.", "http://www.")
        return f"Updated URL: {new_url})"
    return f"The URL {url} is already valid."

url = input("Enter a website address: ")
print(update_website_url(url))