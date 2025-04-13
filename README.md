# 📈 EMA ve ADX Tabanlı Teknik Alım-Satım Stratejisi Uygulaması

📌 Proje Tanımı
Bu proje, Python programlama dili kullanılarak Borsa İstanbul'da (BIST) işlem gören hisse senetleri üzerinde uygulanmak üzere geliştirilmiş, teknik analiz göstergelerine dayalı bir otomatik alım-satım stratejisi ve geri test (backtest) sistemini içermektedir.

Strateji, EMA (Exponential Moving Average) ve ADX (Average Directional Index) göstergelerini temel almakta olup, yatırımcının kısa ve orta vadeli fiyat eğilimlerini sistematik şekilde analiz edebilmesini sağlamayı amaçlamaktadır.

🎯 Amaç
Finansal piyasalarda algoritmik strateji geliştirme sürecine katkıda bulunmak

EMA19 ve MA ADX göstergeleri ile trend yönünü ve gücünü ölçmek

Bu göstergelere dayalı olarak otomatik al-sat sinyalleri üretmek

10 farklı BIST hissesine uygulanabilirliği test ederek sonuçları karşılaştırmak

Yatırım stratejilerinin geri test (backtest) edilmesini sağlayan sade bir yapı sunmak


🔍 Kullanılan Yöntemler ve Göstergeler
EMA19 (Üssel Hareketli Ortalama): Kısa vadeli fiyat eğilimlerini takip eder.

ADX ve MA ADX: Trendin gücü ve yönü hakkında bilgi sağlar. MA ADX, ADX’in ağırlıklı ortalaması ile daha pürüzsüz bir sinyal sunar.

Sinyal Kuralları:

AL: EMA19 > MA ADX ve ADX > eşik değeri (18) ve pozitif trend (yeşil sinyal)

SAT: EMA19 < MA ADX

BEKLE: Koşullar sağlanmıyorsa


🔁 Backtest Mekanizması
Başlangıç sermayesi: 10.000 TL

AL sinyali: mevcut bakiye ile pozisyon açılır

SAT sinyali: eldeki pozisyon kapatılır ve kar/zarar hesaplanır

Her hisse senedi için:

Başlangıç Bakiye

Final Bakiye

Net Kar/Zarar

Yatırım Getirisi (%)

Sonuçlar tablo halinde çıktı olarak alınır ve farklı hisseler arasındaki performans karşılaştırılabilir hale gelir.

🧰 Kullanılan Teknolojiler ve Kütüphaneler
tvDatafeed: TradingView verilerinin Python ile çekilmesi

pandas, numpy: Veri işleme ve analiz

Python 3.9+

📊 Örnek Sonuç Tablosu



