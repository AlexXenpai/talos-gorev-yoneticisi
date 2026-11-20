# AGENTS.md — TALOS Otonom Araç Takımı Antigravity Ajan Kuralları

Bu dosya, **Google Antigravity (AGY)** ve **Antigravity IDE** ajanlarının bu çalışma alanında (workspace) kod yazarken ve görev yürütürken uyması gereken temel kuralları tanımlar.

## 1. Python Kodlama Standartları
- Tüm Python kodları **PEP 8** standartlarına uygun olmalıdır (`snake_case` fonksiyon/değişken adları, `PascalCase` sınıf adları).
- Kodlarda gereksiz tekrardan kaçınılmalı (DRY prensibi), modüler fonksiyonlar (`def`) ve nesne yönelimli programlama (`class`, `__init__`, `self`) kullanılmalıdır.
- 1. Hafta mini proje kodları **50–100 satır arası**, en az **2 class** ve en az **4 fonksiyon (`def`)** içerecek şekilde tasarlanmalıdır.

## 2. Dokümantasyon ve Akış Şeması Kuralları
- Tüm notlar `.md` (Markdown) formatında, anlaşılır açıklamalar ve çalışır örneklerle yazılmalıdır.
- Projelerin `README.md` dosyasında mutlaka **Giriş → İşlem → Çıkış** mantığında ilerleyen bir **Akış Şeması (Flowchart)** ve kodun mantığını açıklayan bölüm yer almalıdır.
