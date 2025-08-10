import tkinter as tk
from tkinter import filedialog, messagebox

def xor_file(input_path, output_path):
    try:
        with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
            byte = f_in.read(1)
            while byte:
                f_out.write(bytes([byte[0] ^ 0x22]))
                byte = f_in.read(1)
        messagebox.showinfo("موفقیت", f"تبدیل با موفقیت انجام شد:\n{output_path}")
    except Exception as e:
        messagebox.showerror("خطا", str(e))

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
        messagebox.showerror("خطا", "فایل ورودی باید mp3 باشد.")
        return
    if not output_path.endswith(".adf"):
        messagebox.showerror("خطا", "فایل خروجی باید adf باشد.")
        return
    xor_file(input_path, output_path)

def convert_adf_to_mp3():
    input_path = input_entry.get()
    output_path = output_entry.get()
    if not input_path.endswith(".adf"):
        messagebox.showerror("خطا", "فایل ورودی باید adf باشد.")
        return
    if not output_path.endswith(".mp3"):
        messagebox.showerror("خطا", "فایل خروجی باید mp3 باشد.")
        return
    xor_file(input_path, output_path)

# ساخت پنجره اصلی
root = tk.Tk()
root.title("تبدیل MP3 <-> ADF برای GTA VC")

# فیلد انتخاب فایل ورودی
tk.Label(root, text="فایل ورودی:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)
input_btn = tk.Button(root, text="انتخاب فایل", command=select_input_file)
input_btn.grid(row=0, column=2, padx=5, pady=5)

# فیلد انتخاب فایل خروجی
tk.Label(root, text="فایل خروجی:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=5, pady=5)
output_btn = tk.Button(root, text="انتخاب محل ذخیره", command=select_output_file)
output_btn.grid(row=1, column=2, padx=5, pady=5)

# دکمه‌ها برای تبدیل
convert_mp3_btn = tk.Button(root, text="MP3 → ADF", command=convert_mp3_to_adf)
convert_mp3_btn.grid(row=2, column=1, pady=10, sticky='w')

convert_adf_btn = tk.Button(root, text="ADF → MP3", command=convert_adf_to_mp3)
convert_adf_btn.grid(row=2, column=1, pady=10, sticky='e')

root.mainloop()
