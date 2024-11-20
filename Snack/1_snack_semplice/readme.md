Scrivi una nuova funzione guess2() che permetta di giocare a Guess the number ma questa volta, invece di ricevere come feedback "numero troppo basso" o "numero troppo alto", l'utente riceverà come feedback i seguenti indizi:

se il valore assoluto di nr_scelto - nr_generato è minore di 3 >>> Fuoco!
se invece il valore assoluto di nr_scelto - nr_generato è compreso tra 3 e 5 (inclusi) >>> Fuochino!
se invece il valore assoluto di nr_scelto - nr_generato è compreso tra 6 e 10 (inclusi) >>> Acqua!
altrimenti >>> Oceano!
Suggerimento: in Python puoi calcolare il valore assoluto di un valore x col la funzione abs(x).