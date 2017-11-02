# -*- coding: utf-8 -*-
import smtplib
import time
from tkinter import *


n = int(input("Digite o numero de emails a enviar: "))
j=0

email = [None] * n
nome = [None] * n

while j < n:
    email[j] = input("Digite o email da pessoa: ")
    nome[j] = input("Digite o nome da pessoa: ")
    j+=1

j = 0
while j < len(email):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('add_from', 'password')    
    msg = "Ola, " + nome[j] + "!\n" + "Voce se inscreveu no Processo Seletivo 2017/3 da ERUS. Preciso que marque a entrevista neste link: https://doodle.com/poll/n53yhq27ycyxuvae" + "\n\nERUS - Equipe de Robotica da UFES"    
    assunto = "Processo Seletivo da ERUS"
    
    message = 'Subject: {}\n\n{}'.format(assunto, msg)
    server.sendmail('add_from', email[j], message)
    server.quit()
    j+=1
