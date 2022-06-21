---
layout: post
title:  Docházka
date:   2015-01-01
excerpt: Jednoduchá stránka napsaná v jazyce PHP zobrazující přítomnost studentů a učitelů školy SPŠEIT Purkyňova.
thumb_img_path: /assets/images/web_zdeandroid.webp
tags: webové technologie PHP cron
---

Jednoduchá stránka napsaná v jazyce PHP zobrazující přítomnost studentů a učitelů školy SPŠEIT Purkyňova. Stránka je cílená na mobilní telefony. Obsahuje pouze jedno vstupní pole, kde lze zadat příjmení žáka pro zobrazení docházky, zkratku třídy/učitele/učebny pro zobrazení jejího rozvrhu hodin. Zobrazuje i data, která nejsou mimo školní síť dostupná. Stránka se zobrazuje korektně na všech běžných prohlížečích. V případě zájmu obsahuje i cron, který periodicky kontroluje docházku konkrétních studentů a pokud některý ze studentů chybí déle, než nastavenou dobu, tak systém zašle upozornění na email.

![Desktop screenshot](/assets/images/web_zdewin.webp)
![Mobile screenshot](/assets/images/web_zdeandroid.webp)

 - [http://dochazku.cekuj.net](http://dochazku.cekuj.net)
