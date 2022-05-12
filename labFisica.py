# CÓDIGO PARA ESTUDO DE UM OBJETO EM MOVIMENTO OBLÍQUO (SISTEMA IDEAL)
# AUTOR: FERNANDO SHIRAISHI DE ALMEIDA
# (^.^)

#------------------------------------------------------------------//---------------------------------------------------------
from math import *
g = 9.8; #(m/s^2)


# Funções de coleta dos parâmetros

def parametros():
    v0 = float(input("Insira a Velocidade inicial (m/s):\n"));
    ang = float(input("Insira o Ângulo inicial (°):\n"));
    altura = float(input("Insira a Altura em relação ao solo (cm):\n"));
    return v0, ang, altura;
def pegaparametro(nome, unidade):
    if nome == "Ângulo inicial" or nome == "Tempo":
        var = input("Insira o {0} ({1}):\n"  .format(nome, unidade));
    else:
        var = input("Insira a {0} ({1}):\n"  .format(nome, unidade));
    return var;

#------------------------------------------------------------------//---------------------------------------------------------
# Funções de cáculos


# calcula as componentes da velocidade inicial
def componenParame(v0, ang):
    v0x = cos(ang*pi/180)*v0;
    v0y = sin(ang*pi/180)*v0;
    return v0x, v0y;

# calcula o tempo em que o objeto permanece no ar
def calcTempAr(v0, ang, altura):
    v0y = sin(ang*pi/180)*v0;
    delta = v0y*v0y - 4*(-g/2)*(altura/100);
    tSobra1 = (v0y + sqrt(delta))/(-g);
    tSobra2 = (v0y - sqrt(delta))/(-g);

    tsobra = 0;

    if tSobra1 > 0:
        tsobra = tSobra1;
    elif tSobra2 > 0:
        tsobra = tSobra2;
    
    #(v0y/2) = instante em que atinge a altura máxima
    tempoNoAr = (v0y/g)*2 + tsobra;

    return tempoNoAr

# calcula a posição do objeto em determinado tempo durante a trajetória
def calcPosicao(v0, ang, altura, tempo):
    v0x, v0y = componenParame(v0,ang);
    posX = v0x*tempo;
    posY = v0y*tempo - g*tempo*tempo/2 + altura/100;
    return posX, posY;

# calcula a altura máxima atingida pelo objeto durante a trajetória
def calcAltMax(v0, ang, altura):
    v0y = sin(ang*pi/180)*v0;
    altMax = (v0y*v0y)/(2*g) + (altura/100);
    return altMax;

# calcula o alcance horizontal máximo obtido pelo objeto até atingir o solo
def calcAlcMax(v0, ang, altura):
    v0y = sin(ang*pi/180)*v0;
    delta = v0y*v0y - 4*(-g/2)*(altura/100);
    tSobra1 = (v0y + sqrt(delta))/(-g);
    tSobra2 = (v0y - sqrt(delta))/(-g);

    tsobra = 0;

    if tSobra1 > 0:
        tsobra = tSobra1;
    elif tSobra2 > 0:
        tsobra = tSobra2;

    alcsobra = cos(ang*pi/180)*v0*tsobra;

    alcMax = (sin(2*(ang*pi/180))*v0*v0)/g + alcsobra;
    return alcMax;

# calcula a velocidade, e suas componentes, do objeto em qualquer instante durante a trajetória
def calcVelocidades(v0, ang, tempo):
    v0x, v0y = componenParame(v0, ang);
    vy = v0y - g*tempo;
    vx = v0x;
    vt = sqrt((vx*vx) + (vy*vy));
    return vt, vy, vx;

#------------------------------------------------------------------//---------------------------------------------------------
# Funções de impressão dos dados


# Função das componentes nos eixos x e y da velocidade inicial do objeto.
def componentes():
    v0 = float(pegaparametro("Velocidade inicial","m/s"));
    ang = float(pegaparametro("Ângulo inicial", "°"));
    
    v0x, v0y = componenParame(v0,ang);
    
    print('');
    print("A componente Vx da velocidade inicial possui módulo:", round(v0x,2));
    print("A componente Vy da velocidade inicial possui módulo:", round(v0y,2));
    input("\nPressione 'Enter' para retornar ao menu")

# Função tempo em que a bola permanece no ar.
def tempAr():
    v0, ang, altura = parametros();
    
    tempoNoAr = calcTempAr(v0, ang, altura);    

    print("\nO tempo em que a bola permanece no ar é de: %.2f segundos" % round(tempoNoAr,2));
    input("\nPressione 'Enter' para retornar ao menu")

# Função da posição do objeto em qualquer instante t
def posicao():
    v0, ang, altura = parametros();
    tempo = float(pegaparametro("Tempo","s"));

    bateu = False;
    tempoAr = calcTempAr(v0, ang, altura);
    if tempo > tempoAr:
        tempo = tempoAr;
        bateu = True;

    posX, posY = calcPosicao(v0, ang, altura, tempo);
    
    print("");
    if bateu:
        print("O objeto atingiu o solo!");
    print("Posição em X:",round(posX,2));
    print("Posição em Y:",round(posY,2));
    input("\nPressione 'Enter' para retornar ao menu");

# Função da altura máxima atingida do objeto
def alturaMax():
    v0, ang, altura = parametros();
    
    altMax = calcAltMax(v0, ang, altura);

    print("\nAltura máxima atingida foi de %.2f m"% round(altMax,2));
    input("\nPressione 'Enter' para retornar ao menu")

# Função do alcance máximo horizontal obtido pelo objeto
def alcanceMax():
    v0, ang, altura = parametros();
    
    alcMax = calcAlcMax(v0, ang, altura)

    print("\nO alcance máximo obtido foi de %.2f m" % round(alcMax,2));
    input("\nPressione 'Enter' para retornar ao menu")

# Função das velocidades em qualquer instante t
def velocidades():
    v0 = float(pegaparametro('Velocidade inicial', "m/s"));
    ang = float(pegaparametro('Ângulo inicial', "°"));
    tempo = float(input("Insira o Tempo no qual deseja obter a velocidade desejada (s):\n"));

    vt, vy, vx = calcVelocidades(v0, ang, tempo);

    print("\nA Velocidade, no instante {0:.2f}s, é: {1:.2f} m/s \nCom componentes Vx = {2:.2f} m/s e Vy = {3:.2f} m/s".format(tempo, vt, vx, vy));
    input("\nPressione 'Enter' para retornar ao menu")

# Função da velocidade no momento da altura máxima
def veloAltMax():
    v0 = float(pegaparametro("Velocidade inicial", "m/s"))
    ang = float(pegaparametro("Ângulo inicial", "°"))

    v0x,v0y = componenParame(v0, ang);
    tempo = (v0y/g);

    print("\nA Velocidade no momento da altura máxima (no instante {0:.2f}s) possui módulo {1:.2f} m/s\nCom componentes Vx = {2:.2f} m/s e Vy = 0.00 m/s".format(tempo, v0x, v0x));
    input("\nPressione 'Enter' para retornar ao menu")

# Função da velocidade imediatamente antes do objeto atingir o solo
def veloAntesSolo():
    v0, ang, altura = parametros();
    tempoNoAr = calcTempAr(v0, ang, altura);

    vt, vy, vx = calcVelocidades (v0, ang, tempoNoAr);

    print("\nA Velocidade, imediatamente antes de alcançar o solo, é: {0:.2f} m/s \nCom componentes Vx = {1:.2f} m/s e Vy = {2:.2f} m/s".format(vt, vx, vy));
    input("\nPressione 'Enter' para retornar ao menu")

# Função para imprimir todas as opções
def tudo():
    # Definição de variáveis
    v0, ang, altura = parametros();
    tempo = float(input("Insira o Tempo no qual deseja obter a velocidade e a posição (s):\n"));
    
    print('');
    # Componentes da velocidade inicial
    v0x, v0y = componenParame(v0,ang);
    print("A componente Vx da velocidade inicial possui módulo:", round(v0x,2));
    print("A componente Vy da velocidade inicial possui módulo:", round(v0y,2));

    # Tempo em que o objeto permanece no ar
    tempoNoAr = calcTempAr(v0, ang, altura);
    print("\nO tempo em que a bola permanece no ar é de: %.2f segundos" % round(tempoNoAr,2));

    # Posição no instante desejado
    posX, posY = calcPosicao(v0, ang, altura, tempo);
    print("");
    print("Posição em X:",round(posX,2));
    print("Posição em Y:",round(posY,2));

    # Velocidade no instante desejado 
    vt, vy, vx = calcVelocidades(v0, ang, tempo);
    print("\nA Velocidade, no instante {0:.2f}s, é: {1:.2f} m/s \nCom componentes Vx = {2:.2f} m/s e Vy = {3:.2f} m/s".format(tempo, vt, vx, vy));

    # Altura máxima atingida
    altMax = calcAltMax(v0, ang, altura);
    print("\nAltura máxima atingida foi de %.2f m"% round(altMax,2));

    # Alcance máximo obtido
    alcMax = calcAlcMax(v0, ang, altura)
    print("\nO alcance máximo obtido foi de %.2f m" % round(alcMax,2));

    # Velocidade imediatamente antes de alcançar o solo
    vt, vy, vx = calcVelocidades(v0, ang, tempoNoAr);
    print("\nA Velocidade, imediatamente antes de alcançar o solo, é: {0:.2f} m/s \nCom componentes Vx = {1:.2f} m/s e Vy = {2:.2f} m/s".format(vt, vx, vy));

    # Velocidade e instante na altura máxima
    v0x,v0y = componenParame(v0, ang);
    tempo = (v0y/g);
    print("\nA Velocidade no momento da altura máxima (no instante {0:.2f}s) possui módulo {1:.2f} m/s\nCom componentes Vx = {2:.2f} m/s e Vy = 0.00 m/s".format(tempo, v0x, v0x));

    # Fim;
    input("\nPressione 'Enter' para retornar ao menu");
#------------------------------------------------------------------//---------------------------------------------------------

# menu de opções do programa
def menu():
    while True:
        print("\n-----------------Menu-----------------");
        print("1 - Componentes da Velocidade Inicial")
        print("2 - Tempo total no ar")
        print("3 - Posição em qualquer instante t")
        print("4 - Altura máxima atingida")
        print("5 - Alcance máximo obtido")
        print("6 - Velocidade, e suas componentes, em qualquer instante t")
        print("7 - Velocidade, e suas componentes, no instante da altura máxima")
        print("8 - Velocidade, e suas componentes, imediatamente antes de atingir o solo")
        print("9 - Mostrar todas as opções")
        print("")
        print("0 - Sair")
        print("")
        opcao = (input("Selecione o tipo de cálculo que deseja realizar:"));
        if opcao == "0":
            return;
        elif opcao == '1':
            componentes();
        elif opcao == '2':
            tempAr();
        elif opcao == '3':
            posicao();
        elif opcao == '4':
            alturaMax();
        elif opcao == '5':
            alcanceMax();
        elif opcao == '6':
            velocidades();
        elif opcao == '7':
            veloAltMax();
        elif opcao == '8':
            veloAntesSolo();
        elif opcao == '9':
            tudo();
        else:
            print("\nErro! Por favor, selecione uma das opções solicitadas")
            input("\nPressione 'Enter' para retornar ao menu")

menu()