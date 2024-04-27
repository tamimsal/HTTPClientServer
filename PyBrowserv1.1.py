import tkinter as tk 
import requests
from tkinter import END
from requests.auth import HTTPBasicAuth

headers = {
    'User-Agent': 'My User Agent',
    'Content-Type': 'application/json'
}

cookies = {
    'cookie_name': 'cookie_value'
}

def get_method():  
    value = entry.get()
    response = requests.get('https://' + value + '.com')
    text_box.delete('1.0', END) 
    text_box.insert(END, response.content)
    text_box.pack()
    getHeadersButton.pack()
    getCookies.pack()
    postMethod.pack()
    
def get_headers():
    value = entry.get()
    response = requests.get('https://' + value + '.com', headers=headers)
    text_box.delete('1.0', END) 
    text_box.insert(END, response.content)
    text_box.pack()

def get_with_auth():
    value = entry.get()
    response = requests.get('https://' + value + '.com', auth=HTTPBasicAuth('username', 'password'))
    text_box.delete('1.0', END) 
    text_box.insert(END, response.content)
    text_box.pack()

def get_cookies():
    value = entry.get()
    response = requests.get('https://' + value + '.com' , cookies=cookies)
    text_box.delete('1.0', END) 
    text_box.insert(END, response.cookies)
    text_box.pack()

def post_method():
    url = 'https://example.com/api'
    data = {'key': 'value'}
    response = requests.post(url, data=data)
    text_box.delete('1.0', END) 
    text_box.insert(END, response.text)
    text_box.pack()

root = tk.Tk()
root.title("TBrowser")
root.geometry("1920x1080")
x = tk.StringVar()
entry = tk.Entry(root)
l = tk.Label(root, text = "The Browser better than Google")
l.config(font =("Courier", 50))
searchButton = tk.Button(root,text="Search", fg="Black", bg="White", command=get_method)
getHeadersButton = tk.Button(root,text="Get Headers", fg="Black", bg="White", command=get_headers)
getWithAuth = tk.Button(root,text="Get with authntication", fg="Black", bg="White", command=get_with_auth)
getCookies = tk.Button(root,text="Get Cookies", fg="Black", bg="White", command=get_cookies)
postMethod = tk.Button(root,text="Post", fg="Black", bg="White", command=post_method)

text_box = tk.Text(root, height=50, width=200) 
l.pack()
entry.pack()
searchButton.pack()

root.mainloop()

