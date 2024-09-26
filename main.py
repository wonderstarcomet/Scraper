import requests 
import json
from bs4 import BeautifulSoup
import customtkinter

URL = "https://devnetproject.netlify.app/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find("body")
body = table.find("script").text.replace(" ","").replace("name", '"name"').replace("phone", '"phone"').replace("specialization",'"speciaization"').replace("experience",'"experience"')[15:-331]
data= json.loads(body)


class myFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.entry = customtkinter.CTkEntry(self, placeholder_text = "search")
        self.button = customtkinter.CTkButton(self, text="Enter", command = self.buttonEvent)
        self.textbox = customtkinter.CTkTextbox(self, width=250,height=100)
        self.entry.pack(padx=20,pady=20)
        self.button.pack(side="top")
        self.textbox.pack(side = "top")

    def buttonEvent(self):

        phoneNum = self.entry.get().replace(" ","")
        self.textbox.delete("0.0","end")
        for table in data:
            if table["name"]==phoneNum:
                nameNum = f"name: {table["name"]}, phone: {table["phone"]}\n"
                self.textbox.insert("0.0", nameNum)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.my_frame = myFrame(master=self)
        self.my_frame.pack(expand = "True", fill= "both")

app = App()
app.mainloop()