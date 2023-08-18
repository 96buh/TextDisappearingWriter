from tkinter import *


class App:
    def __init__(self):
        self.start_text = ""
        self.end_text = ""
        self.start_time = 0
        self.end_time = 0
        # create window
        self.window = Tk()
        self.window.title("Text Disappearing Writer")
        self.window.config(padx=50, pady=50)
        # title label
        self.title = Label(text="Text disappears every five seconds", font=("Arial", 20))
        self.title.grid(row=0, column=0, pady=10)
        # textbox
        self.textbox = Text(font=('Arial', 10))
        self.textbox.focus()
        self.textbox.grid(row=1, column=0)

        self.begin_text()
        self.window.mainloop()

    def begin_text(self):
        self.start_text = self.textbox.get("1.0", "end-1c")
        self.window.after(5000, self.compare_text)

    def compare_text(self):
        self.end_text = self.textbox.get("1.0", "end-1c")

        if self.start_text == self.end_text:
            self.textbox.delete("1.0", END)
            self.textbox.insert("1.0", "")
        self.begin_text()


App()
