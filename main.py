import tkinter as tk
import requests
import json   

def words():
    word = word_entry.get()
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    r = requests.get(url)
    wdict = json.loads(r.text)
    try:
        data = wdict[0]["meanings"][0]["definitions"][0]["definition"]
        output_lable.config(text=f"{data}")
    except Exception as e:
        output_lable.config(text="Error Enter the Correct word")
    

window = tk.Tk()
window.title("Word Search")

word_label = tk.Label(window,text="Enter the Word")
word_label.pack()

word_entry = tk.Entry(window)
word_entry.pack()

word_button = tk.Button(window,text="Search",command=words)
word_button.pack()

output_lable = tk.Label(window,text="")
output_lable.pack()

window.mainloop()