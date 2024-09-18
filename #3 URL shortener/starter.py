import pyshorteners

link = input("Type your link: ")

# Initialize the Shortener object
shortener = pyshorteners.Shortener()

# Use the tinyurl shortener to shorten the link
short_link = shortener.tinyurl.short(link)

# Print the shortened link
print(short_link)