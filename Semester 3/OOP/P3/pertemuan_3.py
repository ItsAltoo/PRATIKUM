class User:
    def __init__(self, userName, level):
        self.__userName = ""
        self.__level = ""
        self.set_userName(userName)
        self.set_level(level)
        
    def info(self):
        print(f"UserName: {self.__userName}, Level: {self.__level}")

    def get_userName(self):
        return self.__userName
    
    def get_level(self):
        return self.__level

    def set_userName(self, newUserName):
        if len(newUserName) > 5:
            self.__userName = newUserName
            print("UserName berhasil diubah")
        else:
            print("Error: UserName harus lebih dari 5 karakter")

    def set_level(self, newLevel):
        allowed_levels = ["Admin", "Super Admin", "User"]
        if newLevel in allowed_levels:
            self.__level = newLevel
            print("Level berhasil diubah")
        else:
            print(f"Error: Level harus salah satu dari {allowed_levels}")


""" Contoh penggunaan class User """
user_1 = User("pengguna_baru", "User")
user_1.info()

print("~" * 5, "Mencoba mengubah data dengan setter", "~" * 5)
user_1.set_userName("Admin")
user_1.set_level("Moderator")
user_1.info()

print("~" * 5, "Mencoba mengubah data dengan setter yang benar", "~" * 5)
user_1.set_userName("pengguna_baru_admin")
user_1.set_level("Admin")
user_1.info()
