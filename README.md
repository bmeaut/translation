# Összefoglaló

Az alábbi útmutató lépésről lépésre leírja, hogyan lehet automatizáltan Word dokumentumokat idegen nyelvre fordítani a formátum megőrzésével.

A fordítás a [docutranslate](https://github.com/xunbu/docutranslate) nevű nyílt forráskódú szoftverrel, és egy szabadon választott MI modellel (pl. GPT 5.1) történik. A fordító az eredeti dokumentumban cseréli le a szövegeket, ezzel megőrzi az eredeti formátumot. 

A szoftverrel számos egyetemi anyag fordítása automatizálható, de mivel minden dokumentum egyedi, az utólagos emberi átolvasás elengedhetetlen.

# Nehézségek

- Jelenleg nincs egyetemi/kari szinten elfogadott szótár a szakkifejezésekre, a bizottságok neveire és számos más témakörre. Ha hozzájutunk ilyenhez, frissítjük az oldalon.
- Jelenleg nincs egyetemi állásfoglalás, hogy britt/amerikai angolt használjunk. A szótár egy régi [minisztériumi lista](https://www.nefmi.gov.hu/felsooktatas/dokumentumok/felsooktatasban-gyakran) alapján britt angolt használ 

# Előkészítés

## Python környezet

Telepítő letöltése, futtatása: [python.org](https://www.python.org/downloads/)

## Fordítóprogram

A nyílt forráskódú [docutranslate](https://github.com/xunbu/docutranslate) szoftvert használhjuk. A honlapjukon 3 féle alternatívát is adnak a telepítésre, melyek [itt](https://github.com/xunbu/docutranslate?tab=readme-ov-file#installation) láthatók.

## API kulcsra

A fordításhoz számos nagy nyelvi modell szolgáltatás haszánlható. Érdemes a legfejlettebbek ([openai](https://platform.openai.com/api-keys), [gemini](https://aistudio.google.com/u/0/apikey)) közül választani. A nyelvi modellek használatához előfizetés szükséges, modelltől függően egy 60 oldalas anyag egyszeri lefordítása pár száz forintos tétel lesz. [Regisztrálj valamely szolgáltatónál](https://github.com/xunbu/docutranslate?tab=readme-ov-file#1-get-a-large-model-api-key) és generálj egy API kulcsot.

# Szótár összeállítása

Bár a nyelvi modell nagyon jó az általános szövegek lefordításában, fontos, hogy azokat a kifejezéseket, melyeknek rögzített fordításuk van, helyesen fordítsa le. Ilyenek lehetnek az egyetemi tantárgynevek, bizottságok, szabályzatok angol elnevezései, általános egyetemi szavak (szakdolgozat, docens, vizsgaidőszak stb.) fordításai.
   
Nézzük át a fordítandó anyagot, gyűjtsük ki azokat a kifejezéseket, amik problémásak lehetnek. Jó megoldás az is, hogy alapból generáljunk egy fordítást és az angol szöveg átolvasásával azonosísuk azokat a kifejezéseket, melyekre az MI rossz ajánlatot tesz. Fontos, hogy az elnevezések (tanszékek, tárgyak nevei) sokszor elsőre jónak tűnhetnek, de nem feltétlenül egyeznek meg a hivatalos fordítással. Ezeket mindenképp érdemes szótárba felvenni.

A szótárt a rendszer JSON formátumban várja el. Az egyszerűbb szerkeszthetőség érdekében mellékelünk egy minta Excel fájlt is ([glossary.xlsx](https://github.com/bmeaut/translation/raw/refs/heads/master/glossary.xlsx)), mely harmadik oszlopában legenerálja a szótár fájl sorait. Ezt utána egyszerűen bemásolhatjuk a [glossary.json](https://raw.githubusercontent.com/bmeaut/translation/refs/heads/master/glossary.json) fájlba. Másolásnál figyelni kell rá, hogy az utolsó sor után nem kell vessző, illetve a szótárbejegyzések egy nyitó és záró kapcsoszárójel között legyenek.

# Fordítás előkészítése

A fordítást a [translate.py](https://raw.githubusercontent.com/bmeaut/translation/refs/heads/master/translate.py) fájl futtatásával fogjuk majd végezni. Futtatás előtt szerkeszzük a fájlt és adjuk meg a következő információkat:

- api_key: API kulcs
- model_id: csak akkor szükséges változtatni, ha nem az OpenAI gpt-5.1 modelljével dolgoznál
- uzinfo_mini.docx: ez a forrásfájl, amit le akarunk fordítani. Szükség esetén elérési úttal együtt adjukmeg a sajátunkat.
- translated_uzinfo_mini.docx: ez a célfájl, amit egy Output mappában létrehoz majd a fordító. A neve mindenképpen térjen el az eredeti fájltól.

# Fordítás

A fordítást a következő paranccsal kezdeményezhetjük:

```python
python translate.py
```

A fordítás során fura kínai szövegek jelenhetnek meg, ez normális, mivel a program kínai. A fordítás relatíve gyors, gyakorlatilag nagyobb anyagok esetében is néhány másodpercet vesz csak igénybe. A szoftver folyamatosan mutatja hol tart a folyamatban. 

Előfordulhat, hogy a folyamat elakad, ez esetben értelmezni kell a hibaüzenetet és reagálni rá. Jellemzően az API hozzáféréssel, vagy magával a Python fájlban megadott konfigurációval van gond.

# További tippek
## git clone

Ezt a projektet klónozhatod kiindulásként, de figyelj rá, hogy API kulcsodat véletlenül se push-old vissza

## ESCO

Előfordulhatnak olyan elemek, ahol a gépi fordítás nem megfelelő eszköz. Ilyenek például az ESCO kompetenciák a programleírásoknál. Mivel ezeknek hivatalos nevük és leírásuk van mind magyarul, mind angolul, ezért a fordítási folyamatot nem praktikus automatizálni, e helyett 

1. töltsük le a magyar és az angol nyelvű kategórialistát az [ESCO honlapjáról](https://esco.ec.europa.eu/en/use-esco/download)
2. keressük ki a magyar elnevezésekhez tartozó azonosítókat (pl. [http://data.europa.eu/esco/skill/dc9a236c-c640-43c3-812f-269403591edb](http://data.europa.eu/esco/skill/dc9a236c-c640-43c3-812f-269403591edb))
3. azonosító alapján keressük ki az angol elnevezéseket és leírásokat
4. cseréljük a már lefordított dokumentumban a táblázatot

