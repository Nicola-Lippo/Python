# importiamo la libreria random
import random
# definizione della funzione
def guess2(min, max):
  # Variabili
  a = min
  b = max
  # Numero casuale generato con funzione importata
  nr_generato = random.randint(a, b)
  # Debug del numero generato, scomentare il print sottostante
  # print(nr_generato)
  print(f'Indovina un numero tra {a} e {b}.')
  nr_scelto = 0  
  # Ciclo while
  while nr_scelto != nr_generato:
    # Chiediamo all'utente di scegliere un numero
    nr_scelto = int(input(f"Scegli un numero tra {a} e {b}: "))
    if nr_scelto < a or nr_scelto > b:
      print(f"Per favore, scegli un numero tra {a} e {b}!")                
      # Interrompe immediatamente l'esecuzione del codice rimanente
      # Salta al prossimo ciclo
      continue  
    # Calcolo del valore assoluto
    valore_assoluto = abs(nr_scelto - nr_generato)
    # Istruzioni condizionali
    if valore_assoluto > 10:
      print("Oceano")
    elif 6 <= valore_assoluto <= 10:
      print("Acqua")
    elif 3 <= valore_assoluto <= 5:
      print("Fuochino")
    elif 0 < valore_assoluto < 3:
      print("Fuoco")
  # l'utente ha indovinato il numero nr_scelto == nr_generato
  else:
    print('Congratulazioni, hai indovinato il numero!')    
# Chiamata della funzione
guess2(1, 100)