# Polish Alcohol for Project Zomboid

A small local mod for **Build 42.13 and newer**. It adds Żywiec, Tyskie, Lech and Żubr beers, plus Żubrówka, Wyborowa and Soplica vodkas. The bottles hold 500 mL of vanilla beer or vodka, so the normal Build 42 fluid, drinking, pouring and drunkenness mechanics apply. They use vanilla bottle visuals (not custom brand labels); the vodka varieties share the same vanilla vodka properties. Bottles start open, so no bottle opener is needed.

## Install

1. Copy the **PolishAlcohol** folder (the one containing `42` and `common`) into `Zomboid/mods/`. On Windows this is normally `C:\Users\<you>\Zomboid\mods\`; on Linux it is `~/Zomboid/mods/`.
2. Enable **Polish Alcohol** in the Mods menu. For an existing save, also enable it under Load → More → Choose Mods.
3. Start or reload the game. Drinks are added to appropriate vanilla loot lists, including liquor-store beer shelves; loot already generated in explored containers will not be replaced. Server owners should install the same folder on the server and clients and add `PolishAlcohol` to the server's Mods list.

## Test in game

In debug mode, use the item list to spawn `Base.PolishZywiec` or `Base.PolishZubrowka`. Right-click the bottle and drink or pour its contents; check that the fluid amount drops and the alcohol effects appear. Look in a newly generated liquor store for the naturally spawning items. Other IDs are `Base.PolishTyskie`, `Base.PolishLech`, `Base.PolishZubr`, `Base.PolishWyborowa` and `Base.PolishSoplica`.

This mod targets the newer Build 42 item syntax, not Build 41 or early 42 builds. It has not been tested in a running copy of the game; loot lists and behavior may change across game updates.
