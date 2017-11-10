# -*- coding: utf-8 -*-
#o usuario deve indicar o nome com "$name"

import sys
import smtplib
import getpass

email = []
nome = []

assunto = input("Digite o assunto: ")

with open(sys.argv[1]) as f:
	msg = f.readlines()

final = ""
for i in range(0, len(msg)-1) :
	final += str(msg[i])

with open(sys.argv[2]) as f :
    content = f.readlines()
content = [x.strip() for x in content] 

add_from = input("Digite o email remetente: ")
password = getpass.getpass()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(add_from, password)

j = 0

while j < len(content):
    email.append(content[j])
    nome.append(content[j+1])
    j+=2

for i in range(0,int(len(content)/2)):
    
    message = 'Subject: {}\n\n{}'.format(assunto, final.replace("$name", nome[i]))
    server.sendmail(add_from, email[i], message.encode('utf-8'))
server.quit()
