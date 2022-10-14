
import socket


def scanner():
    portas = []
    respostar = 'S'
    ip = input("\n Digite endereço IP:")
    while respostar == 'S':
        porta = int(input("\n Digite o numero da porta:"))
        portas.append(porta)
        respostar = input(
            "\n Digite S para adiconar outra porta ou N para sair:").upper()
    for port in portas:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        codigo = scanner.connect_ex((ip, port))
        if codigo == 0:
            print("A porta:" + str(port) + "  está aberta!")
        else:
            print("A porta:" + str(port) + "  está fechada")


scanner()
