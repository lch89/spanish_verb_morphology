#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from json_globals import *
from morphology import *
from spanish_irregulars import *

def loadJson(file_path):
	json_data = {}

	# if not file_path[-5:0]==".json":
	# 	file_path = "{}.json".format(file_path)

	with open(file_path,"r") as f:
		json_data = json.load(f)
		return json_data

	return json_data

valid_reference = loadJson(SPANISH_CONJ_NAME)
en_sp_inf = loadJson(EN_SP_INF_NAME)
sp_en_inf = loadJson(SP_EN_INF_NAME)
morph = Conjugator()
# morph.englishToSpanish("to dance", PRESENT, FIRST_PERSON_SINGULAR)

# def assertEquals(statement1, statement2):	
# 	assert  statement1==statement2, "{} and {} are not equal".format(statement1,statement2)

def assertEquals(word, tense, person):
	test_word = ""
	sp_word = ""

	if word in set(en_sp_inf.keys()):
		test_word = morph.englishToSpanish(word, tense, person)
		sp_word = en_sp_inf.get(word)
	elif word in set(sp_en_inf.keys()):
		test_word = morph.conjugateInfinitive(word, tense, person)
		sp_word = word
	else:
		print("\"{}\" cannot be translated!".format(word))
		return

	# test_word = morph.englishToSpanish(eng_word, tense, person)
	# sp_word = en_sp_inf.get(eng_word)
	# if not sp_word:
	# 	if eng_word in sp_en_inf.keys():
	# 		sp_word = eng_word
	# 	else:
	# 		print("\"{}\" cannot be traslated!".format(eng_word))
	
	correct_word = valid_reference[sp_word][tense][person]

	if test_word==correct_word:
		pass
	else:
		print("Incorrect test case: \"{}\", {}, {}".format(sp_word, tense, person))
		# print("Definition: \"{}\"".format(eng_word))
		print("Should be: \"{},\" was \"{}\"".format(correct_word,test_word))

	# print("---------------------------------------")

	# assert  statement1==statement2, "{} and {} are not equal".format(statement1,statement2)

def testVerb(verb, tense):
	assertEquals(verb, tense, FIRST_PERSON_SINGULAR)
	assertEquals(verb, tense, SECOND_PERSON_SINGULAR)
	assertEquals(verb, tense, THIRD_PERSON_SINGULAR)
	assertEquals(verb, tense, FIRST_PERSON_PLURAL)	
	assertEquals(verb, tense, SECOND_PERSON_PLURAL)
	assertEquals(verb, tense, THIRD_PERSON_PLURAL)

def testAll(tense):
	for word in valid_reference.keys():
		testVerb(word, tense)

if __name__ == "__main__":
	
	# testVerb("to dance", PRESENT)
	# testVerb("to eat", PRESENT)
	# testVerb("to admit, accept, allow, recognize", PRESENT)

	# testVerb("caber", PRESENT)
	# testVerb("conocer", PRESENT)
	# testVerb("poner", PRESENT)

	# testVerb("caber",PRESENT)
	# testVerb("caer",PRESENT)
	# testVerb("conocer",PRESENT)

	# testVerb("poner",PRESENT)
	# testVerb("componer",PRESENT)

	# testVerb("salir",PRESENT)
	# testVerb("traducir",PRESENT)
	# testVerb("traer",PRESENT)
	# testVerb("valer",PRESENT)

	# testVerb("ser", PRESENT)

	# testVerb("despertarse", PRESENT)	
	


	# testVerb("to think", PRESENT)
	# testVerb("to close, shut", PRESENT)
	# testVerb("to be able, can", PRESENT)
	# testVerb("to request, ask for", PRESENT)	
	# # testVerb("to recognize", PRESENT)
	# # testVerb("to choose, select, pick", PRESENT)
	# testVerb("to follow, continue", PRESENT)
	# testVerb("to build, construct", PRESENT)
	# # testVerb("ser")
	# # for(i=0;i<len([ie_boots]);i++):
	# # 	pass
	# for word in ie_boots:
	# 	testVerb(word, PRESENT)
	# 	print("--------------------")

	# for word in valid_reference.keys():
	# 	testVerb(word, PRESENT)
		# print("--------------------")

	testAll(PRESENT)

	# print("--------------------")

	# testVerb("sentir", PRETERITE)
	# testVerb("pedir", PRETERITE)

	# testVerb("sentir", PRETERITE)
	# testVerb("pedir", PRETERITE)

	# testVerb("reír", PRETERITE)
	# testVerb("sonreír", PRETERITE)
	# testVerb("dormir", PRETERITE)


	# print("--------------------")

	# testVerb("to dance", PRESENT_SUBJUNCTIVE)
	# testVerb("to eat", PRESENT_SUBJUNCTIVE)
	# testVerb("to admit, accept, allow, recognize", PRESENT_SUBJUNCTIVE)

	# print("--------------------")

	# testVerb("to dance", FUTURE_SUBJUNCTIVE)
	# testVerb("to eat", FUTURE_SUBJUNCTIVE)
	# testVerb("to admit, accept, allow, recognize", FUTURE_SUBJUNCTIVE)	


	# ue_boots
	# i_boots