import socket

HOST = 'localhost'
PORT = 12000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srv = (HOST, PORT)

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
      "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
      "Miresevini ne Aplikacion                         \n"
      "Sherbimet qe i ofrojme mund ti shfrytzoni permes shkrimit te frazave ne vijim:                           \n")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
      "Kerkimi per Ip adresen tuaj permes : IPADRESA \n"
      "Kerkimi per numrin e portit permes : NUMRIIPORTIT\n"
      "Kerkimi per numerimin e bashketingelloreve : BASHKETINGELLORET(hapesire)tekst\n"
      "Kerkimi per oren,diten,muajin dhe vitin : KOHA\n"
      "Kerkimi per emrin tuaj te kompjuterit : EMRIIKOMPJUTERIT\n"
      "Luajtja e lojes behet permes : LOJA\n"
      "Gjetja e numrit fibonacci permes : FIBONACCI(hapesire)numer\n"
      "Konvertimin nga njesi te ndryshme mund ta beni : KONVERTIMI(hapesire)njesite(hapesire)sasia\n"
      "Kalkulartorin e thjesht mund ta perdoresh permes : KALKULATORI(hapesire)veprimi(hapesire)numri1(hapesire)numri2\n"
      "Per gjetjen e qfare dite e javes ka qene ne baz te dates qe jepni:DITA(hapesire)dita.muaji.viti\n"
      "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

var = input("Zgjedhja juaj per kerkim: ")
s.sendto(str.encode(var), srv)
r = s.recvfrom(128)
message = r[0].decode()
print(message)
s.close()