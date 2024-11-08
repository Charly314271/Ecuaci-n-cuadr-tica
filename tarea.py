 
import random

#Definimos la funcion que resuelva la ecuación de segundo grado
def ecuación_cuadratica(a, b, c):
    #Tomamos en cuenta varios parametro para (ax)**2 + bx + c = 0
    if a == 0 and b == 0: 
        if c == 0:
            return "Infinitas soluciones" 
        else: 
            return "no tiene solución"
    #Sabemos que si a = 0 ----> ((0)x)** 2 = 0 , por ende tenemos una ecuacion lineal.
    elif a == 0: 
        x = -c / b
        return f"La ecuación es lineal y su solución es x = {x}"
 #Usamos el discriminante 
    discriminante = b**2 -4*a*c
    if discriminante > 0: 
        x_1 = (-b + discriminante**0.5)/(2*a)
        x_2 = (-b - discriminante**0.5)/(2*a)
        return f"Las sokluciones son x_1 = {x_1}y x_2 ={x_2}"
    elif discriminante == 0:
        x= -b/ (2*a)
        return f"La solución única es: x = {x}"
    else:
        return "La ecuación no tiene soluciones reales"

def evaluar_funcion(a, b, c, x):
    return a * x**2 + b * x + c

def evaluar_en_intervalo(a, b, c, inicio, fin):           
    numeros_aleatorios = random.sample(range(inicio, fin + 1), 7)    
    resultados = {x: evaluar_funcion(a, b, c, x) for x in numeros_aleatorios}
    return resultados
def main():
    print("Ingrese los coeficientes de la ecuación (a, b, c):")    
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))    

    resultado = ecuación_cuadratica(a, b, c)
    print(resultado)

    for N in range(1, 3):
        y = evaluar_funcion(a, b, c, N)
        print(f"y({N}) = {y}")

    inicio = int(input("Ingrese el inicio del intervalo: "))
    fin = int(input("Ingrese el fin del intervalo: "))
    
    resultados_intervalo = evaluar_en_intervalo(a, b, c, inicio, fin)
    print("Resultados de la evaluación en 7 números aleatorios:")
    for x, y in resultados_intervalo.items():
        print(f"y({x}) = {y}")

if __name__ == "__main__":
    main()