import email
from tkinter.ttk import *
from  tkinter  import *
from tkinter import scrolledtext
from pandas import *
from tkcalendar import*
from tkinter import filedialog as dlg
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from tkinter import messagebox
from tkinter import ttk
from tkinter import Entry
import tkinter  as tk
from tkcalendar import DateEntry
from mysql.connector import Error
from service.LoginService import LoginService
from datetime import date, datetime
import csv
#from tkPDFViewer import tkPDFViewer as pdf 
#import mysql.connector
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import 
#import matplotlib.pyplot as plt
#import locale
from entity.Usuariopc import Usuario
import threading
import time
import pdfkit
import win32print
import win32com.client
import win32api
import tempfile
import requests
from UI import limpaWidget
import subprocess
import os
from  Leitura import Leitura
from setuptools import setup, find_packages
#TABELA DO MYSQL USADA CAB3//\\    
#con = mysql.connector.connect(host='127.0.0.1', database='ez-sys', user='root', password='q9w8e7#MTB')
#con = mysql.connector.connect(host='127.0.0.1', database='ezsys', user='root', password='q9w8e7#MTB')
usuarioLogado=None
janlogin = Tk()
janlogin.title("EZ-ADM")
janlogin.geometry("1200x800+250+50")
janlogin.configure(background="White")
janlogin.resizable(width=False, height=False)
janlogin.attributes("-alpha", 1.1)



logo = PhotoImage(file='Resource\logo\Ezipa.gif')

logo2 = PhotoImage(file='Resource\logo\Ezipanovo.gif')

logo3 = PhotoImage(file='Resource\logo\Logo teste2.png')

img=PhotoImage(file='Resource\logo\EzipaBG.gif')
img=img.subsample(1,0)

janlogin.iconbitmap("Resource\Adminsitrativo\Icone.ico")


topframe = Frame(janlogin, width=9999, height=135, bg="#0F4F21", relief="raise")
topframe.pack(side=TOP,fill = 'both', expand = True)
bottomframe = Frame(janlogin, width=9999, height=665,bg="white", relief="raise")
bottomframe.pack(side=BOTTOM,fill = 'both', expand = True)
LogoLabel = Label(topframe, image=logo, bg="#0F4F21")
LogoLabel.place(x=1040, y=0)
LogoLabel = Label(topframe, image=logo3, bg="#0F4F21")
LogoLabel.place(x=0, y=0)
UserLabel = Label(bottomframe, text="Usuário", font=("Calibri",15), bg="white", fg="black" )
UserLabel.place(x=330,y=300)
UserEntry = ttk.Entry(bottomframe, width=25)
UserEntry.bind("<KeyPress>", lambda e: PassEntry.focus() if e.char == '\r' else None) 
UserEntry.place(x=410,y=305)
PassLabel = Label(bottomframe, text="Senha", font=("Calibri",15), bg="white", fg="black")
PassLabel.place(x= 610,y=300)
PassEntry = ttk.Entry(bottomframe, width=25, show="*")
PassEntry.bind("<KeyPress>", lambda e: Entrar() if e.char == '\r' else None)
PassEntry.place(x=680,y=305)
ModuloLabel = Label(topframe, text="Módulo: Administrativo", font=("Calibri",12), bg="#0F4F21", fg="White")
ModuloLabel.place(x= 500 ,y=10)    


def Entrar():
   nome = UserEntry.get()  
   senha = PassEntry.get()  
   loginService = LoginService()
   usuarioLogado = loginService.realizarLoginComUsuarioESenha(nome, senha)
   #adminitrativomodule=adminitrativo
   #financeiromodule=financeiro
   #pcpmodule=pcp
   #comprasmodule=compras
   #vendasmodule=vendas
   #dpmodule=dp
   
   
   #vendaService = VendaService()
   #vendaService.gerarTabela()
   #vendaService.gerarRelatorioExcel()
   #usuarioLogado = Usuario('Teste', 'teste')   
   if usuarioLogado!= False :
         
        messagebox.showinfo('Login', 'Logado com Sucesso')
       
   else:
        messagebox.showerror('Erro','verifique as credenciais de Login e senha')
        return
   
   
   
   
   janlogin.mainloop()