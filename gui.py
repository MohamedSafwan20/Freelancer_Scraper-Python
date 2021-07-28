from tkinter import *
import scraper

root = Tk()

root.title("Freelancer scraper")
root.geometry("1000x700")
root.configure(background="#55595e")

Button(root, text="Scrape", command=lambda: scraper.scrape_freelancer(text),
       width=7).grid(row=0, column=0)

Button(root, text="Clear", width=7, command=lambda: text.delete(
    "1.0", END)).grid(row=0, column=1)

text = Text(root, width=100, height=40, wrap="word")
text.grid(row=1, column=3)

root.mainloop()
