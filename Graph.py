class Peta:
    def __init__(self):
        self.cityList = {}

    def printPeta(self):
        for kota in self.cityList:
            print(kota + ":", self.cityList[kota])

    def tambahkanKota(self, kota):
        if kota not in self.cityList:
            self.cityList[kota] = []
            return True
        return False
    
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.cityList:
            for kotalain in self.cityList:
                if kotaDihapus in self.cityList[kotalain]:
                    self.cityList[kotalain].remove(kotaDihapus)
            del self.cityList[kotaDihapus]
            return True
        return False

    def tambahkanJalan(self, kota1, kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            self.cityList[kota2].append(kota1)
            self.cityList[kota1].append(kota2)
            return True
        return False
