import getpass
import datetime #koha
import random #importim per gjetjen e rastesishme te nje numri
import math
import socket #soketa
from _thread import * #import per threds


serverName = 'localhost' #ketu shenohet ipadresa po kete rast eshte localhost
serverPort = 12000 #porti
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName, serverPort)) #lidh me nje ipadrese dhe port te caktuar
print('Serveri eshte startuar ne localhost ne portin ' + str(serverPort)) #kur te lidhet tregon me cilin port
serverSocket.listen(5) #tregon deri ne sa mund te lidhen
print('Serveri eshte i gatshem te pranoj kerkesat e klientit !') #pas lidhjes printohet ne server




def BASHKETINGELLORE(sentence): #definim i funksionit
        sentence = sentence.lower()   #shnderrohen ne shkronja te vogla gjithqka qe hyn si argument
        numerimi = 0
        ll = sentence.count("ll")       #funksioni .count() njeh sa here nje ose me shume karaktere shfaqen brenda nje stringu
        dh = sentence.count("dh")
        rr = sentence.count("rr")
        gj = sentence.count("gj")
        sh = sentence.count("sh")
        th = sentence.count("th")
        zh = sentence.count("zh")
        nj = sentence.count("nj")
        xh = sentence.count("xh")
        numerimi = ll + dh + rr + gj + sh + th + xh + zh + nj
        char1 = sentence.replace("ll", "")    #zevendsoj shkronjat si 'll' 'rr' 'th' etj me empty pasi qe snevojiten ne tekst me
        char2 = char1.replace("zh", "")
        char3 = char2.replace("dh", "")
        char4 = char3.replace("rr", "")
        char5 = char4.replace("th", "")
        char6 = char5.replace("nj", "")
        char7 = char6.replace("gj", "")
        char8 = char7.replace("sh", "")
        char9 = char8.replace("xh", "")

        for x in char9:                    #loop for ,per çdo karakter x ne fjali
            if x in ["b", "c", "ç", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r" , "s" , "t" , "v", "x", "z"]: #nese karakteri x qe gjendet ne fjali eshte njeri nga keto elemente te vektorit(array)
                numerimi = numerimi + 1 #numerimi rritet per nje
        return numerimi #dalja nga metoda me return, kthen numrin e bashktinglloreve kete rast



def GAME():
    stringu = "("       #stringu eshte nje string qe ka nje karakter
    for numbers in range(7):  #loop for, per 7 elemente, ne kete rast 7 numra pra do te perseritet loopa for 7 here
        stringu = stringu + str(random.randint(1,49)) + ","   # stringut i shtohet nga nje numer i rastesishem mes intervalit 1-49 si dhe nje presje ,kjo vazhdon 7 her per shkak te loopes for
    stringu = stringu[0:-2]  #prej stringut qe fitohet marrim prej karakterit te pare deri ne ate te parafundit me arsye qe te largojm presjen e fundit
    stringu = stringu + ")" #ja shtojm krejt nje fund nje kllap
    return stringu #rezultati


def FIBONACCI (fib): #funksioni fibonacci me argument fib
    fibNum1 = int(fib) #e kam bere fib si integer
    fibNum2 = fibNum1 + 1 #rritet per
    alpha = -1 #variabla
    beta = 1
    for i in range(0, fibNum2): #loop for,per i qe perseritet prej 0 deri ne sa eshte fibNum2 ,kaq here
        omega = alpha + beta #mbledhim
        alpha = beta
        beta = omega
    return beta #rezultati ,pra numri fibonacci i numrit qe jep klienti


def CONVERT(inWord):
    pjesaStringut = str(inWord[inWord.find(' ') + 1:]) #stringu qe merr pjesen e karaktereve nga hapsira e par deri ne fund
    opcioni = str(pjesaStringut[0:pjesaStringut.find(' ')]) #stringu qe merr nga stringu me lart nga karakteri i par deri tek hapesira
    x = float(pjesaStringut[pjesaStringut.find(' ') + 1:]) #mirret si float pjesa prej hapsires deri ne fund te stringut fillestar
    if opcioni == "KilowattToHorsepower": #nese nga mesazhi qe hyn nga klienti perkatesisht fjala e dyt eshte e njejte me njeren nga keto shprehjet ateher kryhet returni qe kane nen.Meqe rast kryhet metoda
        return x * 1.341
    elif opcioni == "HorsepowerToKilowatt":
        return x / 1.341
    elif opcioni == "DegreesToRadians":
        return x * 0.01745
    elif opcioni == "RadiansToDegrees":
        return x / 0.01745
    elif opcioni == "GallonsToLiters":
        return x * 3.785
    elif opcioni == "LitersToGallons":
        return x / 3.785


def CALCULATOR(inWord):
    parts = str(inWord[inWord.find(' ') + 1:]) #njesoj si tek metoda me lart fillimisht nga mesazhi qe hyn mirret nga hapsira e pare deri ne fund
    veprimi = str(parts[0:parts.find(' ')]) #pastaj zgjidhet nga stringu me lart nga fillimi deri tek hapesira
    part1 = str(parts[parts.find(' ') + 1:])#perseri nje string tjeter prej hapesires se par deri ne fund, por ne kete rast mirret i stringut me lart, jo mesazhit fillestar
    n1 = float(part1[0:part1.find(' ')]) #mirret si float pjesa prej karakterit te pare deri tek hapsira e stringut me siperm
    n2 = float(part1[part1.find(' ') + 1:]) #mirret si float pjesa prej hapsires deri ne fund te stringut te me siperm
    if veprimi == "Mbledhja":  #nese nga mesazhi qe hyn nga klienti perkatesisht fjala e dyt eshte e njejte me njeren nga keto shprehjet atehere kryhet returni qe kane nen.Meqe rast kryhet metoda
        return n1 + n2
    elif veprimi == "Zbritja":
        return n1 - n2
    elif veprimi == "Shumezimi":
        return n1 * n2
    elif veprimi == "Pjestimi":
        return n1 / n2
    elif veprimi == "Mbetja":
        return n1 % n2


def WEEKDAY(inWord):
    argumenti = str(inWord[inWord.find(' ') + 1:])
    dita = int(argumenti[0:argumenti.find('.')])
    argumenti2 = str(argumenti[argumenti.find('.') + 1:])
    muaji = int(argumenti2[0:argumenti2.find('.')])
    viti = int(argumenti2[argumenti2.find('.')+1:])
    arrays = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]  #numri i diteve pas qdo muaji
    java    = ['Diele',
              'Hene',                   #java si array ,perkatesisht ditet e javes si elemente
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

def clientthread(co): #metoda per threads
    while True: #derisa gjithmone eshte e vertet (sakte)
        inWord = connectionSocket.recv(128).decode('UTF-8') #pranimi prej klienti me 128 bytes i dekoduar mirret si nje variabel inWord


        if inWord == "IPADRESA":         #nese perputhet fjala e marr nga klienti shfaqet pergjigja perkatesist outWord si ne vijim
            outWord = "IP adresa juaj: " + str(socket.gethostbyname(socket.gethostname())) #ky funksion sherben per shfaqjen e ipadreses se bashku me pjesen tjeter te pergjigjes

        elif inWord == "NUMRIIPORTIT": #nese perputhet fjala e marr nga klienti shfaqet pergjigja perkatesist outWord si ne vijim
            outWord = "Numri i portit tuaj eshte: " + str(addr[1]) #shfaqet fjala e dyte nga funksioni addr ,perkatesisht nga ajo qe kthen ajo

        elif inWord[0:inWord.find(' ')] == "BASHKETINGELLORET": #nese fjala e pare e marr nga klienti eshte si ne vijim ,
            sentence = inWord[inWord.find(' ') + 1:] #ndersa fjala e dyte mirret si variabel , nga hapsira deri ne fund
            nrBashk = str(BASHKETINGELLORE(sentence)) #returnin e metodes me lart bashketingellore e bejme si string qe te mund ta lidhim me string tjeter (concatenated) ne Outword
            outWord = "Numri i bashketingelloreve nga fjala e kerkuar eshte: " + nrBashk +"!" #Pergjigja qe i shfaqet klientit

        elif inWord[0:inWord.find(' ')] == "PRINTIMI": ##nese fjala e pare e marr nga klienti eshte si ne vijim ,
            outWord = "Fjalia qe keni shkruar:" + inWord[inWord.find(' ') + 1:].strip() # shfaqet pergjigja tek klienti ashtu qe fjala e printuar ka hapsirat para dhe ne fund te eliminuara (nese ka kuptohet)
                                                                                                                  #eliminimi i hapsirave para dhe pas behet me strip()
        elif inWord == "EMRIIKOMPJUTERIT": #nese fjala marr nga klienti eshte si ne vijim ,
            outWord = "Emri i kompjuterit tuaj eshte: " + getpass.getuser() +"!" #pergjigja tek klienti, ku kemi shfrytzuar importimin e getpass si dhe funks getuser per marrjen e emrit te kompjuterit te klientit

        elif inWord == "KOHA": #nese fjala e pare e marr nga klienti eshte si ne vijim
            outWord = "Tani koha eshte: " + datetime.datetime.now().strftime(" %d.%m.%Y %H:%M:%S %p ") #pergjigja tek klienti , me funksionin marrim kohen e tashme te klientit dhe me strftime e kthejme ne string

        elif inWord == "LOJA": #nese fjala e marr nga klienti eshte si ne vijim
            outWord = "Shtate numrat e rastesishem nga rangu 1-49 jane:" + GAME()  #si pergjigje i shkon stringu i lidhur me rezultatin e metodes game()

        elif inWord[0:inWord.find(' ')] == "FIBONACCI": #nese fjala e pare e marr nga klienti eshte si ne vijim
            fib = str(inWord[inWord.find(' ') + 1:]) #ndersa fjala e dyte mirret si variabel , nga hapsira deri ne fund
            fibCipher = str(FIBONACCI(fib)) #returnin e metodes me lart fibonacci e bejme si string qe te mund ta lidhim me string tjeter (concatenated) ne Outword
            outWord = "Numri fibonacci i numrit qe keni shkruar eshte:" + fibCipher #Pergjigja qe i shfaqet klientit

        elif inWord[0:inWord.find(' ')] == "KONVERTIMI": #nese fjala e pare e marr nga klienti eshte si ne vijim
            con = str(CONVERT(inWord)) #returnin e metodes me lart convert e bejme si string qe te mund ta lidhim me string tjeter (concatenated) ne Outword
            outWord = "Rezultati eshte:" + con #Pergjigja qe i shfaqet klientit


        elif inWord[0:inWord.find(' ')] == "KALKULATORI": #nese fjala e pare e marr nga klienti eshte si ne vijim
            res = str(CALCULATOR(inWord)) #returnin e metodes me lart convert e bejme si string qe te mund ta lidhim me string tjeter (concatenated) ne Outword
            outWord = "Rezultati eshte: " + res #Pergjigja qe i shfaqet klientit


        elif inWord[0:inWord.find(' ')] == "DITA":  #nese fjala e pare e marr nga klienti eshte si ne vijim
            outWord = "Dita ishte(do te jete) e " + WEEKDAY(inWord) + "!"  #Pergjigja qe i shfaqet klientit

        else: #nese klienti nuk e shenon asnjeren nga fjalet me lart i shfaqet kjo pergjigje
            outWord = "Ju duhet te shenoni njeren nga fjalet/fjalit me lart!Falemnderit!"

        connectionSocket.send(str.encode(str(outWord))) #dergimi i pergjigjes se enkoduar ne klient


while 1:
    connectionSocket, addr = serverSocket.accept() #pranon nje lidhje (connection)
    print('Klienti u lidh ne serverin %s me portin %s' % addr) #Shfaqet pas lidhjes me nje klient
    start_new_thread(clientthread,(connectionSocket,)) #fillo threads
connectionSocket.close() #mbyllja