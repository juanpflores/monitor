#!/user/bin/python
# coding=utf-8

#===========================================================
#PRIMER PRYECTO DE SISTEMAS OPRATIVOS: Manejador de Procesos
#===========================================================

# @author Diego Barriga <umoqnier@gmail.com>
# @author Juan Pablo Flores <jp@temazcal.io>
# @date 27/03/2016


from threading import Semaphore, Thread
import os, threading, time

mut_impr = threading.Semaphore(1)
band = 0

# Definimos la funcion que nos dará a información del uso 
# de disco duro.
def uso_disco():
	'''Impresión de uso de disco'''
	global mut_impr
	mut_impr.acquire()
	print "*===========================USO DE DISCO===========================*"
	print " "
	os.system("du -h")
	mut_impr.release()

#Definimos la funcion que imprime el uso de los preocesos
def procesos():
	'''Impresión de Procesos'''
	global mut_impr
	mut_impr.acquire()
	print "*===========================PROCESOS===========================*"
	print " "
	os.system("ps -auf")
	mut_impr.release()

#Definimos la funcion que imprime el uso de memoria.
def uso_memoria():
	'''Impresión de Uso de Memoria'''
	global mut_impr
	mut_impr.acquire()
	print "*===========================MEMORIA===========================*"
	print " "
	os.system("free -h")
	os.system("cat /proc/meminfo")
	mut_impr.release()


def procesos_tree():
	'''Arbol de Procesos'''
	global mut_impr
	mut_impr.acquire()
	print "*===========================PROCESOS [ARBOL]===========================*"
	print " "
	os.system("pstree")
	mut_impr.release()

def logins():
	'''Imprimir Logins'''
	global mut_impr
	mut_impr.acquire()
	print "*===========================LOGINS===========================*"
	print " "
	os.system("last")
	mut_impr.release()

def cpu_info():
	'''Informacion de CPU'''
	global mut_impr
	mut_impr.acquire()
	print "*===========================INFORMACION CPU===========================*"
	print " "
	os.system("cat /proc/cpuinfo")
	mut_impr.release()

def interrupciones():
	'''Impresion de Interrupciones de CPU'''
	global mut_impr
	mut_impr.acquire()
	print "*===========================INTERRUPCIONES DEL CPU===========================*"
	print " "
	os.system("cat /proc/interrupts")
	mut_impr.release()

def limpia_pantalla():
	'''Limpiar Pantalla'''
	global mut_impr
	mut_impr.acquire()
	os.system("clear")
	mut_impr.release()

def command(var):
	'''Lanzador de Hilos'''
	global band 
	if var == "all":
		hilo()
	elif var == "disk":
		thr = threading.Thread(target = uso_disco)
		thr.start()
	elif var == "memory":
		thr = threading.Thread(target = uso_memoria)
		thr.start()
	elif var == "process":
		thr = threading.Thread(target = procesos)
		thr.start()
	elif var == "protree":
		thr = threading.Thread(target = procesos_tree)
		thr.start()
	elif var == "logins":
		thr = threading.Thread(target = logins)
		thr.start()
	elif var == "cpuinfo":
		thr = threading.Thread(target = cpu_info)
		thr.start()
	elif var == "interrupts":
		thr = threading.Thread(target = interrupciones)
		thr.start()
	elif var == "clear":
		thr = threading.Thread(target = limpia_pantalla)
		thr.start()
	elif var == "help all":
		print "-----------------------------|all|-----------------------------"
		print "Desliega toda la informacion del sistema disponible"
		print " "
	elif var == "help disk":
		print "-----------------------------|disk|-----------------------------"
		print "Desliega el uso de disco por directorio, incluyendo los subdirecctorios del mismo."
		print " "
	elif var == "help memory":
		print "-----------------------------|memory|-----------------------------"
		print "Muestra informacion sobre la memoria de la maquina. Incluye memoria RAM, swap y buffers usados por el kernel. Ademas despliega el contenido del archivo /proc/meminfo"
		print " "
	elif var == "help process":
		print "-----------------------------|proces|-----------------------------"
		print "Muestra los procesos que estan corriendo en ese momento con informacion especifica de cada uno."
		print " "
	elif var == "help protree":
		print "-----------------------------|protre|-----------------------------"
		print "Despliega lo procesos que estan corriendo en ese momento en formato de arbol."
		print " "
	elif var == "help logins":
		print "-----------------------------|logins|-----------------------------"
		print "Imprime los logins del sistema."
		print " "
	elif var == "help cpuinfo":
		print "-----------------------------|cpuinfo|-----------------------------"
		print "Imprime la informacion de cada cpu existente en el sistema. Funciona gracias al archivo /proc/cpuinfo"
		print " "
	elif var == "help interrupts":
		print "-----------------------------|interrupts|-----------------------------"
		print "Imprime las interrupciones a los cpu's. Funciona gracias al archivo /proc/interrupts"
		print " "
	elif var == "help clear":
		print "-----------------------------|clear|-----------------------------"
		print "Limpia la pantalla."
		print " "
	elif var == "help help":
		print "-----------------------------|help|-----------------------------"
		print "Comando para desplegar informacion sobre los comandos."
		print " "
	elif var == "help exit":
		print "-----------------------------|exit|-----------------------------"
		print "Salida del programa."
		print " "
	elif var == "exit":
		print """ ____________________________
< Developed by Ptolomeo Team >
 ----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||"""
		band = 1
	else:
		print "Invalid command..."
	
#Definimos una fucnion para que asigne hilos a las funciones.
def hilo():
	'''Creación de Hilos'''
	thr0 = threading.Thread(target = uso_disco)
	thr0.start()
	thr1 = threading.Thread(target = procesos)
	thr1.start()
	thr2 = threading.Thread(target = uso_memoria)
	thr2.start()
	thr3 = threading.Thread(target = procesos_tree)
	thr3.start()
	thr4 = threading.Thread(target = logins)
	thr4.start()
	thr5 = threading.Thread(target = cpu_info)
	thr5.start()
	thr6 = threading.Thread(target = interrupciones)

def shell():
	'''Funciones en Shell'''
	global var, band, mut_impr
	os.system("clear")
	while band == 0:
		time.sleep(.1)
		print "comands: all, memory, process, disk, protree, logins, cpuinfo, interrupts, clear, help <comand>, exit"
		var = raw_input("user@machine$ ")
		command(var)
	mut_impr.release()

shell()


