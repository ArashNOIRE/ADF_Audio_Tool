import tkinter as tk
from tkinter import filedialog, messagebox

def xor_file(input_path, output_path):
    try:
        with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
            byte = f_in.read(1)
            while byte:
                f_out.write(bytes([byte[0] ^ 0x22]))
                byte = f_in.read(1)
        messagebox.showinfo("Success", f"Conversion completed successfully:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3"), ("ADF files", "*.adf")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".adf", filetypes=[("ADF files", "*.adf"), ("MP3 files", "*.mp3")])
    if file_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)

def convert_mp3_to_adf():
    input_path = input_entry.get()
    output_path = output_entry.get()
    if not input_path.endswith(".mp3"):
        messagebox.showerror("Error", "Input file must be an MP3.")
        return
    if not output_path.endswith(".adf"):
        messagebox.showerror("Error", "Output file must be an ADF.")
        return
    xor_file(input_path, output_path)

def convert_adf_to_mp3():
    input_path = input_entry.get()
    output_path = output_entry.get()
    if not input_path.endswith(".adf"):
        messagebox.showerror("Error", "Input file must be an ADF.")
        return
    if not output_path.endswith(".mp3"):
        messagebox.showerror("Error", "Output file must be an MP3.")
        return
    xor_file(input_path, output_path)

# Create main window
root = tk.Tk()
root.title("MP3 <-> ADF Converter for GTA VC")

# Input file field
tk.Label(root, text="Input File:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)
input_btn = tk.Button(root, text="Select File", command=select_input_file)
input_btn.grid(row=0, column=2, padx=5, pady=5)

# Output file field
tk.Label(root, text="Output File:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=5, pady=5)
output_btn = tk.Button(root, text="Select Save Location", command=select_output_file)
output_btn.grid(row=1, column=2, padx=5, pady=5)

# Conversion buttons
convert_mp3_btn = tk.Button(root, text="MP3 → ADF", command=convert_mp3_to_adf)
convert_mp3_btn.grid(row=2, column=1, pady=10, sticky='w')

convert_adf_btn = tk.Button(root, text="ADF → MP3", command=convert_adf_to_mp3)
convert_adf_btn.grid(row=2, column=1, pady=10, sticky='e')

root.mainloop()
