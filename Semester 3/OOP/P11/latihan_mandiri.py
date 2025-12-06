from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


# Data Mahasiswa Dummy
@dataclass
class Mahasiswa:
    nama: str
    sks_diambil: int
    ipk: float
    prasyarat_lulus: bool
    jadwal_aman: bool


# ==========================================
# 2. IMPLEMENTASI DIP/OCP (Interface)
# ==========================================
class IValidationRule(ABC):
    """
    Kontrak: Semua aturan validasi harus punya method 'validate'.
    Return True jika lolos, False jika gagal.
    """

    @abstractmethod
    def validate(self, mhs: Mahasiswa) -> bool:
        pass


# ==========================================
# 2. IMPLEMENTASI KELAS KONKRIT
# ==========================================
class SksLimitRule(IValidationRule):
    def validate(self, mhs: Mahasiswa) -> bool:
        maks_sks = 24 if mhs.ipk >= 3.0 else 20
        if mhs.sks_diambil > maks_sks:
            print(
                f"[GAGAL] {mhs.nama} mengambil {mhs.sks_diambil} SKS (Maks: {maks_sks})."
            )
            return False
        print(f"[OK] SKS {mhs.nama} aman.")
        return True


class PrerequisiteRule(IValidationRule):
    def validate(self, mhs: Mahasiswa) -> bool:
        if not mhs.prasyarat_lulus:
            print(f"[GAGAL] {mhs.nama} belum lulus mata kuliah prasyarat.")
            return False
        print(f"[OK] Prasyarat {mhs.nama} terpenuhi.")
        return True


# ==========================================
# 4. CHALLENGE (PEMBUKTIAN OCP)
# ==========================================
# Kita buat aturan baru TANPA mengubah RegistrationService sama sekali.
class JadwalBentrokRule(IValidationRule):
    def validate(self, mhs: Mahasiswa) -> bool:
        if not mhs.jadwal_aman:
            print(f"[GAGAL] Jadwal {mhs.nama} ada yang bentrok!")
            return False
        print(f"[OK] Jadwal {mhs.nama} aman.")
        return True


# ==========================================
# 3. IMPLEMENTASI SRP (RegistrationService)
# ==========================================
class RegistrationService:
    # Menerima DAFTAR aturan (List), bukan cuma satu.
    # Ini menerapkan Dependency Injection.
    def __init__(self, rules: List[IValidationRule]):
        self.rules = rules

    def register_student(self, mhs: Mahasiswa):
        print(f"\n--- Memulai Validasi untuk {mhs.nama} ---")

        # Logika Koordinator: Jalankan SEMUA aturan yang disuntikkan
        for rule in self.rules:
            is_valid = rule.validate(mhs)
            if not is_valid:
                print(">> Registrasi Ditolak.")
                return False

        print(">> Registrasi Berhasil Disetujui!")
        return True


# ==========================================
# PROGRAM UTAMA (Main)
# ==========================================

# 1. Setup Data
mhs_budi = Mahasiswa(
    "Budi", sks_diambil=22, ipk=3.5, prasyarat_lulus=True, jadwal_aman=False
)

# 2. Konfigurasi Rules (Kita bisa pasang copot aturan di sini)
#    Kita masukkan Challenge (JadwalBentrokRule) ke dalam list ini.
daftar_aturan = [
    SksLimitRule(),
    PrerequisiteRule(),
    JadwalBentrokRule(),  # <-- Bukti OCP: Fitur baru masuk sebagai plugin
]

# 3. Inject ke Service
service = RegistrationService(rules=daftar_aturan)

# 4. Eksekusi
service.register_student(mhs_budi)
