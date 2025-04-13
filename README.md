# 📈 Python ile Teknik Göstergelere Dayalı Algoritmik Yatırım Stratejisi ve Performans Analizi

## ⚠️ Yasal Uyarı ve Bilgilendirme
Bu çalışma, yalnızca teknik analiz göstergelerine dayalı algoritmik stratejilerin Python diliyle modellenmesini ve tarihsel veriler üzerinden test edilmesini amaçlamaktadır. Burada sunulan içerikler, hiçbir şekilde yatırım tavsiyesi niteliği taşımamaktadır. Yatırım kararlarınızı verirken, makroekonomik koşullar, şirket temelleri, sektörel dinamikler ve kişisel risk profiliniz gibi çok yönlü faktörleri dikkate almanız önem arz etmektedir.

Borsa; bilgi, analiz ve strateji gerektiren, risk içeren bir yatırım ortamıdır. Şansa dayalı bir oyun veya kısa vadeli kazanç hedefiyle yaklaşmak, maddi kayıplara yol açabilir. Lütfen yatırım yaparken bilinçli, araştırmacı ve sorumlu bir yaklaşım benimseyiniz.

## 🙏 Teşekkür ve Kaynak

Bu projede kullanılan MA ADX göstergesi, TradingView platformunda capnOscar kullanıcı adıyla paylaşılan özel bir Pine Script indikatörüne dayanmaktadır.capnOscar’a bu katkısı için teşekkür ederim
İlgili gösterge, geleneksel ADX hesaplamasına ağırlıklı ortalama (WMA) entegrasyonu ile daha rafine bir trend gücü sinyali sunmaktadır.
Bu çalışmada, söz konusu gösterge Python diline çevrilmiş; ardından EMA19 göstergesiyle birlikte değerlendirilerek özgün bir al-sat stratejisi ve backtest sistemi geliştirilmiştir.


## 📌 Proje Tanımı
Bu proje, Python programlama dili kullanılarak Borsa İstanbul'da (BIST) işlem gören hisse senetleri üzerinde uygulanmak üzere geliştirilmiş, teknik analiz göstergelerine dayalı bir otomatik alım-satım stratejisi ve geri test (backtest) sistemini içermektedir.

Strateji, EMA (Exponential Moving Average) ve ADX (Average Directional Index) göstergelerini temel almakta olup, yatırımcının kısa ve orta vadeli fiyat eğilimlerini sistematik şekilde analiz edebilmesini sağlamayı amaçlamaktadır.

## 🎯 Amaç

>- Finansal piyasalarda algoritmik strateji geliştirme sürecine katkıda bulunmak
>- EMA19 ve MA ADX göstergeleri ile trend yönünü ve gücünü ölçmek
>- Bu göstergelere dayalı olarak otomatik al-sat sinyalleri üretmek
>- 20 farklı BIST hissesine uygulanabilirliği test ederek sonuçları karşılaştırmak
>-Yatırım stratejilerinin geri test (backtest) edilmesini sağlayan sade bir yapı sunmak

## 🔍 Kullanılan Yöntemler ve Göstergeler
>- EMA19 (Üssel Hareketli Ortalama): Kısa vadeli fiyat eğilimlerini takip eder.
>- ADX ve MA ADX: Trendin gücü ve yönü hakkında bilgi sağlar. MA ADX, ADX’in ağırlıklı ortalaması ile daha pürüzsüz bir sinyal sunar.
##### Sinyal Kuralları:

>- AL: EMA19 > MA ADX ve ADX > eşik değeri (18) ve pozitif trend (yeşil sinyal)
>- SAT: EMA19 < MA ADX
>- BEKLE: Koşullar sağlanmıyorsa


## 🔁 Backtest Mekanizması

Başlangıç sermayesi: 10.000 TL
>- AL sinyali: mevcut bakiye ile pozisyon açılır
>- SAT sinyali: eldeki pozisyon kapatılır ve kar/zarar hesaplanır


## 🧰 Kullanılan Teknolojiler ve Kütüphaneler

>- tvDatafeed: TradingView verilerinin Python ile çekilmesi
>- pandas, numpy: Veri işleme ve analiz
>- Python 3.9+

## 📊 Örnek Sonuç Tablosu

###### Strateji kapsamında yapılan tüm alım-satım işlemleri kümülatif olarak değerlendirilmiştir. Başlangıç sermayesi 10.000 TL olup, her işlem sonucunda oluşan yeni bakiye, bir sonraki işlemin sermayesi olarak kullanılmıştır. Dolayısıyla, alım işlemlerinde bakiye her seferinde yeniden 10.000 TL’ye sabitlenmemekte; önceki işlemlerin kar/zarar durumu doğrudan sonraki işlemlere yansıtılmaktadır.”


###### Test edilen senaryoya göre son 2 yıllık getiriler - hisseler rastgele seçilmiştir


|Hisse|Başlangıç Bakiye|Final Bakiye|Net Kar /Zarar|Yatırım Getiris(%)|
|:---|:---:|---:|---:|---:|
|TAVHL|10000|33722.72|23722.72|237.23|
|FROTO|10000|15948.43|5948.43|59.48|
|AKSA|10000|13833.42|3833.42|38.33|
|TUPRS|10000|22138.14|12138.14|121.38|
|YEOTK|10000|18281.05|8281.05|82.81|
|MIATK|10000|59657.55|49657.55|496.58|
|BIMAS|10000|18634.78|8634.78|86.35|
|MGROS|10000|25688.99|15688.99|156.89|
|NUHCM|10000|21475.03|11475.03|114.75|
|GOLTS|10000|30719.45|20719.45|207.19|
|BANVT|10000|23777.55|13777.55|137.78|
|GRSEL|10000|79563.48|69563.48|695.63|
|DOAS|10000|20007.75|10007.75|100.08|
|ASTOR|10000|28092.63|18092.63|180.93|
|ANSGR|10000|29411.39|19411.39|194.11|
|TCELL|10000|23046.99|13046.99|130.47|
|AYGAZ|10000|20215.66|10215.66|102.16|
|KCHOL|10000|12595.45|2595.45|25.95|
|MPARK|10000|31446.98|21446.98|214.47|
|GARAN|10000|16290.62|6290.62|62.91|
|ISCTR|10000|9785.66|-214.34|-2.14|













