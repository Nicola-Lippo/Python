Quest'ultima versione del gioco è sicuramente più difficile, soprattutto se la distanza tra a e b è molto elevata. Se invece la distanza tra a e b è molto bassa il gioco finisce subito. Sarebbe bello avere delle regole più dinamiche che si adattino alla distanza tra a e b.

Scrivi una nuova funzione guess3() dove gli indizi non sono legati alla distanza assoluta (come nell'esercizio semplice) tra nr_scelto e nr_generato ma alla distanza relativa (cioè in termini percentuali rispetto alla distanza tra a e b):

se il valore assoluto di nr_scelto - nr_generato diviso b - a è minore del 3% >>> Fuoco!
se il valore assoluto di nr_scelto - nr_generato diviso b - a è compreso tra il 3% e il 5% (inclusi) >>> Fuochino!
se il valore assoluto di nr_scelto - nr_generato diviso b - a è compreso tra il 6% e il 10% (inclusi) >>> Acqua!
altrimenti >>> Oceano!