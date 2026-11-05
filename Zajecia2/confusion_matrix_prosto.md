# Confusion matrix — najprościej

To tabela: **co model powiedział** vs **co było naprawdę**.

Weźmy test na chorobę:

- **positive (1)** = chory
- **negative (0)** = zdrowy

---

## 4 możliwe wyniki

| Nazwa | Model mówi | Prawda | Po polsku |
|-------|------------|--------|-----------|
| **TP** True Positive | chory | chory | trafił |
| **TN** True Negative | zdrowy | zdrowy | trafił |
| **FP** False Positive | chory | zdrowy | fałszywy alarm |
| **FN** False Negative | zdrowy | chory | przeoczenie |

---

## Tabela

```text
                 model: zdrowy (0)    model: chory (1)
naprawdę zdrowy           TN                 FP
naprawdę chory            FN                 TP
```

---

## Mini-przykład (10 osób)

Prawda: 4 chore, 6 zdrowych.

Model:

- 3 chorych wykrył dobrze → **TP = 3**
- 1 chorego uznał za zdrowego → **FN = 1**
- 5 zdrowych uznał za zdrowych → **TN = 5**
- 1 zdrowego uznał za chorego → **FP = 1**

```text
              pred zdrowy   pred chory
true zdrowy       5             1
true chory        1             3
```

---

## Wskaźniki (metryki)

Używamy liczb z przykładu: **TP=3, TN=5, FP=1, FN=1**.

### Accuracy (dokładność)

```text
ACC = (TP + TN) / (TP + TN + FP + FN)
ACC = (5 + 3) / 10 = 80%
```

**Co mówi:** ile % wszystkich decyzji było dobrych.  
**Uwaga:** przy nierównych klasach może mylić (łatwo „zgadywać większość”).

---

### Precision (precyzja)

```text
PREC = TP / (TP + FP)
PREC = 3 / (3 + 1) = 75%
```

**Co mówi:** gdy model mówi „chory”, w ilu % ma rację.  
**Ważne, gdy:** fałszywy alarm jest drogi / irytujący.

---

### Recall / Sensitivity / TPR (czułość)

```text
REC = TP / (TP + FN)
REC = 3 / (3 + 1) = 75%
```

**Co mówi:** z wszystkich naprawdę chorych, ilu % złapaliśmy.  
**Ważne, gdy:** przeoczenie jest groźne (choroba, oszustwo, zły kredyt).

---

### F1 Score

```text
F1 = 2 * (PREC * REC) / (PREC + REC)
F1 = 2 * (0.75 * 0.75) / (0.75 + 0.75) = 75%
```

**Co mówi:** jeden wynik łączący precision i recall.  
**Po co:** gdy chcesz kompromis, a nie patrzeć na samą accuracy.

---

### Specificity / TNR (specyficzność)

```text
SPEC = TN / (TN + FP)
SPEC = 5 / (5 + 1) ≈ 83%
```

**Co mówi:** z wszystkich naprawdę zdrowych, ilu % poprawnie uznano za zdrowych.

---

### False Positive Rate (FPR)

```text
FPR = FP / (FP + TN)
FPR = 1 / (1 + 5) ≈ 17%
FPR = 1 - SPEC
```

**Co mówi:** z wszystkich zdrowych, ilu % dostało fałszywy alarm.  
**Po co:** używane na osi X w krzywej ROC.

---

### Szybkie porównanie

| Wskaźnik | Pytanie jednym zdaniem |
|----------|------------------------|
| Accuracy | Ile % ogólnie dobrze? |
| Precision | Gdy mówię „tak”, czy mam rację? |
| Recall | Ile prawdziwych „tak” złapałem? |
| F1 | Jak wygląda kompromis precision + recall? |
| Specificity | Ile prawdziwych „nie” rozpoznałem? |
| FPR | Ile fałszywych alarmów wśród „nie”? |

**Precision vs Recall:**  
często jedno rośnie, gdy drugie spada — dlatego istnieje F1.

---

## Jeszcze prostszy obrazek

Wyobraź sobie bramkarza łapiącego „złe piłki” (positive = zagrożenie):

- **TP** — była zła piłka, obronił
- **TN** — nie było zagrożenia, słusznie stał
- **FP** — bronił, a piłka była niewinna (fałszywy alarm)
- **FN** — była zła piłka, a puścił (najgorsze w medycynie / banku)

---

## Zapamiętaj 1 zdanie

Confusion matrix nie mówi tylko „model ma 80%”.  
Mówi **jakie błędy robi**: za dużo fałszywych alarmów, czy za dużo przeoczeń.
