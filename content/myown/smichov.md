---
date: "2022-06-01"
title: Osvětlení urbanistického modelu
summary:
  Osvětlení urbanistického modelu pomocí WiFi kontroléru ESP32 a programovatelného RGB LED pásku
  WS2812.
tags: ["ESP32", "WS2812", "PlatformIO", "C++", "JavaScript", "webové technologie"]
ShowBreadCrumbs: true
cover:
  image: /myown/images/smichov-etapa_IV.webp
---

Osvětlení urbanistického modelu pomocí WiFi kontroléru ESP32 a programovatelného RGB LED pásku WS2812.

![Celkový pohled](/myown/images/smichov-celek.webp)

iPad komunikuje s modelem pomocí WiFi.
Model může zobrazovat jednu z etap nebo je možné zapínat a vypínat jednotlivé bloky.
Je možné regulovat jas modelu a nebo zapnout časovač vypnutí. Každý blok je osazen programovatelnými RGB LED diodami.
Zákazník může volit libovolné barevné kombinace pro různé bloky v rámci etapy pomocí konfiguračního souboru ve formátu JSON.

![Režim etapy I](/myown/images/smichov-etapa_I.webp)
![Režim etapy II](/myown/images/smichov-etapa_II.webp)

Model je osazen zásuvkou pro nabíjení tabletu a vypínačem, kterým je možné osvětlení vypnout.
Kontrolér ESP32 poskytuje webové rozhraní, pomocí kterého se model ovládá.
Rozhraní je možné připnout na domovskou obrazovku iPadu nebo přímo do doku.
Poté se rozhraní chová stejně, jako nativní aplikace iOS.

![Režim etapy III](/myown/images/smichov-etapa_III.webp)

Model se může připojit k existující WiFi síti, může si vytvořit vlastní hotspot nebo kombinaci obojího.
Nejprve bylo použito ESP8266. To se ukázalo jako velmi nespolehlivé při dlouhodobém provozu (restarty, výpadky WiFi).
Po přechodu na ESP32 je odezva modelu rychlá a chování spolehlivé.

![Režim etapy IV](/myown/images/smichov-etapa_IV.webp)

Bloky je možné vyměňovat, zapojení je řešeno páčkovými WAGO svorkami 221.
Adresy diod bloků jsou uloženy v konfiguračním souboru, který se aktualizuje v administraci webového rozhraní.
