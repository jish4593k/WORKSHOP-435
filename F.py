import os
import time
import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter

time1 = time.time()

def get_pdf_files(directory):
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

def convert_pdfs_to_word(pdf_files):
    for pdf_file in pdf_files:
        docx_file = os.path.splitext(pdf_file)[0] + '.docx'
        cv = Converter(pdf_file)
        cv.convert(docx_file, start=0, end=None)
        cv.close()

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, folder_selected)

def convert_and_display():
    folder_path = entry_path.get()
    pdf_files_list = get_pdf_files(folder_path)

    if not pdf_files_list:
        status_label.config(text="No PDF files found in the specified folder.")
    else:
        convert_pdfs_to_word(pdf_files_list)
        status_label.config(text="Conversion completed successfully.")

    time2 = time.time()
    elapsed_time_label.config(text='Elapsed time: {}s'.format(round(time2 - time1, 2)))

up
root = tk.Tk()
root.title("PDF to DOCX Converter")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=20, pady=20)

label_path = tk.Label(frame, text="Select Folder:")
label_path.grid(row=0, column=0, sticky='e')

entry_path = tk.Entry(frame, width=50)
entry_path.grid(row=0, column=1, padx=5)

button_browse = tk.Button(frame, text="Browse", command=select_folder)
button_browse.grid(row=0, column=2, padx=5)

button_convert = tk.Button(frame, text="Convert", command=convert_and_display)
button_convert.grid(row=1, column=1, pady=10)

status_label = tk.Label(frame, text="")
status_label.grid(row=2, column=0, columnspan=3, pady=10)

elapsed_time_label = tk.Label(frame, text="")
elapsed_time_label.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
