from globals import *
import sys

class Calculator:
    def __init__(self, angka1 = nil1, angka2=nil2):
        self.angka1 = angka1
        self.angka2 = angka2
    def add(self):
        return self.angka1 + self.angka2

    def substract(self):
        return self.angka1 - self.angka2

    def multiply(self):
        return self.angka1 * self.angka2

    def divide(self):
        if self.angka2 == 0:
            return sys.exit(1)
        return self.angka1 / self.angka2

    def result(self):
        func = [
          (self.add(), 'Penjumlahan'),
          (self.substract(), 'Pengurangan'), 
          (self.multiply(), 'Perkalian'),
          (self.divide(), 'Pembagian')
        ]
        hasil = []
        for fun, desc in func:
            hasil.append("Hasil dari {} {} dan {} = {}".format(desc, self.angka1, self.angka2, fun))
        return hasil

