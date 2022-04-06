#Class
class Mahasiswa:
    
    jumlah_mahasiswa = 0 #Variable
    
    def _init_(self, inputNama, inputNim):
        self.nama = inputNama
        self.nim = inputNim
        Mahasiswa.jumlah_mahasiswa += 1
        
Umi = Mahasiswa("Umi","D0219022")
Umi Qalsum = Mahasiswa("Umi Qalsum","D0219022")

print(Mahasiswa.jumlah_mahasiswa)