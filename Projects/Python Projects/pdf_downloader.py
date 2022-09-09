import urllib.request

url = input("Enter link to download PDF: ")
name = input("Enter a name for the PDF file: ")
filename = name + ".pdf"
urllib.request.urlretrieve(url, filename)