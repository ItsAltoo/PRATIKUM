class Notifikasi:
    def kirim(self):
        raise NotImplementedError


class Email(Notifikasi):
    def kirim(self, pesan):
        return f"[Email] Mengirim : {pesan}"


class SMS(Notifikasi):
    def kirim(self, pesan):
        return f"[SMS] Mengirim : {pesan}"


class PushNotification(Notifikasi):
    def kirim(self, pesan):
        return f"[Push Notification] Mengirim : {pesan}"


daftar_pesan = [Email(), SMS(), PushNotification()]
pesan = "Diskon spesial! hanya untuk Anda."

for i in daftar_pesan:
    print(i.kirim(pesan))
