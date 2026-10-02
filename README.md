# SRD_Z2026
Repozytorium do przedmiotu Statystyczne Reguły Decyzyjne [223490-D] - Semestr zimowy 2026/2027

**Wymagane oprogramowanie**

W trakcie ćwiczeń będziemy korzystać z Pythona w notatniku Jupyter.
Do uruchomienia materiałów wykorzystanych w trakcie ćwiczeń potrzebne jest następujące oprogramowanie:
* [Python](https://www.python.org/downloads/) (użytkownicy Windowsa w łatwy sposób mogą pobrać Pythona z [Anacondą](https://anaconda.org/))
* [Jupyter](https://jupyter.org/install) Notebook lub Jupyter Lab
* [Git](https://git-scm.com/)

---
**Kontakt**

Imię i nazwisko: Łukasz Kraiński

Email: lkrain@sgh.waw.pl

---
**Prowadzący zajęcia**

* wykłady: Bogumił Kamiński
* ćwiczenia: Łukasz Kraiński, Marcin Rutecki

Konsultacje:
* Łukasz Kraiński - sala C-3B wtorki 15:20-17:00, lub online na MS Teams
* Marcin Rutecki - online na MS Teams
---
**Harmonogram**

* wykłady: wtorki, G-Aula B, 09:50

* ćwiczenia: wtorki, C-4D:
  * 13:30 (Grupy 11 i 12) - Łukasz Kraiński
  * 15:20 (Grupy 13 i 14) - Marcin Rutecki
  * 17:10 (Grupy 15 i 16) - Łukasz Kraiński
  * 19:00 (Grupa 17) - Łukasz Kraiński

---

**Tematy spotkań**
|     #    |     Temat                                                                                          |
|----------|----------------------------------------------------------------------------------------------------|
|     1    |     Zajęcia   organizacyjne; wprowadzenie do narzędzia Jupyter Notebook z językiem Python   |
|     2    |     Metody   oceny jakości modeli klasyfikacyjnych                                                 |
|     3    |     Regularyzacja i walidacja krzyżowa                                                            |
|     4    |     Modele oparte na drzewach (CART, Random Forest, XGBoost)                            |
|     5    |     TabularLLM                                                        |
|     6    |     Konkurs modelarski                                                                         |
|     7    |     Prezentacje projektów                                                                |

---
**Literatura**

* Literatura podstawowa
  * Materiały udostępniane na wykładzie
  * Gareth J., Witten D., Hastie T., Tibshirani R. (2023), [An Introduction to Statistical Learning](https://www.statlearning.com/)
* Literatura dodatkowa
  * Hastie T., Tibshirani R., Friedman J. (2017), [The Elements of Statistical Learning](https://hastie.su.domains/ElemStatLearn/)
  * Kamiński B. (2022), [Julia for Data Analysis](https://www.manning.com/books/julia-for-data-analysis)
  * Mykel J. Kochenderfer, Tim A. Wheeler, And Kyle H. Wray (2022), [Algorithms for Decision Making](https://algorithmsbook.com/)
  * Stephen Boyd and Lieven Vandenberghe, [Introduction to Applied Linear Algebra](http://vmls-book.stanford.edu/)
  * Kamiński B., Zawisza M. (2012), [Receptury w R. Podręcznik dla ekonomisty](http://bogumilkaminski.pl/projekty/)
  * VanderPlas J. (2016), [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
  * Géron A. (2025), [Hands-On Machine Learning with Scikit-Learn and PyTorch](https://github.com/ageron/handson-mlp)

---
**Zasady zaliczenia**

* Kolokwium teoretyczne na ostatnim wykładzie (50 punktów)
* Praktyczny projekt w grupach na ćwiczeniach (50 punktów)
* Punkty dodatkowe:
  * Prace domowe
  * Konkurs w trakcie laboratorium

---

#### Projekt analityczny (50 punktów)

Projekt można realizować w grupach liczących do 3 osób. Należy wykorzystać zbiór danych zawierający ponad 5000 rekordów oraz co najmniej 10 cech.

Zadanie polega na analizie danych, przeprowadzeniu procesu modelowania i sporządzeniu raportu o następującej strukturze:

1) Wprowadzanie i opis wybranego problemu (klasyfikacja lub regresja), opis zbioru danych.

2) Czyszczenie i wstępne przetwarzanie danych - imputacja braków danych, standaryzacja, kodowanie typu one-hot, transformacja wartości odstających, itp.

3) Graficzna i opisowa analiza eksploracyjna (EDA), m.in. graficzna prezentacja zależności pomiędzy wybraną zmienną celu i zmiennymi niezależnymi, wykonanie i opisanie wyników segmentacji (klastrowania) rekordów, itp.

4) Stworzenie min. 3 modeli i tuning hiperparametrów do zadania klasyfikacji lub regresji

5) Graficzna i opisowa ocena oraz wybór modelu

6) Podsumowanie wyników, dyskusja na temat napotkanych problemów, wyzwań i zastosowanych rozwiązań

Kod oraz opis i komentarze należy zamieścić w pliku typu Jupyter Notebook.

Raporty należy przesłać na adres lkrain@sgh.waw.pl w formatach .html/.pdf oraz .ipynb (jeden format do odczytu, drugi wykonywalny).
Podczas ostatnich zajęć odbędą się prezentacje projektów (proszę przygotować oddzielną prezentację) trwające około 10 minut. Prezentacje nie są oceniane oddzielnie, ale mogą wpłynąć na ocenę końcową projektu.

Termin oddania raportu upływa **19.01.2027** - ostatnie zajęcia laboratoryjne w semestrze.

---
**Ocena końcowa**
|Od |Do|Ocena|
|-----|--|--------|
|0 |49| 2.0|
|50 |59 |3.0|
|60 |69 |3.5|
|70 |79 |4.0|
|80 |89 |4.5|
|90 |100 |5.0|
