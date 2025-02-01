---
date: "2015-01-01"
title: Docházka
summary:
  Jednoduchá stránka napsaná v jazyce PHP zobrazující přítomnost studentů a učitelů školy
  SPŠEIT Purkyňova.
tags: ["webové technologie", "PHP", "cron"]
ShowBreadCrumbs: true
cover:
  image: /myown/images/web_zdeandroid.webp
---

Jednoduchá stránka napsaná v jazyce PHP zobrazující přítomnost studentů a učitelů školy SPŠEIT Purkyňova.
Stránka je cílená na mobilní telefony. Obsahuje pouze jedno vstupní pole, kde lze zadat příjmení žáka pro zobrazení docházky, zkratku třídy/učitele/učebny pro zobrazení jejího rozvrhu hodin.
Zobrazuje i data, která nejsou mimo školní síť dostupná. Stránka se zobrazuje korektně na všech běžných prohlížečích.
V případě zájmu obsahuje i cron, který periodicky kontroluje docházku konkrétních studentů a pokud některý ze studentů chybí déle, než nastavenou dobu, tak systém zašle upozornění na email.

![Desktop screenshot](/myown/images/web_zdewin.webp)
![Mobile screenshot](/myown/images/web_zdeandroid.webp)

- [http://dochazku.cekuj.net](http://dochazku.cekuj.net)
