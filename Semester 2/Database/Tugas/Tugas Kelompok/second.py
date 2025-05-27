import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Koneksi ke database
conn = sqlite3.connect("data.db")
cur = conn.cursor()

# Fungsi untuk menampilkan data barang di tabel GUI
def tampilkan_barang():
    for row in tree.get_children():
        tree.delete(row)
    cur.execute("SELECT * FROM barang")
    for barang in cur.fetchall():
        tree.insert('', 'end', values=barang)

# Fungsi untuk menambahkan barang baru
def tambah_barang():
    kode = entry_kode.get()
    nama = entry_nama.get()
    harga = entry_harga.get()

    if not (kode and nama and harga):
        messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")
        return

    try:
        cur.execute("INSERT INTO barang VALUES (?, ?, ?)", (kode, nama, int(harga)))
        conn.commit()
        messagebox.showinfo("Sukses", "Data barang berhasil ditambahkan.")
        tampilkan_barang()
        entry_kode.delete(0, tk.END)
        entry_nama.delete(0, tk.END)
        entry_harga.delete(0, tk.END)
    except sqlite3.IntegrityError:
        messagebox.showerror("Gagal", "Kode barang sudah ada!")

# GUI Setup
root = tk.Tk()
root.title("Aplikasi Barang")
root.geometry("500x400")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Kode Barang").grid(row=0, column=0)
tk.Label(frame_input, text="Nama Barang").grid(row=1, column=0)
tk.Label(frame_input, text="Harga").grid(row=2, column=0)

entry_kode = tk.Entry(frame_input)
entry_nama = tk.Entry(frame_input)
entry_harga = tk.Entry(frame_input)

entry_kode.grid(row=0, column=1)
entry_nama.grid(row=1, column=1)
entry_harga.grid(row=2, column=1)

btn_tambah = tk.Button(frame_input, text="Tambah Barang", command=tambah_barang)
btn_tambah.grid(row=3, columnspan=2, pady=5)

frame_tree = tk.Frame(root)
frame_tree.pack(pady=10)

tree = ttk.Treeview(frame_tree, columns=("Kode", "Nama", "Harga"), show="headings")
tree.heading("Kode", text="Kode")
tree.heading("Nama", text="Nama")
tree.heading("Harga", text="Harga")
tree.pack()

tampilkan_barang()
root.mainloop()
