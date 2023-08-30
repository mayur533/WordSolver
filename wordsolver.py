from tkinter import *
from itertools import permutations, combinations
import enchant
import ttkbootstrap as ttk

root = Tk()
root.title('Word Solver')
root.minsize(400,200)
style = ttk.Style(theme="journal")

# Main Function for finding words
def find_words(event=None):
    letters = letter_entry.get()
    if length_entry.get():
    	length = int(length_entry.get())
    else:
    	length=len(letters) 
    word_dict = enchant.Dict("en_US")
    found_words = set()
    perm = permutations(letters)
    for word_length in range(1, length + 1):
        for word in perm:
            comb = combinations(word, length)
            for c in comb:
                string = "".join(c)
                if word_dict.check(string):
                    found_words.add(string)

    if found_words:
        words_str = ", ".join(found_words)
    else:
        words_str = "No words found."
    statement.config(text=f"Found Words: {words_str}",wraplength=301)

def switch_focus(event):
    if event.keysym == 'Up':
        letter_entry.focus_set()
    elif event.keysym == 'Down':
        length_entry.focus_set()



# Frame for Label and Input
letterframe=ttk.Frame(root)

# Label for letter input
letter_label = ttk.Label(letterframe,text="Enter letters:")
letter_value = StringVar()

# Entry box for letter input
letter_entry = ttk.Entry(letterframe, textvariable=letter_value)
letter_entry.bind("<Return>", find_words)  # Bind "Enter" key to find_words function

letter_label.pack(side="left")
letter_entry.pack(side="left")
letterframe.pack(pady=10)

# Frame for Label and Input
lengthframe=ttk.Frame(root)

# Label for word length input
length_label = ttk.Label(lengthframe,text="Enter length:")

length_value = StringVar()

# Entry box for word length input
length_entry = ttk.Entry(lengthframe, textvariable=length_value)
length_entry.bind("<Return>", find_words)  # Bind "Enter" key to find_words function

length_label.pack(side="left")
length_entry.pack(side="left")
lengthframe.pack(pady=5)

# Button to find words

find_button = ttk.Button(root, text="Find Words",command=find_words)
find_button.pack(pady=5)

# Label to display found words
statement = ttk.Label(root, text="Found Words: ")
statement.pack(pady=5)

# Bind Up and Down keys to switch between input boxes
root.bind("<Up>", switch_focus)
root.bind("<Down>", switch_focus)
# Infinite loop to run the program
root.mainloop()
