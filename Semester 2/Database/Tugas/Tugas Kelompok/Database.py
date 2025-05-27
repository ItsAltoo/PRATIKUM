import sqlite3
import os

# Menghapus database jika sudah ada,agar tidak terjadi error saat insert data
if os.path.exists("data.db"):
    os.remove("data.db")


con = sqlite3.connect("data.db")
cur = con.cursor()

cur.execute(
    """ 
create table if not exists barang (
    kode_barang text primary key,
    nama_barang text ,
    harga integer
);
"""
)

cur.execute(
    """ 
create table if not exists transaksi (
    kode_faktur text primary key,
    tanggal date
);
"""
)

cur.execute(
    """ 
create table if not exists detail_barang (
    kode_faktur text,
    kode_barang text,
    jumlah integer,
    primary key (kode_faktur, kode_barang),
    foreign key (kode_faktur) references transaksi(kode_faktur),
    foreign key (kode_barang) references barang(kode_barang)
);
"""
)

cur.execute(
    """ 
insert into barang values 
('BRG-001','BATU BATA',900),
('BRG-002','SEMEN',60000),
('BRG-003','PIPA',11000),
('BRG-004','KAYU',90000),
('BRG-005','BESI',58000),
('BRG-006','BETON',720000),
('BRG-007','CAT DINDING',260000)
"""
)

cur.execute(
    """
insert into transaksi values 
('KP-001','2023-10-01'),
('KP-002','2023-10-02'),
('KP-003','2023-10-03')
"""
)

cur.execute(
    """
insert into detail_barang values 
('KP-001','BRG-001',4200),
('KP-001','BRG-002',310),
('KP-001','BRG-003',18),
('KP-001','BRG-004',80),
('KP-002','BRG-005',190),
('KP-002','BRG-006',10),
('KP-003','BRG-007',5)
"""
)

cur.execute(
    """
SELECT f.kode_faktur, f.tanggal, b.nama_barang, d.jumlah, b.harga
FROM detail_barang d
JOIN transaksi f ON d.kode_faktur = f.kode_faktur
JOIN barang b ON d.kode_barang = b.kode_barang
"""
)

for row in cur.fetchall():
    print(row)


con.commit()
con.close()

# Mengapa data tidak bisa ditampilkan 2 kali?
# Karena saat code dieksekusi insert data ke dalam tabel tidak bisa dilakukan karena adanya primary key
