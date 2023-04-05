import pyperclip

# Copy text to the clipboard
pyperclip.copy('Lorem ipsum dolor sit amet')

# Get the text from the clipboard
text = pyperclip.paste()

# Show the text from the clipboard
print(text)
