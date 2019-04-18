import socket #importimi soketave
serverName = 'localhost' #ipadresa
port = 12000 #porti
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverName, port)) #lidhja me nje ipadres dhe port tjeter

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
      "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
      "Miresevini ne Aplikacion                         \n"
      "Sherbimet qe i ofrojme mund ti shfrytzoni permes shkrimit te frazave ne vijim:                           \n")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
      "Kerkimi per Ip adresen tuaj permes : IPADRESA \n"
      "Kerkimi per numrin e portit permes : NUMRIIPORTIT\n"
      "Kerkimi per printimin perkatesisht kthimin e fjalise qe shkruani behet:PRINTIMI(hapesire)tekst\n"
      "Kerkimi per numerimin e bashketingelloreve : BASHKETINGELLORET(hapesire)tekst\n"
      "Kerkimi per oren,diten,muajin dhe vitin : KOHA\n"
      "Kerkimi per emrin tuaj te kompjuterit : EMRIIKOMPJUTERIT\n"
      "Luajtja e lojes behet permes : LOJA\n"
      "Gjetja e numrit fibonacci permes : FIBONACCI(hapesire)numer\n"
      "Konvertimin nga njesi te ndryshme mund ta beni : KONVERTIMI(hapesire)njesite(hapesire)sasia\n"
      "Kalkulartorin e thjesht mund ta perdoresh permes : KALKULATORI(hapesire)veprimi(hapesire)numri1(hapesire)numri2\n"
      "Per gjetjen e qfare dite e javes ka qene ne baz te dates qe jepni:DITA(hapesire)dita.muaji.viti\n"
      "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
#Printat qe sherbejn per shfaqje dhe permirsim te programit per klientin
while True:
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    var = input('Zgjedhja juaj per kerkim: ') #input per futjen e pergjigjes(kekreses) se klientit
    s.send((var.encode())) #dergon pergjigjen(kerkesen) ne server te enkodume
    r = s.recv(128).decode() #e pranon pergjigjen(kerkesen nga serberi te dekodume me 128 bytes
    print(r) #dhe printohet pergjigja(kerkesa e serverit

s.close()
