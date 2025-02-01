---
date: "2022-05-01"
summary:
  Progresivní webová aplikace, která představuje výukový portál GoLearn Studenti jsou vyučováni
  průběžnými úkoly a učitelé vidí postup svých žáků a tříd.
tags: ["PWA", "NLP", "PHP", "Nette", "JavaScript", "Python", "Pandas"]
ShowBreadCrumbs: true
cover:
  image: /myown/images/golearn1.webp
title: Progresivní webová aplikace GoLearn
---

Progresivní webová aplikace, která představuje výukový portál GoLearn.
Studenti jsou vyučováni průběžnými úkoly a učitelé vidí postup svých žáků a tříd.

Během jednoho roku jsem odladil ovládání na mobilních zařízeních, přidal podporu instalace progresivní aplikace a umístil aplikaci pomocí TWA do Google Play.

![Simple radio buttons task](/myown/images/golearn1.webp)
![Drag and Drop task](/myown/images/golearn2.webp)

Do stávající platformy jsem vytvořil a integroval nový typ úkolu – konverzace.
Uživatel reaguje dle zadání úkolu a jeho řeč je převáděna na text a následně zpracována neuronovou sítí.
Uživatel tak vede přirozenou konverzaci a jeho projev je automaticky ohodnocen.

![Talking task](/myown/images/golearn3.webp)

Napříč celou platformou bylo zlepšeno UX. Učitelé vidí komplexní statistiky svých studentů.
Studenti naopak vidí srozumitelné výsledky a mohou své dovednosti procvičovat.
Stačí vytvořit třídu a nasdílet svým studentům přístupový QR kód.

![Class report](/myown/images/golearn4.webp)

Konverzace jsem vyvinul jako samostatnou JavaScriptovou knihovnu.
Data dobrovolníků byla získávána v jednoduchém prostředí pro sběr dat.
Následně v pohledu anotátora ohodnocena profesionálními učiteli.
Anotovaná data sloužila pro vyhodnocování úspěšnosti systému automatického vyhodnocení.
Prostředí provede anotátora krok po kroku každým pokusem tak, aby se soustředil vždy jen na konkrétní metriku.
Analýzu dat jsem prováděl pomocí Pandas v prostředí Jupyter Notebook.

![Annotator mode](/myown/images/golearn5.webp)
![Annotator mode](/myown/images/golearn6.webp)
