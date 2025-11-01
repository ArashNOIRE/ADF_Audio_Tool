import tkinter as tk
from tkinter import filedialog, messagebox

# -------------------------------
# XOR function:
# Reads the input file byte by byte,
# XORs each byte with 0x22, and writes it to the output file.
# The operation is reversible: applying it twice restores the original file.
# -------------------------------
def xor_file(input_path, output_path):
    try:
        # Open both input and output files in binary mode
        with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
            byte = f_in.read(1)  # Read the first byte
            while byte:
                # XOR each byte with 0x22 (decimal 34) and write to output
                f_out.write(bytes([byte[0] ^ 0x22]))
                byte = f_in.read(1)  # Read next byte

        # Show success message when conversion finishes
        messagebox.showinfo("Success", f"Conversion completed successfully:\n{output_path}")

    except Exception as e:
        # Show an error message if something goes wrong (e.g., file not found, permission error)
        messagebox.showerror("Error", str(e))


# -------------------------------
# Open file dialog to select the input file (MP3 or ADF)
# -------------------------------
def select_input_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("MP3 files", "*.mp3"), ("ADF files", "*.adf")]
    )
    if file_path:
        # Clear any previous path and insert the new one into the input entry field
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)


# -------------------------------
# Open file dialog to select where to save the output file (ADF or MP3)
# -------------------------------
def select_output_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".adf",
        filetypes=[("ADF files", "*.adf"), ("MP3 files", "*.mp3")]
    )
    if file_path:
        # Clear any previous path and insert the new one into the output entry field
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)


# -------------------------------
# Convert MP3 → ADF
# Checks file extensions before running the XOR operation
# -------------------------------
def convert_mp3_to_adf():
    input_path = input_entry.get()
    output_path = output_entry.get()

    # Validate file extensions
    if not input_path.endswith(".mp3"):
        messagebox.showerror("Error", "Input file must be an MP3.")
        return
    if not output_path.endswith(".adf"):
        messagebox.showerror("Error", "Output file must be an ADF.")
        return

    # Perform the XOR conversion
    xor_file(input_path, output_path)


# -------------------------------
# Convert ADF → MP3
# Checks file extensions before running the XOR operation
# -------------------------------
def convert_adf_to_mp3():
    input_path = input_entry.get()
    output_path = output_entry.get()

    # Validate file extensions
    if not input_path.endswith(".adf"):
        messagebox.showerror("Error", "Input file must be an ADF.")
        return
    if not output_path.endswith(".mp3"):
        messagebox.showerror("Error", "Output file must be an MP3.")
        return

    # Perform the XOR conversion
    xor_file(input_path, output_path)


# -------------------------------
# GUI setup (Tkinter)
# -------------------------------

# Create main application window
root = tk.Tk()
root.title("MP3 <-> ADF Converter for GTA VC")

# --- Input file section ---
tk.Label(root, text="Input File:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)
input_btn = tk.Button(root, text="Select File", command=select_input_file)
input_btn.grid(row=0, column=2, padx=5, pady=5)

# --- Output file section ---
tk.Label(root, text="Output File:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=5, pady=5)
output_btn = tk.Button(root, text="Select Save Location", command=select_output_file)
output_btn.grid(row=1, column=2, padx=5, pady=5)

# --- Conversion buttons ---
convert_mp3_btn = tk.Button(root, text="MP3 → ADF", command=convert_mp3_to_adf)
convert_mp3_btn.grid(row=2, column=1, pady=10, sticky='w')

convert_adf_btn = tk.Button(root, text="ADF → MP3", command=convert_adf_to_mp3)
convert_adf_btn.grid(row=2, column=1, pady=10, sticky='e')

# Start the Tkinter event loop (keeps the window running)
root.mainloop()
