import tkinter as tk 
import webview 

def get_square_root():  
    value = entry.get()
    webview.create_window(value, 'https://' + value + '.com', width= 1920, height= 1080) 
    webview.start() 
    
root = tk.Tk()
root.title("TBrowser")
root.geometry("1920x1080")
x = tk.StringVar()
entry = tk.Entry(root)
l = tk.Label(root, text = "The Browser better than Google")
l.config(font =("Courier", 50))
searchButton = tk.Button(root,text="Search", fg="Black", bg="White", command=get_square_root)
l.pack()
entry.pack()
searchButton.pack()

root.mainloop()