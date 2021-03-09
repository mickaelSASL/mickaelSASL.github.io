#! C:\laragon\bin\python\python-3.6.1\python.exe
# -*- coding: UTF-8 -*-

import cgi, cgitb
cgitb.enable()

# Ces 3 lignes semblent indispensables pour que les lettres accentuées
# soient prises en compte

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
###################################################################
# CODE HTML
print ("Content-type:text/html\r\n\r\n")
print('<!DOCTYPE html>')
print ('<html>')
print ('<head>')
print ('<title>Fisrt example</title>')
print ('''
      <meta charset="utf-8">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
''')
print ('</head>')
print ('<body>')

#ici débute le contenu <body>
print('<div class="container"><h1 class="alert alert-success"> Hello World ! Apache Web + Python </h1></div>')


#fin de la page

print ('</body>')
print ('</html>')
