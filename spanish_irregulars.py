#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Tilde n just in case = ñ
# Thanks me =3

vowels = set(["a","e","i","o","u","á","é","í","ó","ú","ü"])
consonants = set(["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ",  "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"])

to_accent = {"a":"á", "e":"é", "i":"í", "o":"ó", "u":"ú"}
un_accent = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u"}

# boot_verbs = set()

######### PRESENT TENSE CASES #########

present_irreg = set([
	"ser",
	"estar",
	"ir",
	"haber",
	])

e_ie_boots = set([
	"pensar",
	"cerrar",
	"calentar",
	"comenzar",
	"pensar",
	"perder",
	"gobernar",
	"negar",
	"quebrar",
	"querer",
	"herir",
	"entender",
	"encender",
	"despertar",
	"despertarse",
	"defender",
	"confesar",
	"mentir",
	"preferir",
	"sentir",
	"acertar",
	"atender",
	"atravesar",
	"calentar",
	"cerrar",
	"comenzar",
	"confesar",
	"helar",
	"defender",
	"descender",
	"despertarse",
	"divertirse",
	"empezar",
	"encender",
	"encerrar",
	"entender",
	"fregar",
	"gobernar",
	"mentir",
	"negar",
	"nevar",
	"pensar",
	"perder",
	"preferir",
	"recomendar",
	"remendar",
	"sentar",
	"sentarse",
	"sentir",
	"sugerir",
	"tener",
	"obtener",
	"tropezar",
	"venir",
	"regar",
	"presentir",
	"merendar",
])

i_ie_boots = set([
	"adquirir",
	"inquirir",	
])

o_ue_boots = set([
	"poder",
	"llover",
	"contar",
	"almorzar",
	"devolver",
	"envolver",
	"volver",
	"encontrar",
	"llover",
	"morder",
	"mover",
	"oler",
	"poder",
	"volar",
	"probar",
	"recordar",
	"soñar",
	"sonar",
	"dormir",
	"morir",
	"torcer",
	"rogar",
	"resolver",
	"soler",
])

i_boots = set([
	"pedir",
	"perseguir",
	"reír",
	"repetir",
	"vestir",
	"seguir",
	"servir",
	"sonreír",
	# "construir",
	"destruir",
	"concluir",
	"medir",
	"diluir",
	"teñir",
	"reñir"
	"regir",
])

u_ue_boots = set([
	"jugar",
])

go_verbs = set([
	"hacer",
	"decir",
	"predecir",
	"satisfacer",
	"asir",
	"salir",
	"oír",
	"tener",
	"poner",
	"valer",
])

######### PRETERITE TENSE CASES #########

preterite_irreg = set([
	"ser",
	"dar",
	"ir",
	"ver",
	])

i_soles = set(["sentir", "pedir", "reír", "sonreír"])

u_soles = set(["dormir"])

######### FUTURE TENSE CASES #########

future_irreg = set([
	"decir",
	"hacer"
	"predecir",
	"rehacer"
	])
