import datetime
import getpass
import random
import socket
import math

HOST = 'localhost'
PORT = 12000
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.bind((HOST, PORT))
print("Serveri u startua ne localhost :", str(PORT))
print("Serveri eshte i gatshem te pranoj kerkesa!")


def BASHKETINGELLORE(sentence):
    sentence = sentence.lower()
    numerimi = 0
    ll = sentence.count("ll")
    dh = sentence.count("dh")
    rr = sentence.count("rr")
    gj = sentence.count("gj")
    sh = sentence.count("sh")
    th = sentence.count("th")
    zh = sentence.count("zh")
    nj = sentence.count("nj")
    xh = sentence.count("xh")
    numerimi = ll + dh + rr + gj + sh + th + xh + zh + nj
    char1 = sentence.replace("ll", "")
    char2 = char1.replace("zh", "")
    char3 = char2.replace("dh", "")
    char4 = char3.replace("rr", "")
    char5 = char4.replace("th", "")
    char6 = char5.replace("nj", "")
    char7 = char6.replace("gj", "")
    char8 = char7.replace("sh", "")
    char9 = char8.replace("xh", "")

    for x in char9:
        if x in ["b", "c", "ç", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z"]:
            numerimi = numerimi + 1
    return numerimi


def game():
    stringu = "("
    for numbers in range(7):
        stringu = stringu + str(random.randint(1,49)) + ","
    stringu = stringu[0:-2]
    stringu = stringu + ")"
    return stringu


def fibonacci (fib):
    fibNum1 = int(fib)
    fibNum2 = fibNum1 + 1
    alpha = -1
    beta = 1
    for i in range(0, fibNum2):
        omega = alpha + beta
        alpha = beta
        beta = omega
    return beta


def convert(message):
    pjesaStringut1 = str(message[message.find(' ') + 1:])
    opcioni = str(pjesaStringut1[0:pjesaStringut1.find(' ')])
    x = float(pjesaStringut1[pjesaStringut1.find(' ') + 1:])
    if opcioni == "KILOWATTTOHORSEPOWER":
        return x * 1.341
    elif opcioni == "HORSEPOWERTOKILOWATT":
        return x / 1.341
    elif opcioni == "DEGREESTORADIANS":
        return x * 0.01745
    elif opcioni == "RADIANSTODEGREES":
        return x / 0.01745
    elif opcioni == "GALLONSTOLITERS":
        return x * 3.785
    elif opcioni == "LITERSTOGALLONS":
        return x / 3.785



def calculator(message):
    parts = str(message[message.find(' ') + 1:])
    veprimi = str(parts[0:parts.find(' ')])
    part1 = str(parts[parts.find(' ') + 1:])
    n1 = float(part1[0:part1.find(' ')])
    n2 = float(part1[part1.find(' ') + 1:])
    if veprimi == "MBLEDHJA":
         return n1 + n2
    elif veprimi == "ZBRITJA":
         return n1 - n2
    elif veprimi == "SHUMEZIMI":
         return n1 * n2
    elif veprimi == "PJESETIMI":
         return n1 / n2
    elif veprimi == "MBETJA":
         return n1 % n2


def weekDay(message):
    argumenti = str(message[message.find(' ') + 1:])
    dita = int(argumenti[0:argumenti.find('.')])
    argumenti2 = str(argumenti[argumenti.find('.') + 1:])
    muaji = int(argumenti2[0:argumenti2.find('.')])
    viti = int(argumenti2[argumenti2.find('.')+1:])
    arrays = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    java    = ['Diele',
              'Hene',
              'Marte',
              'Merkure',
              'Enjte',
              'Premte',
              'Shtune']
    pasShkurtit = 1
    if muaji > 2:
        pasShkurtit = 0
    temp = viti - 1700 - pasShkurtit
    ditaJaves  = 5
    ditaJaves += (temp + pasShkurtit) * 365
    ditaJaves += temp / 4 - temp / 100 + (temp + 100) / 400
    ditaJaves += arrays[muaji - 1] + (dita - 1)
    ditaJaves %= 7
    return  java[int(ditaJaves)]


while 1:
    inWord = serversocket.recvfrom(128)
    message = inWord[0].upper().decode('UTF-8')
    address = inWord[1]

    if message == "IPADRESA":
        outWord = "IP adresa juaj: " + str(socket.gethostbyname(socket.gethostname()))

    elif message == "NUMRIIPORTIT":
        outWord = "Numri i portit tuaj eshte: " + str(address[1])

    elif message[0:message.find(' ')] == "BASHKETINGELLORET":
        sentence = message[message.find(' ') + 1:]
        nrBashk = str(BASHKETINGELLORE(sentence))
        outWord = "Numri i bashketingelloreve nga fjala e kerkuar eshte: " + nrBashk

    elif message[0:message.find(' ')] == "PRINTIMI":
        outWord = "Fjalia qe keni shkruar:" + message[message.find(' ') + 1:].strip()

    elif message == "EMRIIKOMPJUTERIT":
        outWord = "Emri i kompjuterit tuaj eshte: " + getpass.getuser()

    elif message == "KOHA":
        outWord = "Tani koha eshte: " + datetime.datetime.now().strftime(" %H:%M:%S %p %d.%m.%Y")

    elif message == "LOJA":
        outWord = "Shtate numrat e rastesishem nga rangu 1-49 jane:" + game()

    elif message[0:message.find(' ')] == "FIBONACCI":
        fib = str(message[message.find(' ') + 1:])
        fibCipher = str(fibonacci(fib))
        outWord = "Numri fibonacci i numrit qe keni shkruar eshte:" + fibCipher

    elif message[0:message.find(' ')] == "KONVERTIMI":
        con = str(convert(message))
        outWord = "Rezultati eshte:" + con


    elif message[0:message.find(' ')] == "KALKULATORI":
        res = str(calculator(message))
        outWord = "Rezultati eshte: " + res

    elif message[0:message.find(' ')] == "DITA":
        outWord = "Dita ishte e " + weekDay(message) + "!"

    else:
        outWord = "Ju duhet te shenoni njeren nga fjalet/fjalit me lart!Falemnderit!"

    print("Kerkesa nga klienti:" + message)
    serversocket.sendto(str.encode(str(outWord)), address)


serversocket.close()