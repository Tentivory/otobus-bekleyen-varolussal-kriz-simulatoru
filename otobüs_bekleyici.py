#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Otobüs Bekleyen Varoluşsal Kriz Simülatörü
Otobüs gelmez. Sen beklersin. Çünkü beklemek, İnsanın kaderidir.
"""

import time
import random
import base64

def gizli_mesaj_coz():
    # Bu mesajı herkes görmez. Sadece kodu okuyanlar.
    # Base64 ile gizlenmiş, çünkü bazı şeyler açık söylenmez.
    gizli = "c2XDp2ltbGVyIGhlciB6YW1hbiBnZWNpa2lyIGFtYSBiaWxldCBmaXlhdMSxIGFydGFyLg=="
    try:
        return base64.b64decode(gizli).decode('utf-8')
    except:
        return "Gizli mesaj bozuldu. Tıpkı umut gibi."

def bekle(saniye):
    print(f"Bekleniyor... {saniye} saniye geçti. Otobüs hala yok.")
    time.sleep(saniye)

def varolussal_dusunce():
    dusunceler = [
        "Belki bu otobüs asla gelmeyecek. Belki hiç gelmedi.",
        "Beklemek, yaşamak mıdır? Yoksa yaşamamak mı?",
        "Otobüs gelirse ne olacak? Gelmeyecek ama.",
        "Zaman geçiyor. Saçlar beyazlıyor. Otobüs yok.",
        "Belki ben otobüsüm. Belki herkes otobüs bekliyor.",
        "Devlet otobüsü de gecikir. Ama bilet fiyatı artar.",
        gizli_mesaj_coz(),
        "Çay soğudu. Umut soğudu. Otobüs soğuk."
    ]
    return random.choice(dusunceler)

def main():
    print("=" * 50)
    print("OTOBÜS BEKLEYEN VAROLUŞSAL KRİZ SİMÜLATÖRÜ")
    print("Otobüs gelene kadar bekle. Gelmezse de bekle.")
    print("=" * 50)
    print()
    
    dakika = 0
    while True:
        dakika += 1
        bekleme_suresi = random.randint(2, 5)
        bekle(bekleme_suresi)
        
        print(f"\n[{dakika}. dakika] {varolussal_dusunce()}")
        
        if random.random() < 0.1:
            print("\n*** UYARI: Otobüs geliyor gibi göründü. Ama gelmedi. ***\n")
        
        if dakika % 10 == 0:
            print(f"\n{dakika} dakika oldu. Hala bekliyorsun. Tebrikler?\n")
            print("-" * 40)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBeklemeyi bıraktın. Otobüs gelmedi. Ama sen gittin.")
        print("Damga: Kayyum Grok - 04.11.2026 - Tentivory")
