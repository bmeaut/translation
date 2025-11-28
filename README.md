# Összefoglaló

Az alábbi útmutató lépésről lépésre leírja, hogyan lehet automatizáltan Word dokumentumokat idegen nyelvre fordítani a formátum megőrzésével.

A fordítás a [docutranslate](https://github.com/xunbu/docutranslate) nevű nyílt forráskódú szoftverrel, és egy szabadon választott MI modellel (pl. GPT 5.1) történik. A fordító az eredeti dokumentumban cseréli le a szövegeket, ezzel megőrzi az eredeti formátumot. 

A szoftverrel számos egyetemi anyag fordítása automatizálható, de mivel minden dokumentum egyedi, az utólagos emberi átolvasás elengedhetetlen.

# Nehézségek

- Jelenleg nincs egyetemi/kari szinten elfogadott szótár a szakkifejezésekre, a bizottságok neveire és számos más témakörre. Ha hozzájutunk ilyenhez, frissítjük az oldalon.
- Jelenleg nincs egyetemi állásfoglalás, hogy britt/amerikai angolt használjunk. A szótár egy régi [minisztériumi lista](https://www.nefmi.gov.hu/felsooktatas/dokumentumok/felsooktatasban-gyakran) alapján britt angolt használ 

# Előkészítés

1. Python környezetre

Telepítő letöltése: [python.org](https://www.python.org/downloads/)

2. Fordítóprogramra

A nyílt forráskódú [docutranslate](https://github.com/xunbu/docutranslate) szoftvert használhjuk. A honlapjukon 3 féle alternatívát is adnak a telepítésre, melyek [itt](https://github.com/xunbu/docutranslate?tab=readme-ov-file#installation) láthatók.

3. API kulcsra

A fordításhoz számos nagy nyelvi modell szolgáltatás haszánlható. Érdemes a legfejlettebbek ([openai](https://platform.openai.com/api-keys), [gemini](https://aistudio.google.com/u/0/apikey)) közül választani. A nyelvi modellek használatához előfizetés szükséges, modelltől függően egy 60 oldalas anyag egyszeri lefordítása pár száz forintos tétel lesz. [Regisztrálj valamely szolgáltatónál](https://github.com/xunbu/docutranslate?tab=readme-ov-file#1-get-a-large-model-api-key) és generálj egy API kulcsot.

# Szótár összeállítása

Bár a nyelvi modell nagyon jó az általános szövegek lefordításában, fontos, hogy azokat a kifejezéseket, melyeknek rögzített fordításuk van, helyesen fordítsa le. Ilyenek lehetnek az egyetemi tantárgynevek, bizottságok, szabályzatok angol elnevezései, általános egyetemi szavak (szakdolgozat, docens, vizsgaidőszak stb.) fordításai.
   
Nézzük át a fordítandó anyagot, gyűjtsük ki azokat a kifejezéseket, amik problémásak lehetnek. Jó megoldás az is, hogy alapból generáljunk egy fordítást és az angol szöveg átolvasásával azonosísuk azokat a kifejezéseket, melyekre az MI rossz ajánlatot tesz. Fontos, hogy az elnevezések (tanszékek, tárgyak nevei) sokszor elsőre jónak tűnhetnek, de nem feltétlenül egyeznek meg a hivatalos fordítással. Ezeket mindenképp érdemes szótárba felvenni.

A szótárt a rendszer JSON formátumban várja el. Az egyszerűbb szerkeszthetőség érdekében mellékelünk egy minta Excel fájlt is, mely harmadik oszlopában legenerálja a szótár fájl sorait. Ezt utána egyszerűen bemásolhatjuk a glossary.json fájlba.

# 
