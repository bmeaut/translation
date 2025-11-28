# Fordítás Word-dokumentumokhoz – formázásmegőrzéssel

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![DocuTranslate](https://img.shields.io/badge/Uses-DocuTranslate-0A84FF)](https://github.com/xunbu/docutranslate)
[![Status](https://img.shields.io/badge/Status-Alpha-orange)](#)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-informational)](#)

Kapcsolat: [Kővári Bence](mailto:kovari.bence@vik.bme.hu)

---
## Összefoglaló

Az útmutató lépésről lépésre bemutatja, hogyan lehet Word-dokumentumokat automatizáltan idegen nyelvre fordítani a formátum megőrzésével.

A fordítás a nyílt forráskódú [DocuTranslate](https://github.com/xunbu/docutranslate) eszközzel és egy tetszőlegesen választott MI modellel történik (pl. OpenAI „gpt-5.1” ). A cél a minél pontosabb, mégis gyors első változat elkészítése; a végső szöveg minősége érdekében az emberi átolvasás továbbra is szükséges.

> Megjegyzés: Egyetemi anyagok esetében a szakterminológia következetessége kiemelten fontos, ezért elengedhetetlen a saját szótár (glossary) használata.

---

## Nehézségek és korlátok

- Jelenleg nincs egyetemi/kari szinten elfogadott szótár a szakkifejezésekre, bizottságok neveire stb. Ha elérhető hivatalos lista, az útmutatót frissítjük.
- Nincs egységes iránymutatás a brit vs. amerikai angol használatára. A mellékelt szótár egy régi [minisztériumi lista](https://www.nefmi.gov.hu/felsooktatas/dokumentumok/felsooktatasban-gyak...) alapján készült kiindulópontként.

---

## Gyors kezdés

1) Telepítsd a Python-t: [python.org/downloads](https://www.python.org/downloads/)  
2) Szerezz API kulcsot a választott szolgáltatótól (pl. [OpenAI](https://platform.openai.com/api-keys), [Gemini](https://aistudio.google.com/u/0/apikey)).  
3) (Opcionális) Egészítsd ki a szótárat: [glossary.xlsx](https://github.com/bmeaut/translation/raw/refs/heads/master/glossary.xlsx).  
4) Szerkeszd a beállításokat a [translate.py](https://raw.githubusercontent.com/bmeaut/translation/refs/heads/master/translate.py) fájlban (API kulcs, modell, bemeneti/kimeneti fájlok).  
5) Futtasd a fordítást:
   ```
   python translate.py
   ```

---

## Előkészítés

### Python környezet

Telepítő letöltése, futtatása: [python.org](https://www.python.org/downloads/)

### Fordítóprogram

A nyílt forráskódú [DocuTranslate]([https://github.com/xunbu/docutranslate](https://github.com/xunbu/docutranslate?tab=readme-ov-file#installation)) szoftvert használjuk. A projekt háromféle telepítési lehetőséget ajánl, [részletek a hivatalos oldalon találhatók](https://github.com/xunbu/docutranslate?tab=readme-ov-file#installation).

### API kulcs

A fordításhoz több különböző nagy nyelvi modell szolgáltatás használható. Érdemes a megbízható és fejlett szolgáltatókat választani, például:
- [OpenAI API](https://platform.openai.com/api-keys)
- [Google Gemini](https://aistudio.google.com/u/0/apikey)

> Figyelem: Az API kulcsot soha ne oszd meg, és ne töltsd fel verziókezelőbe!

---

## Szótár (glossary) összeállítása

Bár a nyelvi modellek jók az általános fordításban, a rögzített fordítású kifejezéseket (intézménynevek, szabályzatok, tanszékek, bizottságok, szervezeti egységek) célszerű szótárban meghatározni.

Javaslat:
- Nézd át a fordítandó anyagot, és gyűjtsd ki a problémás kifejezéseket.
- Alternatívaként készíts egy első gépi fordítást, majd az angol változatot átnézve gyűjtsd össze a javítandó terminusokat.

A rendszer JSON formátumú szótárt vár, a szerkesztést pedig megkönnyíti a mellékelt minta Excel: [glossary.xlsx](https://github.com/bmeaut/translation/raw/refs/heads/master/glossary.xlsx)

Egyszerű JSON minta:
```json
{
   "Tanulmányi és Vizsgaszabályzat": "Academic and Examination Regulations",
   "Hallgatói Önkormányzat": "Student Union"
}
```

> Tipp: Az utolsó tag után nincs vessző

---

## Fordítás előkészítése

A fordítást a [translate.py](https://raw.githubusercontent.com/bmeaut/translation/refs/heads/master/translate.py) futtatásával végezzük. Futtatás előtt szerkeszd a fájlban található beállításokat:

- `api_key`: a szolgáltatótól kapott API kulcs
- `model_id`: csak akkor módosítsd, ha nem az alapértelmezett modellt használod (példa: OpenAI „gpt-5.1”)
- `uzinfo_mini.docx`: a forrásfájl (megadható teljes elérési úttal is)
- `translated_uzinfo_mini.docx`: a célfájl neve (automatikusan egy `Output` mappába kerül). A név térjen el az eredetitől.

> Tipp: A kimeneti fájlnevet mindig változtasd meg, így nem írja felül a forrást.

---

## Fordítás futtatása

A fordítást a következő paranccsal kezdeményezheted:
```
python translate.py
```

- A futás során előfordulhat kínai nyelvű napló/üzenet – ez normális, a program eredetileg kínai.
- A fordítás jellemzően gyors; nagyobb anyagoknál is többnyire másodpercek alatt elkészül az első változat.

> Megjegyzés: Ha a folyamat elakad, az API elérés vagy a konfiguráció (pl. kulcs, modell, jogosultságok) a leggyakoribb ok.

---

## Hibakeresés és tippek

- Ellenőrizd, hogy a Python verzió megfelel-e (3.9+ ajánlott).
- Ellenőrizd az API kulcs érvényességét és a szolgáltatói kvótát.
- Ha a `translate.py` hibaüzenetet ad, olvasd el figyelmesen; tipikusan a konfigurációs érték vagy fájl-elérési út a gond.

### git clone

Ezt a projektet klónozhatod kiindulásként, de ügyelj rá, hogy az API kulcsodat véletlenül se töltsd fel a tárolóba ( `.gitignore`, környezeti változók használata ajánlott).

### ESCO kompetenciák

Vannak esetek, amikor a gépi fordítás nem megfelelő – például az ESCO kompetenciák programleírásokban. Mivel ezeknek hivatalos nevük és leírásuk van, érdemes a hivatalos forrásból dolgozni:

1. Töltsd le a magyar és angol nyelvű kategórialistát az [ESCO honlapjáról](https://esco.ec.europa.eu/en/use-esco/download).  
2. Keresd ki a magyar elnevezésekhez tartozó azonosítókat (pl. [http://data.europa.eu/esco/skill/dc9a236c-c640-43c3-812f-269403591edb](http://data.europa.eu/esco/skill/dc9a236c-c640-43c3-812f-269403591edb)).  
3. Azonosító alapján keresd ki az angol elnevezéseket és leírásokat.  
4. Cseréld a már lefordított dokumentumban a táblázatot a hivatalos angol megfelelőkre.

---

Ha találsz hibát vagy javaslatod van, írj a fenti kapcsolati címen, vagy küldj javaslatot (pull request) a repóhoz. 🙂
