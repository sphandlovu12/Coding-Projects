import webbrowser

url = input("Enter url: ")
webbrowser.open(url)

# Open the page in a new browser window
webbrowser.open_new('url')

# Open the page in a new browser tab
webbrowser.open_new_tab('url')