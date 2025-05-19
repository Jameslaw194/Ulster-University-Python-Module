# Input a website address
website = input("Enter a website address: ").strip()

# Check if "www" is in the address
if "www" in website:
    # Replace "www" with "http://www"
    new_url = website.replace("www", "http://www", 1)
    print(f"Updated URL: {new_url}")
else:
    print("The address is not valid as it does not contain 'www'.")
