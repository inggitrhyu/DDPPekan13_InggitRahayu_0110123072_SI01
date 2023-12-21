class Animal:
    def __init__(self, name, makanan, hidup, kembangBiak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.kembangBiak = kembangBiak

    def cetak(self):
        print(
            "\nNama:", self.name,
            "\nMakanan:", self.makanan,
            "\nHidup:", self.hidup,
            "\nKembangBiak:", self.kembangBiak
        )


class Badak(Animal):
    def __init__(self, name, makanan, hidup, kembangBiak, jenis, jenisKelamin):
        super().__init__(name, makanan, hidup, kembangBiak)
        self.jenis = jenis
        self.jenisKelamin = jenisKelamin

    def cetak(self):
        super().cetak()
        print(
            "\nJenis:", self.jenis,
            "\nJenisKelamin:", self.jenisKelamin,              
        )

class Ikan(Animal):
    def __init__(self, name, makanan, hidup, kembangBiak, bernapas, jenis):
        super().__init__(name, makanan, hidup, kembangBiak)
        self.bernapas = bernapas
        self.jenis = jenis

    def cetak(self):
        super().cetak()
        print(
            "\nBernapas:", self.bernapas,
            "\nJenis:", self.jenis, 
        )


class Ular(Animal):
    def __init__(self, name, makanan, hidup, kembangBiak, bergerak, bertaring):
        super().__init__(name, makanan, hidup, kembangBiak)
        self.bergerak = bergerak
        self.bertaring = bertaring

    def cetak(self):
        super().cetak()
        print(
            "\nBergerak:", self.bergerak,
            "\nBertaring:", self.bertaring,
           
        )


badak = Badak("Badak", "Rumput", "Daratan", "Melahirkan", "Badak Jawa", "Betina")
ikan = Ikan("Ikan", "Cacing", "Air", "Bertelur", "Insang", "Mas")
ular = Ular("Ular", "Mamalia", "Semua Habitat", "Bertelur", "1,6 km per jam", "Iya")

badak.cetak()
ikan.cetak()
ular.cetak()