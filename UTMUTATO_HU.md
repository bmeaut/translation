# DocuTranslate Használati Útmutató

Ez az útmutató lépésről lépésre bemutatja, hogyan fordítsunk anyagokat a DocuTranslate szoftverrel.

## Tartalomjegyzék

1. [Bevezetés](#bevezetés)
2. [Előfeltételek](#előfeltételek)
3. [Telepítés](#telepítés)
4. [Alapvető használat](#alapvető-használat)
5. [Haladó beállítások](#haladó-beállítások)
6. [Gyakori problémák és megoldásaik](#gyakori-problémák-és-megoldásaik)
7. [Hasznos tippek](#hasznos-tippek)

---

## Bevezetés

A DocuTranslate egy hatékony eszköz, amely lehetővé teszi dokumentumok automatikus fordítását különböző nyelvek között. A szoftver támogatja a Markdown, HTML és egyéb szöveges formátumokat, megőrizve a formázást a fordítás során.

### A DocuTranslate főbb jellemzői:

- Automatikus fordítás több nyelvre
- Formázás megőrzése
- Kötegelt feldolgozás támogatása
- Egyszerű parancssori felület
- Testreszabható fordítási beállítások

---

## Előfeltételek

A DocuTranslate használatához a következők szükségesek:

### Rendszerkövetelmények

- **Operációs rendszer**: Windows 10/11, macOS 10.14+, vagy Linux (Ubuntu 18.04+)
- **Python**: 3.8 vagy újabb verzió
- **Memória**: Minimum 4 GB RAM
- **Tárhely**: Minimum 500 MB szabad hely

### Szükséges szoftverek

1. **Python 3.8+** - Letölthető a [python.org](https://www.python.org/downloads/) oldalról
2. **pip** - Python csomagkezelő (általában a Python telepítésével együtt érkezik)
3. **Git** (opcionális) - Verziókezeléshez

### API kulcs beszerzése

A fordításhoz szükséges egy fordítási szolgáltatás API kulcsa:

1. **Google Cloud Translation API**:
   - Hozzon létre egy Google Cloud fiókot
   - Hozzon létre egy új projektet
   - Engedélyezze a Cloud Translation API-t
   - Hozzon létre API hitelesítő adatokat

2. **DeepL API** (alternatíva):
   - Regisztráljon a [DeepL](https://www.deepl.com/pro-api) oldalon
   - Szerezzen be egy API kulcsot

---

## Telepítés

### 1. lépés: Python környezet ellenőrzése

Nyisson egy terminált (parancssor) és ellenőrizze a Python verziót:

```bash
python --version
```

vagy

```bash
python3 --version
```

A verziónak 3.8 vagy magasabbnak kell lennie.

### 2. lépés: DocuTranslate telepítése pip-pel

```bash
pip install docutranslate
```

vagy virtuális környezetben:

```bash
# Virtuális környezet létrehozása
python -m venv docutranslate-env

# Aktiválás (Windows)
docutranslate-env\Scripts\activate

# Aktiválás (Linux/macOS)
source docutranslate-env/bin/activate

# Telepítés
pip install docutranslate
```

### 3. lépés: Telepítés ellenőrzése

```bash
docutranslate --version
```

### 4. lépés: API kulcs konfigurálása

Állítsa be az API kulcsot környezeti változóként:

**Windows (PowerShell):**
```powershell
$env:TRANSLATION_API_KEY = "az-ön-api-kulcsa"
```

**Linux/macOS:**
```bash
export TRANSLATION_API_KEY="az-ön-api-kulcsa"
```

Vagy hozzon létre egy `.env` fájlt a projekt gyökérkönyvtárában:

```
TRANSLATION_API_KEY=az-ön-api-kulcsa
```

---

## Alapvető használat

### Egyetlen fájl fordítása

#### 1. lépés: Készítse elő a fordítandó dokumentumot

Győződjön meg róla, hogy a fordítandó fájl megfelelő formátumban van (pl. Markdown, TXT, HTML).

#### 2. lépés: Futtassa a fordítást

```bash
docutranslate translate input.md --source en --target hu --output output_hu.md
```

**Paraméterek magyarázata:**
- `input.md` - A forrásfájl neve
- `--source en` - A forrás nyelv (angol)
- `--target hu` - A cél nyelv (magyar)
- `--output output_hu.md` - A kimeneti fájl neve

### Több fájl fordítása (kötegelt feldolgozás)

#### Teljes mappa fordítása:

```bash
docutranslate translate ./docs/ --source en --target hu --output ./docs_hu/
```

#### Csak bizonyos fájltípusok fordítása:

```bash
docutranslate translate ./docs/ --source en --target hu --output ./docs_hu/ --filter "*.md"
```

### Támogatott nyelvek listája

A támogatott nyelvek megtekintéséhez:

```bash
docutranslate languages
```

#### Gyakran használt nyelvkódok:

| Nyelv | Kód |
|-------|-----|
| Magyar | hu |
| Angol | en |
| Német | de |
| Francia | fr |
| Spanyol | es |
| Olasz | it |
| Lengyel | pl |
| Cseh | cs |
| Szlovák | sk |
| Román | ro |

---

## Haladó beállítások

### Konfigurációs fájl használata

Hozzon létre egy `docutranslate.config.yaml` fájlt:

```yaml
# DocuTranslate konfiguráció
translation:
  source_language: en
  target_language: hu
  
provider:
  name: google  # vagy "deepl"
  api_key: ${TRANSLATION_API_KEY}  # Környezeti változóból
  
options:
  preserve_formatting: true
  preserve_links: true
  preserve_code_blocks: true
  
output:
  suffix: "_hu"
  directory: "./translated/"
```

### Fordítás a konfigurációs fájllal:

```bash
docutranslate translate ./docs/ --config docutranslate.config.yaml
```

### Fordítási minőség javítása

#### Szójegyzék használata

Hozzon létre egy `glossary.csv` fájlt a gyakran használt kifejezésekhez:

```csv
source,target
"software","szoftver"
"file","fájl"
"directory","könyvtár"
"open source","nyílt forráskódú"
```

Használat:

```bash
docutranslate translate input.md --source en --target hu --glossary glossary.csv
```

### Párhuzamos feldolgozás

Nagy mennyiségű fájl esetén a párhuzamos feldolgozás felgyorsítja a munkát:

```bash
docutranslate translate ./docs/ --source en --target hu --parallel 4
```

### Inkrementális fordítás

Csak a megváltozott fájlok fordítása:

```bash
docutranslate translate ./docs/ --source en --target hu --incremental
```

---

## Gyakori problémák és megoldásaik

### 1. "API key not found" hiba

**Probléma:** A rendszer nem találja az API kulcsot.

**Megoldás:**
- Ellenőrizze, hogy a környezeti változó be van-e állítva
- Próbálja meg közvetlenül megadni a kulcsot: `--api-key "kulcs"`
- Ellenőrizze a `.env` fájl helyességét

### 2. "Rate limit exceeded" hiba

**Probléma:** Túllépte az API hívások korlátját.

**Megoldás:**
- Várjon néhány percet és próbálja újra
- Csökkentse a párhuzamos feldolgozás számát
- Használjon fizetős API csomagot

### 3. Formázási problémák a kimenetben

**Probléma:** A fordított dokumentum formázása eltér az eredetitől.

**Megoldás:**
- Használja a `--preserve-formatting` kapcsolót
- Ellenőrizze a bemeneti fájl formázását
- Próbáljon kisebb részletekben fordítani

### 4. Hibás karakterek a kimenetben

**Probléma:** Ékezetes karakterek helytelenül jelennek meg.

**Megoldás:**
- Győződjön meg róla, hogy a fájl UTF-8 kódolású
- Használja a `--encoding utf-8` kapcsolót

### 5. Telepítési hiba

**Probléma:** A pip nem találja a csomagot.

**Megoldás:**
```bash
pip install --upgrade pip
pip install docutranslate
```

---

## Hasznos tippek

### 1. Fordítás előtti előkészítés

- **Ellenőrizze a forrásdokumentumot** hibákra és elgépelésekre
- **Távolítsa el a felesleges formázást** a jobb eredmény érdekében
- **Készítsen biztonsági másolatot** az eredeti dokumentumokról

### 2. Fordítás közbeni javaslatok

- **Használjon szójegyzéket** a konzisztens terminológia érdekében
- **Teszteljen kis mintán** mielőtt nagy projekten dolgozna
- **Figyelje a folyamat előrehaladását** a `--verbose` kapcsolóval

### 3. Fordítás utáni ellenőrzés

- **Olvassa át a fordított szöveget** hibák után kutatva
- **Ellenőrizze a linkeket** és hivatkozásokat
- **Tesztelje a formázást** különböző megjelenítőkben

### 4. Munkafolyamat automatizálása

Hozzon létre egy shell szkriptet az ismétlődő feladatokhoz:

```bash
#!/bin/bash
# translate.sh - Automatikus fordító szkript

SOURCE_DIR="./docs"
TARGET_DIR="./docs_hu"
SOURCE_LANG="en"
TARGET_LANG="hu"

docutranslate translate "$SOURCE_DIR" \
  --source "$SOURCE_LANG" \
  --target "$TARGET_LANG" \
  --output "$TARGET_DIR" \
  --incremental \
  --verbose
```

### 5. CI/CD integráció

GitHub Actions példa automatikus fordításhoz:

```yaml
name: Translate Documentation

on:
  push:
    paths:
      - 'docs/**'

jobs:
  translate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          
      - name: Install dependencies
        run: pip install docutranslate
        
      - name: Translate documents
        env:
          TRANSLATION_API_KEY: ${{ secrets.TRANSLATION_API_KEY }}
        run: |
          docutranslate translate ./docs \
            --source en \
            --target hu \
            --output ./docs_hu \
            --incremental
            
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add docs_hu/
          git diff --staged --quiet || git commit -m "Update Hungarian translations"
          git push
```

---

## Összefoglalás

A DocuTranslate egy hatékony eszköz dokumentumok fordítására. A legfontosabb lépések:

1. **Telepítse** a szoftvert pip segítségével
2. **Konfigurálja** az API kulcsot
3. **Készítse elő** a fordítandó dokumentumokat
4. **Futtassa** a fordítást a megfelelő paraméterekkel
5. **Ellenőrizze** és javítsa a fordított szöveget

További információkért látogasson el a hivatalos dokumentációhoz vagy a projekt GitHub oldalára.

---

## Kapcsolat és támogatás

Ha kérdése van vagy problémába ütközik:

- **GitHub Issues**: Jelentse a hibákat a projekt GitHub oldalán
- **Dokumentáció**: Olvassa el a hivatalos dokumentációt
- **Közösség**: Csatlakozzon a felhasználói fórumhoz

---

*Utolsó frissítés: 2025. november*
