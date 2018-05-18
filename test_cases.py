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
		# print("Correct, got: \"{},\"".format(test_word))
		return 1
	else:
		# print("Incorrect test case: \"{}\", {}, {}".format(sp_word, tense, person))
		# # print("Definition: \"{}\"".format(eng_word))
		# print("Should be: \"{},\" was \"{}\"".format(correct_word,test_word))

		return 0

	# print("---------------------------------------")

	# assert  statement1==statement2, "{} and {} are not equal".format(statement1,statement2)

def testVerb(verb, tense):
	correct_cases = 0 
	correct_cases += assertEquals(verb, tense, FIRST_PERSON_SINGULAR)
	correct_cases += assertEquals(verb, tense, SECOND_PERSON_SINGULAR)
	correct_cases += assertEquals(verb, tense, THIRD_PERSON_SINGULAR)
	correct_cases += assertEquals(verb, tense, FIRST_PERSON_PLURAL)	
	correct_cases += assertEquals(verb, tense, SECOND_PERSON_PLURAL)
	correct_cases += assertEquals(verb, tense, THIRD_PERSON_PLURAL)

	# assertEquals(verb, tense, FIRST_PERSON_SINGULAR)
	# assertEquals(verb, tense, SECOND_PERSON_SINGULAR)
	# assertEquals(verb, tense, THIRD_PERSON_SINGULAR)
	# assertEquals(verb, tense, FIRST_PERSON_PLURAL)	
	# assertEquals(verb, tense, SECOND_PERSON_PLURAL)
	# assertEquals(verb, tense, THIRD_PERSON_PLURAL)

	return correct_cases

def testAll(tense):
	total_correct = 0
	total = 0

	for word in valid_reference.keys():
		total+=6
		total_correct += testVerb(word, tense)
		# testVerb(word, tense)

	print("Total correct cases for {}: {}/{}".format(tense, total_correct,total))


def createTable(tense):

	with open(tense+"_Table.html","w") as f:
		html_string = ""

		html_string += "<!DOCTYPE html> \n"

		html_string += "<html> \n"

		html_string += "\t <head> \n"

		html_string += "<h1 style='text-align: center;'>Conjugated {} Tense Verbs</h1>\n\n".format(tense)

		html_string += "\t \t <style>table, th, td { border: 1px solid black; border-collapse: collapse;} </style>"

		html_string += "\t  </head> \n"

		html_string += "\t <body> \n"
		
		html_string += "\t \t <table style='border: 1px solid black;'> \n"

		# html_string += "\t \t \t <tr> \n"
		
		
		# html_string += "\t \t \t \t <th>"	

		# html_string += "Conjugated {} Verbs".format(tense)

		# html_string += "</th> \n"
		# html_string += "\t \t \t </tr> \n"
		
		html_string += "\t \t \t <tr> \n"
		html_string += "\t \t \t \t <th>"
		html_string += "Infinitive" 
		html_string += "</th> \n"
		for person in en_sp_person.keys():
			html_string += "\t \t \t \t <th>"	

			formatted_person = person.replace("_", " ")
			html_string += formatted_person.title()

			html_string += "</th> \n"
		html_string += "\t \t \t </tr> \n"

		html_string += "\n \n "
				
		for verb in valid_reference.keys():
			html_string += "\t \t \t <tr> \n"

			html_string += "\t \t \t \t <td>"
			html_string += verb
			html_string += "\t \t \t \t </td>"

			for person in en_sp_person.keys():
				# html_string += "\t \t \t \t <td>"

				is_correct = assertEquals(verb, tense, person)
				
				if is_correct:
					html_string += "\t \t \t \t <td>"
				else:
					html_string += "\t \t \t \t <td style='background-color: #FFCCCC;'>"
				
				html_string += morph.conjugateInfinitive(verb, tense, person)

				if not is_correct:
					html_string += "<br> <b>{}</b>".format(valid_reference[verb][tense][person])
				
				html_string += "\t \t \t \t </td> \n"

			html_string += "\t \t \t </tr> \n"

		html_string += "\t \t </table> \n"
		html_string += "\t </body> \n"
		html_string += "</html> \n"
		
		f.write(html_string)
	

if __name__ == "__main__":

	testAll(PRESENT)
	testAll(PRETERITE)
	testAll(FUTURE)
	testAll(CONDITIONAL)
	testAll(IMPERFECT)
	testAll(PRESENT_PROGRESSIVE)
	testAll(PRESENT_SUBJUNCTIVE)
	testAll(FUTURE_SUBJUNCTIVE)	

	# createTable(PRESENT)
	# print(PRESENT+" done")
	# createTable(PRETERITE)
	# print(PRETERITE+" done")
	# createTable(FUTURE)
	# print(FUTURE+" done")
	# createTable(CONDITIONAL)
	# print(CONDITIONAL+" done")
	# createTable(IMPERFECT)
	# print(IMPERFECT+" done")
	# createTable(PRESENT_PROGRESSIVE)
	# print(PRESENT_PROGRESSIVE+" done")
	# createTable(PRESENT_SUBJUNCTIVE)
	# print(PRESENT_SUBJUNCTIVE+" done")
	# createTable(FUTURE_SUBJUNCTIVE)	
	# print(FUTURE_SUBJUNCTIVE+" done")