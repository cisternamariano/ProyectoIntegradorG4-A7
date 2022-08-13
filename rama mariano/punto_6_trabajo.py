
'''
Ejercicio 6
'''

consultas_de_frida = [23500, 5960, 2300, 10200, 8900]

def contador_de_gastos(vector):
  # Contador para saber cuántos gastos superaron los 5000 pesos.
  contador_de_gastos = 0
  for i in vector:
    if i > 5000:
      contador_de_gastos += 1
    
  print(f'La cantidad de gastos superiores a 5000 pesos fue de : {contador_de_gastos}')


def sumar_gastos(vector):
    # Acumulador para saber el monto total gastado por la atención de Frida.
    acumulador_de_gastos = 0
    for i in vector:
        acumulador_de_gastos += i
    
    print(f'El monto total gastado por la atención de Frida fue de: {acumulador_de_gastos} pesos.')

def programa():
    contador_de_gastos(consultas_de_frida)
    sumar_gastos(consultas_de_frida)

programa()
