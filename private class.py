class Baju():
    __JumlahBaju = 2 # private
 
    def _init_(self, NamaBaju):
        self.nama = NamaBaju
 
    def hargaBaju(self, HargaBaju):
       hasil = self.__JumlahBaju* HargaBaju
       return hasil
 
cantik = Baju("Gamis")
print(cantik.hargaBaju(100000))
print(cantik.__JumlahBaju)