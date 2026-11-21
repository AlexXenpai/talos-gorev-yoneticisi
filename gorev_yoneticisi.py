# TALOS 1. Hafta Mini Python Projesi: Görev Yönetim Sistemi (To-Do List)
# Hazırlayan: Ali İhsan Dağaşan | Mimari: 2 Sınıf (Gorev, GorevYoneticisi) ve 5 Fonksiyon

GECERLI_ONCELIKLER = ("Düşük", "Normal", "Yüksek")  # Değiştirilemez (tuple) öncelik seviyeleri

class Gorev:
    # 1. Sınıf: Tek bir görevin özelliklerini (attribute) ve durum metotlarını tutar
    def __init__(self, gorev_id, baslik, oncelik, tahmini_saat):
        self.id, self.baslik = int(gorev_id), str(baslik)
        self.oncelik, self.tahmini_saat = str(oncelik), float(tahmini_saat)
        self.tamamlandi = False                  # bool: Görevin tamamlanma durumu

    def durum_degistir(self, yeni_baslik=""):
        self.tamamlandi = not self.tamamlandi    # Mantıksal not operatörü ile durumu çevir
        if yeni_baslik != "":
            self.baslik = yeni_baslik
    def bilgi_satiri(self):
        durum = "TAMAMLANDI" if self.tamamlandi else "BEKLİYOR"
        return f"#{self.id} [{durum}] {self.baslik} | Öncelik: {self.oncelik} ({self.tahmini_saat} saat)"

class GorevYoneticisi:
    # 2. Sınıf: Görev nesnelerini liste (list), sözlük (dict) ve küme (set) ile yönetir
    def __init__(self, proje_adi):
        self.proje_adi = proje_adi
        self.gorevler, self.oncelik_kumesi, self.sayac = [], set(), 1
    def gorev_bul(self, aranan_id):
        for gorev in self.gorevler:
            if gorev.id == aranan_id:
                return gorev
        return None
    def istatistik_hesapla(self):
        toplam = len(self.gorevler)
        biten = sum(1 for g in self.gorevler if g.tamamlandi)
        sure = sum(g.tahmini_saat for g in self.gorevler)
        oran = round((biten / toplam) * 100, 1) if toplam > 0 else 0.0
        return {"toplam": toplam, "biten": biten, "kalan": toplam - biten, "sure": sure, "oran": oran}

def girdi_dogrula(baslik, oncelik, saat_metni):
    # 1. Fonksiyon (Doğrulama): Başlık, öncelik ve süre girdilerini koşullarla doğrular
    if baslik.strip() == "" or oncelik not in GECERLI_ONCELIKLER:
        return False, "Hata: Başlık boş olamaz ve öncelik (Düşük/Normal/Yüksek) olmalıdır!"
    if not saat_metni.replace(".", "", 1).isdigit():
        return False, "Hata: Süre alanına pozitif bir sayı (int/float) girilmelidir!"
    saat = float(saat_metni)
    return (True, saat) if 0 < saat <= 100 else (False, "Hata: Süre 0-100 saat arasında olmalıdır!")

def gorev_ekle(yonetici, baslik, oncelik, saat_metni):
    # 2. Fonksiyon (Veri Ekleme): Doğrulanan verilerle yeni Gorev nesnesi oluşturup listeye ekler
    gecerli, sonuc = girdi_dogrula(baslik, oncelik, saat_metni)
    if not gecerli:
        return sonuc
    yeni = Gorev(yonetici.sayac, baslik.strip(), oncelik, sonuc)
    yonetici.gorevler.append(yeni)
    yonetici.oncelik_kumesi.add(oncelik)
    yonetici.sayac += 1
    return f"Eklendi: #{yeni.id} '{yeni.baslik}' (Nesne tipi: {type(yeni).__name__})"

def gorev_guncelle(yonetici, gorev_id, yeni_baslik=""):
    # 3. Fonksiyon (Veri Güncelleme): Görevin tamamlanma durumunu ve başlığını günceller
    hedef = yonetici.gorev_bul(gorev_id)
    if hedef is None:
        return f"Uyarı: #{gorev_id} numaralı görev bulunamadı!"
    hedef.durum_degistir(yeni_baslik.strip())
    return f"Güncellendi: {hedef.bilgi_satiri()}"

def gorev_sil(yonetici, gorev_id):
    # 4. Fonksiyon (Veri Silme): Belirtilen ID'ye sahip görevi listeden siler
    hedef = yonetici.gorev_bul(gorev_id)
    if hedef is not None:
        yonetici.gorevler.remove(hedef)
        return f"Silindi: #{gorev_id} - '{hedef.baslik}' listeden kaldırıldı."
    return f"Hata: Silinecek #{gorev_id} numaralı görev mevcut değil!"

def gorevleri_goruntule(yonetici):
    # 5. Fonksiyon (Veri Görüntüleme): Görev listesini ve özet istatistikleri ekrana yazdırır
    ozet = yonetici.istatistik_hesapla()
    print(f"\n=== {yonetici.proje_adi} | Aktif Öncelikler: {yonetici.oncelik_kumesi} ===")
    for g in yonetici.gorevler:
        print(" ", g.bilgi_satiri())
    print(f"Özet -> Toplam: {ozet['toplam']} | Biten: {ozet['biten']} (%{ozet['oran']}) | Süre: {ozet['sure']} saat")

if __name__ == "__main__":
    sistem = GorevYoneticisi("Görev Yönetim Sistemi (To-Do List)")
    gorev_ekle(sistem, "Kamera şerit takip algoritması testi", "Yüksek", "4.5")
    gorev_ekle(sistem, "ROS 2 düğüm haberleşme kontrolü", "Normal", "2.0")
    while True:
        secim = input("\n[1]Listele [2]Ekle [3]Güncelle [4]Sil [0]Çıkış -> Seçiminiz: ").strip()
        if secim == "0":
            print("Sistemden güvenli çıkış yapıldı.")
            break
        elif secim == "1":
            gorevleri_goruntule(sistem)
        elif secim == "2":
            print(gorev_ekle(sistem, input("Başlık: "), input("Öncelik (Düşük/Normal/Yüksek): "), input("Süre: ")))
        elif secim in ("3", "4") and secim.isdigit():
            gid = int(input("Görev ID: "))
            print(gorev_guncelle(sistem, gid, input("Yeni başlık (boş=aynı): ")) if secim == "3" else gorev_sil(sistem, gid))
        else:
            continue
