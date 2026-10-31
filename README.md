# Polish Alcohol for Project Zomboid

A small local mod for **Build 42.13 and newer**. It adds Żywiec, Tyskie, Lech and Żubr beers, plus Kustosz, Romper, Imperator, Karpackie, Tatra and Harnaś beers; and Żubrówka, Wyborowa, Soplica, Adam Mickiewicz, Chopin and Wratislavia vodkas. The bottles hold 500 mL of vanilla beer or vodka, so the normal Build 42 fluid, drinking, pouring and drunkenness mechanics apply. Each item has an original, simplified brand-inspired label on its inventory icon. Held and ground 3D models still use generic vanilla bottles without custom labels; they are not accurate replicas. The vodka varieties share the same vanilla vodka properties. Bottles start open, so no bottle opener is needed.

## Install

1. Copy the **PolishAlcohol** folder (the one containing `42` and `common`) into `Zomboid/mods/`. On Windows this is normally `C:\Users\<you>\Zomboid\mods\`; on Linux it is `~/Zomboid/mods/`.
2. Enable **Polish Alcohol** in the Mods menu. For an existing save, also enable it under Load → More → Choose Mods.
3. Start or reload the game. Drinks are added to appropriate vanilla loot lists, including liquor-store beer shelves; loot already generated in explored containers will not be replaced. Server owners should install the same folder on the server and clients and add `PolishAlcohol` to the server's Mods list.

## Test in game

In debug mode, use the item list to spawn `Base.PolishZywiec` or `Base.PolishZubrowka`. Right-click the bottle and drink or pour its contents; check that the fluid amount drops and the alcohol effects appear. Look in a newly generated liquor store for the naturally spawning items. Other IDs are `Base.PolishTyskie`, `Base.PolishLech`, `Base.PolishZubr`, `Base.PolishWyborowa` `Base.PolishSoplica`, `Base.PolishKustosz`, `Base.PolishRomper`, `Base.PolishImperator`, `Base.PolishKarpackie`, `Base.PolishTatra`, `Base.PolishHarnas`, `Base.PolishAdamMickiewicz`, `Base.PolishChopin` and `Base.PolishWratislavia`.

This mod targets the newer Build 42 item syntax, not Build 41 or early 42 builds. It has not been tested in a running copy of the game; loot lists and behavior may change across game updates.

## Label artwork and references

The 16 inventory icons are original, simplified illustrations, not exact reproductions or official artwork. Packaging varies by product and year; these are intended to make items recognizable, not document a particular edition. All drinks currently use vanilla 3D models, so their labels are **not** visible on held or dropped bottles. Strong beers still use the vanilla beer fluid rather than a brand-specific ABV.

Design references include the [Żywiec logo description](https://en.wikipedia.org/wiki/%C5%BBywiec_Brewery), [Tyskie packaging](https://www.bargainbooze.co.uk/brand/tyskie/), [Lech bottle](https://hywelsbiglog.wordpress.com/2008/02/23/beer-review-lech-premium/), [Żubr packaging](https://en.wikipedia.org/wiki/%C5%BBubr_(beer)), [Kustosz Extra](https://browarparagraf.com/2018/04/kusztosz-nie-taki-extra/), [Tatra's historical label](https://pl.wikipedia.org/wiki/Tatra_(piwo)), [Chopin Potato](https://www.diffordsguide.com/beer-wine-spirits/1749/chopin-potato-vodka), and [Wratislavia and other Polish vodkas](https://alkohole.pl/blog/polska-wodka-poznaj-marki-ktore-sa-nasze-i-sprawdz-liste-kraftowych-wodek/). Other colour schemes are illustrative approximations, not verified brand designs. The icon generator in `tools/generate_icons.py` uses Pillow and DejaVu fonts.
