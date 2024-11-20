# importiamo la libreria random
import random
# definizione della funzione
def guess3(min, max):
  # variabili
  a = min
  b = max
  # distanza tra a e b
  c = b - a
  # numero generato con funzione random importata
  nr_generato = random.randint(a, b)
  # Debug del numero generato, scomentare il print sottostante
  print(nr_generato)
  nr_scelto = 0   # dobbiamo inizializzare nr_scelto per poterlo usare nel ciclo
  #ciclo while
  while nr_scelto != nr_generato:
    # chiediamo all'utente di scegliere un numero
    nr_scelto = int(input(f'Scegli un numero tra {a} e {b}: '))
    if nr_scelto < a or nr_scelto > b:
      print(f"Per favore, scegli un numero tra {a} e {b}!")                
      # Interrompe immediatamente l'esecuzione del codice rimanente
      # Salta al prossimo ciclo
      continue 
    valore_relativo = abs(nr_scelto - nr_generato)
    # percentuale
    # int per numero intero
    percentuale = int((valore_relativo / c) * 100)
    # Debug della percentuale, scomentare il print sottostante
    print(f'{percentuale} %')
    # istruzioni condizionali
    if percentuale > 10:
      print('Oceano')
    elif 6 <= percentuale <= 10:
      print('Acqua')
    elif 3 <= percentuale <= 5:
      print('Fuochino')
    elif 0 < percentuale < 3:
      print('Fuoco')
  # l'utente ha indovinato il numero nr_scelto == nr_generato
  else:
    print('Congratulazioni, hai indovinato il numero!')
# chiamata della funzione
guess3(1, 100)