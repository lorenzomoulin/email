# -*- coding: utf-8 -*-
import sys
import smtplib

email = []
nome = []

with open(sys.argv[0]) as f :
    content = f.readlines()
content = [x.strip() for x in content] 

add_from = input("Digite o email remetente: ")
password = input("Digite a senha do email: ")

j=0
while j < len(content):
    email.append(content[j])
    nome.append(content[j+1])
    j+=2

j = 0
for i in range(1,int(len(content)/2)):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(add_from, password)
    
    
    msg = "Ola, " + str(nome[i]) + "!\n" + "Voce se inscreveu no Processo Seletivo 2017/3 da ERUS. Preciso que marque a entrevista neste link: https://doodle.com/poll/n53yhq27ycyxuvae" + "\n\nERUS - Equipe de Robotica da UFES"    
    assunto = "Processo Seletivo da ERUS"
    
    message = 'Subject: {}\n\n{}'.format(assunto, str(msg))
    server.sendmail(add_from, email[i], message)
    server.quit()
    
print (content)
