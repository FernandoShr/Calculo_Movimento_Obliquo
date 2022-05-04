from math import *
g = 9.8; #(m/s^2)


#Funções de coleta dos parâmetros

def parametros():
    v0 = float(input("Insira a Velocidade inicial (m/s):\n"));
    ang = float(input("Insira o Ângulo inicial (°):\n"));
    altura = float(input("Insira a Altura em relação ao solo (cm):\n"));
    return v0, ang, altura;
def componenParame(v0, ang):
    v0x = cos(ang*pi/180)*v0;
    v0y = sin(ang*pi/180)*v0;
    return v0x, v0y;
def pegaparametro(nome, unidade):
    if nome == "Ângulo inicial" or nome == "Tempo":
        var = input("Insira o {0} ({1}):\n"  .format(nome, unidade));
    else:
        var = input("Insira a {0} ({1}):\n"  .format(nome, unidade));
    return var;

#------------------------------------------------------------------//---------------------------------------------------------
#Funções de cáculos


## Calcule as componentes nos eixos x e y da velocidade inicial da bola.
def componentes():
    v0 = float(pegaparametro("Velocidade inicial","m/s"));
    ang = float(pegaparametro("Ângulo inicial", "°"));
    
    v0x, v0y = componenParame(v0,ang);
    
    print("A componente Vx da velocidade inicial possue módulo:", round(v0x,2));
    print("A componente Vy da velocidade inicial possue módulo:", round(v0y,2));
    input("\nPressione 'Enter' para continuar")

#calcula o tempo em que o objeto permance no ar
def calcTempAr(v0y, altura):
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

## Função tempo em que a bola permanece no ar.
def tempAr():
    v0, ang, altura = parametros();
    v0y = sin(ang*pi/180)*v0;
    
    tempoNoAr = round(calcTempAr(v0y, altura), 2)

    print("O tempo em que a bola permanece no ar é de: %.2f segundos" % tempoNoAr);
    input("\nPressione 'Enter' para continuar")

## Encontrar a posição da bola em qualquer instante t
def posicao():
    v0 = float(pegaparametro("Velocidade inicial", "m/s"))
    ang = float(pegaparametro("Ângulo inicial", "°"))
    altura = float(pegaparametro("Altura em relação ao solo", "cm"))
    tempo = float(pegaparametro("Tempo","s"));
    v0x, v0y = componenParame(v0,ang);

    bateu = False;
    tempoAr = calcTempAr(v0y, altura);
    if tempo >= tempoAr:
        tempo = tempoAr;
        bateu = True;

    posX = v0x*tempo;
    posY = v0y*tempo - g*tempo*tempo/2 + altura/100;
    
    if bateu:
        print("O objeto atingiu o solo!");
    print("Posição em X:",round(posX,2));
    print("Posição em Y:",round(posY,2));
    input("\nPressione 'Enter' para continuar")
    ##lembrar de adicionar a condição do TempoAr

def alturaMax():
    v0, ang, altura = parametros();

    v0y = sin(ang*pi/180)*v0;
    altMax = (v0y*v0y)/(2*g) + (altura/100);
    print("Altura máxima atingida foi de %.2f m"% round(altMax,2));
    input("\nPressione 'Enter' para continuar")

def alcanceMax():
    v0, ang, altura = parametros();
   
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

    print("O alcance máximo obtido foi de %.2f m" % round(alcMax,2));
    input("\nPressione 'Enter' para continuar")

def velocidades():
    v0 = float(pegaparametro('Velocidade inicial', "m/s"));
    ang = float(pegaparametro('Ângulo inicial', "°"));
    tempo = float(input("Insira o Tempo no qual deseja obter a velocidade desejada (s):\n"));
    v0x, v0y = componenParame(v0, ang);
    vy = v0y - g*tempo;
    vx = v0x;
    vt = sqrt((vx*vx) + (vy*vy));
    print("A Velocidade, no instante {0:.2f}s, é: {1:.2f} m/s \nCom componentes Vy = {2:.2f} m/s e Vx = {3:.2f} m/s".format(tempo, vt, vy, vx));
    input("\nPressione 'Enter' para continuar")

def veloAltMax():
    v0 = float(pegaparametro("Velocidade inicial", "m/s"))
    ang = float(pegaparametro("Ângulo inicial", "°"))
    v0x,v0y = componenParame(v0, ang);
    tempo = (v0y/g);

    print("A Velocidade no momento da altura máxima (no instante {0:.2f}s) possue módulo {1:.2f} m/s\nCom componentes Vy = 0.00 m/s e Vx = {2:.2f} m/s".format(tempo, v0x, v0x));
    input("\nPressione 'Enter' para continuar")


def menu():
    while True:
        print("\n-----------------Menu-----------------");
        print("1 - Componentes da Velocidade Inicial")
        print("2 - Altura máxima atingida")
        print("3 - Alcance máximo obtido")
        print("4 - Tempo total no ar")
        print("5 - Velocidade, e suas componentes, em qualquer instante t")
        print("6 - Velocidade, e suas componentes, no instante da altura máxima")
        print("7 - Posição em qualquer instante t")
        print("")
        print("0 - Sair")
        print("")
        opcao = (input("Selecione o tipo de cálculo que deseja realizar:"));
        if opcao == "0":
            return;
        elif opcao == '1':
            componentes();
        elif opcao == '2':
            alturaMax();
        elif opcao == '3':
            alcanceMax();
        elif opcao == '4':
            tempAr();
        elif opcao == '5':
            velocidades();
        elif opcao == '6':
            veloAltMax();
        elif opcao == '7':
            posicao();
        else:
            print("\nErro! Por favor, selecione uma das opções solicitadas")
            input("\nPressione 'Enter' para continuar")

menu()