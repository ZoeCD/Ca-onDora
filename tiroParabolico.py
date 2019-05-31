import matplotlib.pyplot as plt
import math

def main():
    print("***Bienvenido***")
    print("Este programa se utiliza para graficar el movimiento del tiro del proyectil de Dora.")
    angulo = int(input("Por favor ingresar un ángulo. Se recomienda a un ángulo de 48º a 65º: "))



    pesoProyectil = 7100 # en kilogramos
    velocidadInicial = 720 #metros/segundo
    alturaCañon = 11.60#metros
    gravedad = 9.8 # metros/segundo^2
    fricciionAire = 36.8# km /m^3

    posX=[]
    posY=[]
    posXBasica = []
    posYBasica = []
    velocidadesfY = []
    velocidadesfX = []
    tiempos=[]

    Vox= velocidadInicial*math.cos(math.radians(angulo))
    Voy= velocidadInicial*math.sin(math.radians(angulo))

    tiempoMax = (pesoProyectil/fricciionAire)*math.log(1+((fricciionAire*Voy)/(pesoProyectil*gravedad)))
    tiempoVuelo = int(tiempoMax) * 2

    yMax = alturaCañon - (((math.pow(pesoProyectil,2)*gravedad)/math.pow(fricciionAire,2))*math.log(1+((fricciionAire*Voy)/(pesoProyectil*gravedad))))+((pesoProyectil*Voy)/fricciionAire)



    for tiempo in range(0,tiempoVuelo,3):
        exponente= -(fricciionAire*tiempo)/pesoProyectil
        x = (pesoProyectil/fricciionAire)*Vox*(1-math.exp(exponente))
        posX.append(x)
        tiempos.append(tiempo)
        y = alturaCañon - (( (pesoProyectil*gravedad)/fricciionAire)*tiempo) + (pesoProyectil/fricciionAire)*(Voy+((pesoProyectil*gravedad)/fricciionAire))*(1-math.exp(exponente))
        posY.append(y)
        xBasica = Vox * tiempo
        yBasica = alturaCañon + (Voy*tiempo) - ((gravedad * math.pow(tiempo, 2))/2)
        posYBasica.append(yBasica)
        posXBasica.append(xBasica)
        vfy = ((-pesoProyectil*gravedad)/fricciionAire)+((Voy+((pesoProyectil*gravedad)/fricciionAire))*math.exp(exponente))
        vfx = Vox*math.exp(exponente)
        velocidadesfX.append(vfx)
        velocidadesfY.append(vfy)

    print("El tiempo de vuelo es: " + str(tiempoVuelo) + " segundos")
    print("Y la altura máxima es: " + str(yMax) + " metros")
    print("Gracias")



    plt.subplot(131, label="POSICIONES")
    plt.xlabel("Distancia")
    plt.ylabel("Altura")
    plt.scatter(posXBasica, posYBasica, label="Sin aire")
    plt.scatter(posX, posY, label="Con aire")
    plt.legend(loc='lower center', shadow=True)

    plt.subplot(132, label ="Velocidad en y")
    plt.xlabel("Tiempo")
    plt.ylabel ("Velocidad en y")
    plt.scatter(tiempos,velocidadesfY)

    plt.subplot(133, label="Velocidad en x")
    plt.xlabel("Tiempo")
    plt.ylabel ("Velocidad en x")
    plt.scatter(tiempos,velocidadesfX)
    plt.show()





main()