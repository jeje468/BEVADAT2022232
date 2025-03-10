"""
1. Értelmezd az adatokat!!!

2. Írj egy osztályt a következő feladatokra:  
     - Neve legyen NJCleaner és mentsd el a NJCleaner.py-ba. Ebben a fájlban csak ez az osztály legyen.
     - Konsturktorban kapja meg a csv elérési útvonalát és olvassa be pandas segítségével és mentsük el a data (self.data) osztályszintű változóba 
     - Írj egy függvényt ami sorbarendezi a csv-t 'scheduled_time' szerint növekvőbe és visszatér a sorbarendezett df-el, a függvény neve legyen 'order_by_scheduled_time' és térjen vissza a df-el  
     - Dobjuk el a from és a to oszlopokat, illetve a nan-okat és adjuk vissza a df-et. A függvény neve legyen 'drop_columns_and_nan' és térjen vissza a df-el  
     - A date-et alakítsd át napokra, pl.: 2018-03-01 --> Thursday, ennek az oszlopnak legyen neve a 'day'. Ezután dobd el a 'date' oszlopot és térjen vissza a df-el. A függvény neve legyen 'convert_date_to_day' és térjen vissza a df-el   
     - Hozz létre egy új oszlopot 'part_of_the_day' névvel. A 'scheduled_time' oszlopból számítsd ki az alábbi értékeit. A 'scheduled_time'-ot dobd el. A függvény neve legyen 'convert_scheduled_time_to_part_of_the_day' és térjen vissza a df-el  
         4:00-7:59 -- early_morning  
         8:00-11:59 -- morning  
         12:00-15:59 -- afternoon  
         16:00-19:59 -- evening  
         20:00-23:59 -- night  
         0:00-3:59 -- late_night  
    - A késéeket jelöld az alábbiak szerint. Az új osztlop neve legyen 'delay'. A függvény neve legyen pedig 'convert_delay' és térjen vissza a df-el
         0 <= x 5  --> 0  
         5 <= x    --> 1  
    - Dobd el a felesleges oszlopokat 'train_id' 'scheduled_time' 'actual_time' 'delay_minutes'. A függvény neve legyen 'drop_unnecessary_columns' és térjen vissza a df-el
    - Írj egy olyan metódust, ami elmenti a dataframe első 60 000 sorát. A függvénynek egy string paramétere legyen, az pedig az, hogy hova mentse el a csv-t (pl.: 'data/NJ.csv'). A függvény neve legyen 'save_first_60k'. 
    - Írj egy függvényt ami a fenti függvényeket összefogja és megvalósítja (sorbarendezés --> drop_columns_and_nan --> ... --> save_first_60k), a függvény neve legyen 'prep_df'. Egy paramnétert várjon, az pedig a csv-nek a mentési útvonala legyen. Ha default value-ja legyen 'data/NJ.csv'

3.  A feladatot a HAZI06.py-ban old meg.
    Az órán megírt DecisionTreeClassifier-t fit-eld fel az első feladatban lementett csv-re. 
    A feladat célja az, hogy határozzuk meg azt, hogy a vonatok késnek-e vagy sem. 0p <= x < 5p --> nem késik, ha 5 < x --> késik.
    Az adatoknak a 20% legyen test és a splitelés random_state-je pedig 41 (mint órán)
    A testset-en 80% kell elérni. Ha megvan a minimum százalék, akkor azzal paraméterezd fel a decisiontree-t és azt kell leadni.

    A leadásnál csak egy fit kell, ezt azzal a paraméterre paraméterezd fel, amivel a legjobb accuracy-t elérted.

    A helyes paraméter megtalálásához használhatsz grid_search-öt.
    https://www.w3schools.com/python/python_ml_grid_search.asp 

4.  A tanításodat foglald össze 4-5 mondatban a HAZI06.py-ban a fájl legalján kommentben. Írd le a nehézségeket, mivel próbálkoztál, mi vált be és mi nem. Ezen kívül írd le 10 fitelésed eredményét is, hogy milyen paraméterekkel probáltad és milyen accuracy-t értél el. 
Ha ezt feladatot hiányzik, akkor nem fogadjuk el a házit!

##################################################################
##                                                              ##
## A feladatok közül csak a NJCleaner javítom unit test-el      ##
## A decision tree-t majd manuálisan fogom lefuttatni           ##
## NJCleaner - 10p, Tanítás - acc-nál 10%-ként egy pont         ##
## Ha a 4. feladat hiányzik, akkor nem tudjuk elfogadni a házit ##
##                                                              ##
##################################################################
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from src.DecisionTreeClassifier import DecisionTreeClassifier

data = pd.read_csv('HAZI\\HAZI06\\data\\NJ.csv')
X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=41)

opt_split = 0
opt_depth = 0
for i in range(5, 31, 5):
    for j in range(5, 31, 5):
        try:
            classifier = DecisionTreeClassifier(min_samples_split=i, max_depth=j)
            classifier.fit(X_train, Y_train)
            Y_pred = classifier.predict(X_test)
            accuracy = accuracy_score(Y_test, Y_pred)
            print(f"Min split: {i}, max depth: {j}, accuracy:{accuracy}")
            if accuracy >= 0.8:
                opt_split = i
                opt_depth = j
                break
        except Exception:
            print(f"Error: min split:{i}, max depth: {j}")
        

print(opt_split)
print(opt_depth)
classifier = DecisionTreeClassifier(min_samples_split=opt_split, max_depth=opt_split)

# Több módon is próbáltam az optimális fit-t megtalálni. Végül két egymásba ágyazott ciklussal próbáltam meghatározni. 
# Mind a két ciklus 1-től 9-ig megy, viszont voltak olyan érték párok amelykre hibát dobott ezért vezettem be egy try blokkot.
# Az órán tanultak alapján általában a legjobb eredményt akkor kapjuk, ha a max_depth nagy érték a min_samples_split pedig kisebb érték.
# A "min_samples_split" meghatározza a belső csomópont felosztásához szükséges minták minimális számát. Ha egy csomópontban a minták száma kevesebb, 
# mint a megadott "min_samples_split" érték, a csomópont nem osztódik tovább, és a felosztási folyamat leáll.
# a "max_depth" beállítja a döntési fa maximális mélységét. Ez korlátozza a fa szintjeinek számát, és így szabályozhatja a modell összetettségét.
#Az eredményekből látható, hogy a (2, 7) illetve a (3, 7) párosítás adta a legjobb megoldás
#Elő teszt eredmények:
# Min split: 1, max depth: 1, accuracy:0.7773333333333333
# Min split: 1, max depth: 2, accuracy:0.7823333333333333
# Min split: 1, max depth: 3, accuracy:0.7839166666666667
# Min split: 1, max depth: 4, accuracy:0.7849166666666667
# Error: min split:1, max depth: 5
# Error: min split:1, max depth: 6
# Error: min split:1, max depth: 7
# Error: min split:1, max depth: 8
# Error: min split:1, max depth: 9
# Min split: 2, max depth: 1, accuracy:0.7773333333333333
# Min split: 2, max depth: 2, accuracy:0.7823333333333333
# Min split: 2, max depth: 3, accuracy:0.7839166666666667
# Min split: 2, max depth: 4, accuracy:0.7849166666666667
# Min split: 2, max depth: 5, accuracy:0.7885833333333333
# Min split: 2, max depth: 6, accuracy:0.7885
# Min split: 2, max depth: 7, accuracy:0.7934166666666667
# Error: min split:2, max depth: 8
# Error: min split:2, max depth: 9
# Min split: 3, max depth: 1, accuracy:0.7773333333333333
# Min split: 3, max depth: 2, accuracy:0.7823333333333333
# Min split: 3, max depth: 3, accuracy:0.7839166666666667
# Min split: 3, max depth: 4, accuracy:0.7849166666666667
# Min split: 3, max depth: 5, accuracy:0.7885833333333333
# Min split: 3, max depth: 6, accuracy:0.7885
# Min split: 3, max depth: 7, accuracy:0.7934166666666667
# Error: min split:3, max depth: 8
# Error: min split:3, max depth: 9
# Min split: 4, max depth: 1, accuracy:0.7773333333333333
# Min split: 4, max depth: 2, accuracy:0.7823333333333333
# Min split: 4, max depth: 3, accuracy:0.7839166666666667
# Min split: 4, max depth: 4, accuracy:0.7849166666666667
# Min split: 4, max depth: 5, accuracy:0.7885833333333333
# Min split: 4, max depth: 6, accuracy:0.7885
# Min split: 4, max depth: 7, accuracy:0.7934166666666667
# Error: min split:4, max depth: 8
# Error: min split:4, max depth: 9
# Min split: 5, max depth: 1, accuracy:0.7773333333333333
# Min split: 5, max depth: 2, accuracy:0.7823333333333333
# Min split: 5, max depth: 3, accuracy:0.7839166666666667
# Min split: 5, max depth: 4, accuracy:0.7849166666666667
# Min split: 5, max depth: 5, accuracy:0.7885833333333333
# Min split: 5, max depth: 6, accuracy:0.7885
# Min split: 5, max depth: 7, accuracy:0.7934166666666667
# Error: min split:5, max depth: 8
# Error: min split:5, max depth: 9
# Min split: 6, max depth: 1, accuracy:0.7773333333333333
# Min split: 6, max depth: 2, accuracy:0.7823333333333333
# Min split: 6, max depth: 3, accuracy:0.7839166666666667
# Min split: 6, max depth: 4, accuracy:0.7849166666666667
# Min split: 6, max depth: 5, accuracy:0.7885833333333333
# Min split: 6, max depth: 6, accuracy:0.7885
# Min split: 6, max depth: 7, accuracy:0.7935
# Min split: 6, max depth: 8, accuracy:0.7955
# Error: min split:6, max depth: 9
# Min split: 7, max depth: 1, accuracy:0.7773333333333333
# Min split: 7, max depth: 2, accuracy:0.7823333333333333
# Min split: 7, max depth: 3, accuracy:0.7839166666666667
# Min split: 7, max depth: 4, accuracy:0.7849166666666667
# Min split: 7, max depth: 5, accuracy:0.7885833333333333
# Min split: 7, max depth: 6, accuracy:0.7885
# Min split: 7, max depth: 7, accuracy:0.7935
# Min split: 7, max depth: 8, accuracy:0.7955
# Error: min split:7, max depth: 9
# Min split: 8, max depth: 1, accuracy:0.7773333333333333
# Min split: 8, max depth: 2, accuracy:0.7823333333333333
# Min split: 8, max depth: 3, accuracy:0.7839166666666667
# Min split: 8, max depth: 4, accuracy:0.7849166666666667
# Min split: 8, max depth: 5, accuracy:0.7885833333333333
# Min split: 8, max depth: 6, accuracy:0.7885
# Min split: 8, max depth: 7, accuracy:0.7935
# Min split: 8, max depth: 8, accuracy:0.7955
# Error: min split:8, max depth: 9
# Min split: 9, max depth: 1, accuracy:0.7773333333333333
# Min split: 9, max depth: 2, accuracy:0.7823333333333333
# Min split: 9, max depth: 3, accuracy:0.7839166666666667
# Min split: 9, max depth: 4, accuracy:0.7849166666666667
# Min split: 9, max depth: 5, accuracy:0.7885833333333333
# Min split: 9, max depth: 6, accuracy:0.7885
# Min split: 9, max depth: 7, accuracy:0.7935
# Min split: 9, max depth: 8, accuracy:0.7955833333333333
# Error: min split:9, max depth: 9

#A második tesztelés alatt 5-30-ig iteráltam 5-ös inkrementálással
# Min split: 5, max depth: 5, accuracy:0.7885833333333333
# Error: min split:5, max depth: 10
# Error: min split:5, max depth: 15
# Error: min split:5, max depth: 20
# Error: min split:5, max depth: 25
# Error: min split:5, max depth: 30
# Error: min split:5, max depth: 35
# Error: min split:5, max depth: 40
# Error: min split:5, max depth: 45
# Error: min split:5, max depth: 50
# Min split: 10, max depth: 5, accuracy:0.7885833333333333
# Error: min split:10, max depth: 10
# Error: min split:10, max depth: 15
# Error: min split:10, max depth: 20
# Error: min split:10, max depth: 25
# Error: min split:10, max depth: 30
# Error: min split:10, max depth: 35
# Error: min split:10, max depth: 40
# Error: min split:10, max depth: 45
# Error: min split:10, max depth: 50
# Min split: 15, max depth: 5, accuracy:0.7885833333333333
# Error: min split:15, max depth: 10
# Error: min split:15, max depth: 15
# Error: min split:15, max depth: 20
# Error: min split:15, max depth: 25
# Error: min split:15, max depth: 30
# Error: min split:15, max depth: 35
# Error: min split:15, max depth: 40
# Error: min split:15, max depth: 45
# Error: min split:15, max depth: 50
# Min split: 20, max depth: 5, accuracy:0.7885833333333333
# Error: min split:20, max depth: 10
# Error: min split:20, max depth: 15
# Error: min split:20, max depth: 20
# Error: min split:20, max depth: 25
# Error: min split:20, max depth: 30
# Error: min split:20, max depth: 35
# Error: min split:20, max depth: 40
# Error: min split:20, max depth: 45
# Error: min split:20, max depth: 50
# Min split: 25, max depth: 5, accuracy:0.7885833333333333
# Min split: 25, max depth: 10, accuracy:0.8003333333333333
# Error: min split:25, max depth: 10
# Min split: 25, max depth: 15, accuracy:0.79125
# Min split: 25, max depth: 20, accuracy:0.7823333333333333
# Min split: 25, max depth: 25, accuracy:0.77975
# Min split: 25, max depth: 30, accuracy:0.779
# Min split: 25, max depth: 35, accuracy:0.779
# Min split: 25, max depth: 40, accuracy:0.779
# Min split: 25, max depth: 45, accuracy:0.779
# Min split: 25, max depth: 50, accuracy:0.779
# Min split: 30, max depth: 5, accuracy:0.7885833333333333
# Min split: 30, max depth: 10, accuracy:0.80075
# Error: min split:30, max depth: 10
# Min split: 30, max depth: 15, accuracy:0.7929166666666667
# Min split: 30, max depth: 20, accuracy:0.78425
#Itt látható, hogy a (25, 10), illetve a (30, 10) párossal sikerült a 80%-t elérni
