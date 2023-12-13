from aviator import AviatorPredictor
import time

# Conectarse al juego 
aviator = AviatorPredictor(bet_url="https://aviator.betplay.com.co/")

# Configurar variables 
initial_bet = 1000  # Monto inicial de apuesta
stop_loss = 0.2 # Porcentaje de stop loss 

# Función para predecir próximo multiplicador
def predict_multi():
   hist = aviator.get_multipliers_history()
   last_5 = hist[-5:]
   
   # Lógica de predicción en base a últimas 5 rondas
   prediction = 2.15
   
   return prediction

# Ciclo principal del bot
while True:

  # Predicción  
  pred_multi = predict_multi() 
  
  # Calcular apuesta  
  if pred_multi > 2:
     bet_amount = initial_bet * (pred_multi - 1)

  else:
     bet_amount = initial_bet
     
  # Jugar ronda  
  print("Predicción:", pred_multi) 
  print("Apuesta:", bet_amount)

  result = aviator.start_round(bet_amount)
  
  # Stop loss 
  if result < stop_loss * bet_amount:
     print("Stop loss hit, saliendo...")
     break
     
  # Tiempo de espera   
  time.sleep(aviator.get_new_round_countdown())

print("Script finalizado")