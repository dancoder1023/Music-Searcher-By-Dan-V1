from googlesearch import search
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

def search_music_by_genre_and_instrument(genre, instrument):
    query = f"{genre} {instrument} music site:youtube.com OR site:spotify.com"
    links = list(search(query, num_results=30))

    if not links:
        return ["No results found."]

    return links

def on_search():
    genre = genre_entry.get()
    instrument = instrument_entry.get() if include_instrument_var.get() else ""
    results = search_music_by_genre_and_instrument(genre, instrument)
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Here are the top links for your search:\n\n")
    for result in results:
        result_text.insert(tk.END, result + "\n")
    result_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Music Searcher by Dan")
root.geometry("600x500")
root.resizable(False, False)

# Create and place the widgets
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="Enter the music genre you want to search for:").grid(row=0, column=0, pady=10, sticky=tk.W)
genre_entry = ttk.Entry(frame, width=50)
genre_entry.grid(row=1, column=0, pady=5, sticky=tk.W)

ttk.Label(frame, text="Enter the instrument you want to search for:").grid(row=2, column=0, pady=10, sticky=tk.W)
instrument_entry = ttk.Entry(frame, width=50)
instrument_entry.grid(row=3, column=0, pady=5, sticky=tk.W)

include_instrument_var = tk.BooleanVar()
include_instrument_var.set(True)
include_instrument_checkbox = ttk.Checkbutton(frame, text="Include instrument in search", variable=include_instrument_var)
include_instrument_checkbox.grid(row=4, column=0, pady=5, sticky=tk.W)

search_button = ttk.Button(frame, text="Search", command=on_search)
search_button.grid(row=5, column=0, pady=10, sticky=tk.W)

result_text = scrolledtext.ScrolledText(frame, width=70, height=15, state=tk.DISABLED, wrap=tk.WORD)
result_text.grid(row=6, column=0, pady=10, sticky=tk.W)

# Run the application
root.mainloop()
