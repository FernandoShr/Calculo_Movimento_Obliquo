from math import *
g = 9.8;

## Calcule as componentes nos eixos x e y da velocidade inicial da bola.
def componentes():
    v0 = float(input("Insira a Velocidade inicial (m/s): "));
    ang = float(input("Insira a Ângulo inicial (°): "));
    
    v0x = cos(ang*pi/180)*v0;
    v0y = sin(ang*pi/180)*v0;
    
    print("A componente Vx da velocidade inicial possue módulo:", round(v0x,2));
    print("A componente Vy da velocidade inicial possue módulo:", round(v0y,2));

## Calcule o tempo em que a bola permanece no ar.
def tempAr():
    v0 = float(input("Insira a Velocidade inicial (m/s): "));
    ang = float(input("Insira a Ângulo inicial (°): "));
    altura = float(input("Insira a Altura inicial (cm): "));
    v0y = sin(ang*pi/180)*v0;
    delta = v0y*v0y - 4*(-g/2)*(altura/100);
    tSobra1 = (v0y + sqrt(delta))/(-g);
    tSobra2 = (v0y - sqrt(delta))/(-g);

    tsobra = 0;

    if tSobra1 > 0:
        tsobra = tSobra1;
    elif tSobra2 > 0:
        tsobra = tSobra2;
    
    tempoNoAr = (v0y/g)*2 + tsobra;

    print("O tempo em que a bola permanece no ar é: %.2f segundos" % tempoNoAr);

## Encontrar a posição da bola em qualquer instante td.
def posicao():
    v0 = float(input("Insira a Velocidade inicial (m/s): "));
    ang = float(input("Insira a Ângulo inicial (°): "));
    altura = float(input("Insira a Altura inicial (cm): "));
    tempo = float(input("Insira o Tempo no qual deseja obter as coordenadas desejadas (s): "));
    v0x = cos(ang*pi/180)*v0;
    v0y = sin(ang*pi/180)*v0;
    posX = v0x*tempo;
    posY = v0y*tempo - g*tempo*tempo/2 + altura/100;
    print("Posição em X:",round(posX,2));
    print("Posição em Y:",round(posY,2));


posicao();
##componentes();
##tempAr();