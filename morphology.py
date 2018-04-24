#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from json_globals import *
from spanish_irregulars import *
# from test import * #TODO: Turn into JSON parsing specific things

# SPANISH_CONJ_NAME = "Spanish_Conjugations.json"
# SP_EN_INF_NAME = "Spanish_to_English_Infinitives.json"
# EN_SP_INF_NAME = "English_to_Spanish_Infinitives.json"

# en_sp_tenses = {"Present" : "Presente", "Preterite" : "Pretérito", "Future" : "Futuro", "Conditional" : "Condicional", "Imperfect" : "Imperfecto", "Present Progressive" : "Presente progresivo", "Perfect Past" : "Pretérito perfecto", "Perfect Present" : "Pluscuamperfecto", "Perfect Future" : "Futuro perfecto", "Conditional Perfect" : "Condicional perfecto", "Preterite (Archaic)" : "Pretérito anterior", "Present Subjunctive" : "Subjuntivo presente", "Imperfect Subjunctive -RA" : "Subjuntivo imperfecto -RA", "Imperfect Subjunctive -SE" : "Subjuntivo imperfecto -SE", "Future Subjunctive" : "Subjuntivo futuro", "Past Perfect Subjunctive" : "Subjuntivo pretérito perfecto", "Pluperfect Subjunctive -RA" : "Subjuntivo pluscuamperfecto -RA", "Pluperfect Subjunctive -SE" : "Subjuntivo pluscuamperfecto -SE", "Future Perfect Subjunctive" : "Subjuntivo futuro perfecto", "Imperative Affirmative" : "Imperativo positivo", "Imperative Negative" : "Imperativo negativo"}

# sp_en_tenses = {"Presente" : "Present", "Pretérito" : "Preterite", "Futuro" : "Future", "Condicional" : "Conditional", "Imperfecto" : "Imperfect", "Presente progresivo" : "Present Progressive", "Pretérito perfecto" : "Perfect Past", "Pluscuamperfecto" : "Perfect Present", "Futuro perfecto" : "Perfect Future", "Condicional perfecto" : "Conditional Perfect", "Pretérito anterior" : "Preterite (Archaic)", "Subjuntivo presente" : "Present Subjunctive", "Subjuntivo imperfecto -RA" : "Imperfect Subjunctive -RA", "Subjuntivo imperfecto -SE" : "Imperfect Subjunctive -SE", "Subjuntivo futuro" : "Future Subjunctive", "Subjuntivo pretérito perfecto" : "Past Perfect Subjunctive", "Subjuntivo pluscuamperfecto -RA" : "Pluperfect Subjunctive -RA", "Subjuntivo pluscuamperfecto -SE" : "Pluperfect Subjunctive -SE", "Subjuntivo futuro perfecto" : "Future Perfect Subjunctive", "Imperativo positivo" : "Imperative Affirmative", "Imperativo negativo" : "Imperative Negative"}

# en_sp_person = {FIRST_PERSON_SINGULAR : "yo", SECOND_PERSON_SINGULAR : "tu", THIRD_PERSON_SINGULAR : "el", FIRST_PERSON_PLURAL : "ns", SECOND_PERSON_PLURAL : "vs", THIRD_PERSON_PLURAL : "ellos"}

# sp_en_person = {"yo" : FIRST_PERSON_SINGULAR, "tu" : SECOND_PERSON_SINGULAR, "el" : THIRD_PERSON_SINGULAR, "ns" : FIRST_PERSON_PLURAL, "vs" : SECOND_PERSON_PLURAL, "ellos" : THIRD_PERSON_PLURAL}

# FIRST_PERSON_SINGULAR = "FIRST_PERSON_SINGULAR"
# SECOND_PERSON_SINGULAR = "SECOND_PERSON_SINGULAR"
# THIRD_PERSON_SINGULAR = "THIRD_PERSON_SINGULAR"
# FIRST_PERSON_PLURAL = "FIRST_PERSON_PLURAL"
# SECOND_PERSON_PLURAL = "SECOND_PERSON_PLURAL"
# THIRD_PERSON_PLURAL = "THIRD_PERSON_PLURAL"

class Conjugator():

	def __init__(self):
		#TODO: Decide if we need this field for GUI processing
		self.conjugations = self.loadJson(SPANISH_CONJ_NAME) # For cross-checking
		self.sp_en_inf = self.loadJson(SP_EN_INF_NAME)
		self.en_sp_inf = self.loadJson(EN_SP_INF_NAME)
		self.morphology = Morphology()
		self.phonology = Phonology()

	def getTenses(self):
		# self.conjugations.values().keys()
		return set("Present", "Preterite", "Future", "Conditional", "Imperfect", "Present Progressive", "Perfect Past", "Perfect Present", "Perfect Future", "Conditional Perfect", "Preterite (Archaic)", "Present Subjunctive", "Imperfect Subjunctive -RA", "Imperfect Subjunctive -SE", "Future Subjunctive", "Past Perfect Subjunctive", "Pluperfect Subjunctive", "Pluperfect Subjunctive", "Future Perfect Subjunctive", "Imperative Affirmative", "Imperative Negative")

	def getPersons(self):
		return set(FIRST_PERSON_SINGULAR, SECOND_PERSON_SINGULAR, THIRD_PERSON_SINGULAR, FIRST_PERSON_PLURAL, SECOND_PERSON_PLURAL, THIRD_PERSON_PLURAL)

	def loadJson(self, file_path):
		json_data = {}

		# if not file_path[-5:0]==".json":
		# 	file_path = "{}.json".format(file_path)

		with open(file_path,"r") as f:
			json_data = json.load(f)
			return json_data

		return json_data
	
	# def englishToSpanish(self, eng_word, tense=None, person=None):
	def englishToSpanish(self, eng_word, tense, person):
		"""Given"""
		verb = self.en_sp_inf.get(eng_word, "")
		print(verb)
		morph_verb = self.morphology.conjugate(verb, tense, person)
		self.phonology.phonology(morph_verb, tense, person)
		phon_verb = morph_verb

		print(phon_verb)
		print("---")

		return phon_verb

		#Morphology application

		#Phonology application

	# def morphology(self):
	#   pass

	# def phonology(self):
	#   pass


#Arbitrary sectioning of morphology for sake of keeping track of rules
class Morphology():
	def __init__(self):
		pass

	def morphology(self, verb, tense, person):
		pass

	def conjugate(self, verb, tense, person):
		"""Given the verb ending, tense, and person, conjugate the verb"""
		conjugate_verb = verb
		stem = verb[:-2]
		ending = verb[-2:]

		#Check for tense, then person, then ending
		if tense==PRESENT:
			print("Present tense")
			if person==FIRST_PERSON_SINGULAR:
				conjugate_verb = stem+"o"
			elif person==SECOND_PERSON_SINGULAR:
				if ending==AR_ENDING:
					conjugate_verb = stem+"as"
				elif ending==ER_ENDING:
					conjugate_verb = stem+"es"
				elif ending==IR_ENDING:
					conjugate_verb = stem+"es"
			elif person==THIRD_PERSON_SINGULAR:
				if ending==AR_ENDING:
					conjugate_verb = stem+"a"
				elif ending==ER_ENDING:
					conjugate_verb = stem+"e"
				elif ending==IR_ENDING:
					conjugate_verb = stem+"e"
			elif person==FIRST_PERSON_PLURAL:
				if ending==AR_ENDING:
					conjugate_verb = stem+"an"
				elif ending==ER_ENDING:
					conjugate_verb = stem+"emos"
				elif ending==IR_ENDING:
					conjugate_verb = stem+"imos"
			elif person==SECOND_PERSON_PLURAL:
				if ending==AR_ENDING:
					conjugate_verb = stem+"áis"
				elif ending==ER_ENDING:
					conjugate_verb = stem+"éis"
				elif ending==IR_ENDING:
					conjugate_verb = stem+"ís"
			elif person==THIRD_PERSON_PLURAL:
				if ending==AR_ENDING:
					conjugate_verb = stem+"an"
				elif ending==ER_ENDING:
					conjugate_verb = stem+"en"
				elif ending==IR_ENDING:
					conjugate_verb = stem+"en"
		elif tense==PRETERITE:
			print("Preterite")
			if person==FIRST_PERSON_SINGULAR:
				if ending==AR_ENDING:
					conjugate_verb = stem+"é"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = stem+"í"
			elif person==SECOND_PERSON_SINGULAR:
				if ending==AR_ENDING:
					conjugate_verb = stem+"aste"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = stem+"iste"
			elif person==THIRD_PERSON_SINGULAR:
				if ending==AR_ENDING:
					conjugate_verb = stem+"ó"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = stem+"ió"
			elif person==FIRST_PERSON_PLURAL:
				if ending==AR_ENDING:
					conjugate_verb = stem+"amos"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = stem+"imos"
			elif person==SECOND_PERSON_PLURAL:
				if ending==AR_ENDING:
					conjugate_verb = stem+"asteis"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = stem+"isteis"
			elif person==THIRD_PERSON_PLURAL:
				if ending==AR_ENDING:
					conjugate_verb = stem+"aron"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = stem+"ieron"
		elif tense==FUTURE:
			print("Future")
			if person==FIRST_PERSON_SINGULAR:
				conjugate_verb = verb+"é"
			elif person==SECOND_PERSON_SINGULAR:
				conjugate_verb = verb+"ás"
			elif person==THIRD_PERSON_SINGULAR:
				conjugate_verb = verb+"á"
			elif person==FIRST_PERSON_PLURAL:
				conjugate_verb = verb+"emos"
			elif person==SECOND_PERSON_PLURAL:
				conjugate_verb = verb+"éis"
			elif person==THIRD_PERSON_PLURAL:
				conjugate_verb = verb+"án"
		elif tense==CONDITIONAL:
			print("{}".format("Conditional"))
			if person==FIRST_PERSON_SINGULAR:
				conjugate_verb = verb+"ía"
			elif person==SECOND_PERSON_SINGULAR:
				conjugate_verb = verb+"ías"
			elif person==THIRD_PERSON_SINGULAR:
				conjugate_verb = verb+"ía"
			elif person==FIRST_PERSON_PLURAL:
				conjugate_verb = verb+"íamos"
			elif person==SECOND_PERSON_PLURAL:
				conjugate_verb = verb+"íais"
			elif person==THIRD_PERSON_PLURAL:
				conjugate_verb = verb+"ían"
		elif tense==IMPERFECT:
			print("{}".format("Imperfect"))
			if person==FIRST_PERSON_SINGULAR:
				if ending==AR_ENDING:
					conjugate_verb = stem+"aba"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = stem+"ía"
			elif person==SECOND_PERSON_SINGULAR:
				if ending==AR_ENDING:
					conjugate_verb = stem+"abas"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = stem+"ías"
			elif person==THIRD_PERSON_SINGULAR:
				if ending==AR_ENDING:
					conjugate_verb = stem+"aba"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = stem+"ía"
			elif person==FIRST_PERSON_PLURAL:
				if ending==AR_ENDING:
					conjugate_verb = stem+"ábamos"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = stem+"íamos"
			elif person==SECOND_PERSON_PLURAL:
				if ending==AR_ENDING:
					conjugate_verb = stem+"abais"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = stem+"íais"
			elif person==THIRD_PERSON_PLURAL:
				if ending==AR_ENDING:
					conjugate_verb = stem+"aban"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = stem+"ían"
		elif tense==PRESENT_PROGRESSIVE:
			print("TODO: Implement {}".format("Present Progressive"))
		elif tense==PERFECT_PAST:
			print("TODO: Implement {}".format("Perfect Past"))
		elif tense==PERFECT_PRESENT:
			print("TODO: Implement {}".format("Perfect Present"))
		elif tense==PERFECT_FUTURE:
			print("TODO: Implement {}".format("Perfect Future"))
		elif tense==CONDITIONAL_PERFECT:
			print("TODO: Implement {}".format("Conditional Perfect"))
		elif tense==PRETERITE_ARCHAIC:
			print("TODO: Implement {}".format("Preterite (Archaic)"))
		elif tense==PRESENT_SUBJUNCTIVE:
			print("{}".format("Present Subjunctive"))
			subjunctive_stem = conjugate(verb, "Present", FIRST_PERSON_SINGULAR)[:-1]
			if person==FIRST_PERSON_SINGULAR:
				if ending==AR_ENDING:
					conjugate_verb = subjunctive_stem+"e"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = subjunctive_stem+"a"
			elif person==SECOND_PERSON_SINGULAR:
				if ending==AR_ENDING:
					conjugate_verb = subjunctive_stem+"es"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = subjunctive_stem+"as"
			elif person==THIRD_PERSON_SINGULAR:
				if ending==AR_ENDING:
					conjugate_verb = subjunctive_stem+"e"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = subjunctive_stem+"a"
			elif person==FIRST_PERSON_PLURAL:
				if ending==AR_ENDING:
					conjugate_verb = subjunctive_stem+"emos"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = subjunctive_stem+"amos"
			elif person==SECOND_PERSON_PLURAL:
				if ending==AR_ENDING:
					conjugate_verb = subjunctive_stem+"éis"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = subjunctive_stem+"áis"
			elif person==THIRD_PERSON_PLURAL:
				if ending==AR_ENDING:
					conjugate_verb = subjunctive_stem+"en"
				elif ending==ER_ENDING or ending==IR_ENDING:
					conjugate_verb = subjunctive_stem+"an"
		elif tense==IMPERFECT_SUBJUNCTIVE_RA:
			print("TODO: Implement {}".format("Imperfect Subjunctive -RA"))
		elif tense==IMPERFECT_SUBJUNCTIVE_SE:
			print("TODO: Implement {}".format("Imperfect Subjunctive -SE"))
		elif tense==FUTURE_SUBJUNCTIVE:
			print("TODO: Implement {}".format("Future Subjunctive"))
		elif tense==PAST_PERFECT_SUBJUNCTIVE:
			print("TODO: Implement {}".format("Past Perfect Subjunctive"))
		elif tense==PLUPERFECT_SUBJUNCTIVE:
			print("TODO: Implement {}".format("Pluperfect Subjunctive"))
		elif tense==PLUPERFECT_SUBJUNCTIVE:
			print("TODO: Implement {}".format("Pluperfect Subjunctive"))
		elif tense==FUTURE_PERFECT_SUBJUNCTIVE:
			print("TODO: Implement {}".format("Future Perfect Subjunctive"))
		elif tense==IMPERATIVE_AFFIRMATIVE:
			print("TODO: Implement {}".format("Imperative Affirmative"))
		elif tense==IMPERATIVE_NEGATIVE:
			print("TODO: Implement {}".format("Imperative Negative"))

		return conjugate_verb


#Arbitrary sectioning of phonology for sake of keeping track of rules
class Phonology():
	def __init__(self):
		pass

	def phonology(self, morph_verb, tense, person):
		pass

if __name__ == "__main__":
	test = Conjugator()
	test.englishToSpanish("to dance", PRESENT, FIRST_PERSON_SINGULAR)
	test.englishToSpanish("to dance", PRESENT, SECOND_PERSON_SINGULAR)
	test.englishToSpanish("to dance", PRESENT, THIRD_PERSON_SINGULAR)
	test.englishToSpanish("to dance", PRESENT, FIRST_PERSON_PLURAL)
	test.englishToSpanish("to dance", PRESENT, SECOND_PERSON_PLURAL)
	test.englishToSpanish("to dance", PRESENT, THIRD_PERSON_PLURAL)
	print("---------------")
	test.englishToSpanish("to eat", PRESENT, FIRST_PERSON_SINGULAR)
	test.englishToSpanish("to eat", PRESENT, SECOND_PERSON_SINGULAR)
	test.englishToSpanish("to eat", PRESENT, THIRD_PERSON_SINGULAR)
	test.englishToSpanish("to eat", PRESENT, FIRST_PERSON_PLURAL)
	test.englishToSpanish("to eat", PRESENT, SECOND_PERSON_PLURAL)
	test.englishToSpanish("to eat", PRESENT, THIRD_PERSON_PLURAL)
	print("---------------")
	test.englishToSpanish("to admit, accept, allow, recognize", PRESENT, FIRST_PERSON_SINGULAR)
	test.englishToSpanish("to admit, accept, allow, recognize", PRESENT, SECOND_PERSON_SINGULAR)
	test.englishToSpanish("to admit, accept, allow, recognize", PRESENT, THIRD_PERSON_SINGULAR)
	test.englishToSpanish("to admit, accept, allow, recognize", PRESENT, FIRST_PERSON_PLURAL)
	test.englishToSpanish("to admit, accept, allow, recognize", PRESENT, SECOND_PERSON_PLURAL)
	test.englishToSpanish("to admit, accept, allow, recognize", PRESENT, THIRD_PERSON_PLURAL)