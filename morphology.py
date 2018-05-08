#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from json_globals import *
from spanish_irregulars import *
# from test import * #TODO: Turn into JSON parsing specific things

class Conjugator():

	def __init__(self):
		#TODO: Decide if we need this field for GUI processing
		self.conjugations = self.loadJson(SPANISH_CONJ_NAME) # For cross-checking
		self.sp_en_inf = self.loadJson(SP_EN_INF_NAME)
		self.en_sp_inf = self.loadJson(EN_SP_INF_NAME)
		# self.morphology = Morphology()
		# self.phonology = Phonology()

	def getTenses(self):
		# self.conjugations.values().keys()
		# return set("Present", "Preterite", "Future", "Conditional", "Imperfect", "Present Progressive", "Perfect Past", "Perfect Present", "Perfect Future", "Conditional Perfect", "Preterite (Archaic)", "Present Subjunctive", "Imperfect Subjunctive -RA", "Imperfect Subjunctive -SE", "Future Subjunctive", "Past Perfect Subjunctive", "Pluperfect Subjunctive", "Pluperfect Subjunctive", "Future Perfect Subjunctive", "Imperative Affirmative", "Imperative Negative")
		return set(en_sp_tenses.keys())

	def getPersons(self):
		# return set(FIRST_PERSON_SINGULAR, SECOND_PERSON_SINGULAR, THIRD_PERSON_SINGULAR, FIRST_PERSON_PLURAL, SECOND_PERSON_PLURAL, THIRD_PERSON_PLURAL)
		return set(en_sp_person.keys())

	def loadJson(self, file_path):
		json_data = {}

		# if not file_path[-5:0]==".json":
		# 	file_path = "{}.json".format(file_path)

		with open(file_path,"r") as f:
			json_data = json.load(f)
			return json_data

		print("File could not be read: {}".format(file_path))

		return json_data
	
	# def englishToSpanish(self, eng_word, tense=None, person=None):
	def englishToSpanish(self, eng_word, tense, person):
		"""Given"""
		verb = self.en_sp_inf.get(eng_word, "")
		# print(verb)

		translated_verb = self.conjugateInfinitive(verb, tense, person)		

		# print(translated_verb)
		# print("---")

		return translated_verb

	def conjugateInfinitive(self, infinitive, tense, person):
		"""Given"""		
		#Morphology application
		# print(infinitive)
		morph_verb = self.morphology(infinitive, tense, person)
		# print(morph_verb)

		#Phonology application
		phon_verb = self.phonology(infinitive, morph_verb, tense, person)
		# phon_verb = morph_verb

		# print(phon_verb)
		# print("---")

		return phon_verb
		
##################### MORPHOLOGY CODE #####################	

	def morphology(self, verb, tense, person):
		return self.conjugate(verb, tense, person)

	def conjugate(self, verb, tense, person):
		"""Given the verb ending, tense, and person, conjugate the verb"""
		#TODO: Account for reflexive verbs

		#if reflexive then do a thing

		conjugate_verb = verb
		stem = verb[:-2]
		ending = verb[-2:]

		#Check for tense, then person, then ending
		if tense==PRESENT:
			# print("Present tense")
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
					conjugate_verb = stem+"amos"
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
			print("{}".format("Present Progressive"))
			conjugate_verb = stem+"ando"

			if person==FIRST_PERSON_SINGULAR:
				conjugate_verb = "Estoy" + conjugate_verb
			elif person==SECOND_PERSON_SINGULAR:
				conjugate_verb = "Estás" + conjugate_verb
			elif person==THIRD_PERSON_SINGULAR:
				conjugate_verb = "Está" + conjugate_verb
			elif person==FIRST_PERSON_PLURAL:
				conjugate_verb = "Estamos" + conjugate_verb
			elif person==SECOND_PERSON_PLURAL:
				conjugate_verb = "Estáis" + conjugate_verb
			elif person==THIRD_PERSON_PLURAL:
				conjugate_verb = "Están" + conjugate_verb
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
			#TODO: Need to maintain irregularity
			#Should be [conjugateInfinitive] instead of [conjugate]
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
			print("{}".format("Future Subjunctive"))
			#TODO: Need to maintain irregularity
			#Should be [conjugateInfinitive] instead of [conjugate]
			subjunctive_stem = conjugate(verb, PRETERITE, THIRD_PERSON_PLURAL)[:-3]

			if person==FIRST_PERSON_SINGULAR or person==THIRD_PERSON_SINGULAR:
				conjugate_verb = subjunctive_stem+"re"
			elif person==SECOND_PERSON_SINGULAR:
				conjugate_verb = subjunctive_stem+"res"
			elif person==FIRST_PERSON_PLURAL:
				#Add accent to last vowel
				# "á"
				# "é"
				ending_vowel = subjunctive_stem[-1]
				new_vowel = "á" if ending_vowel=="a" else "é"
				
				conjugate_verb = subjunctive_stem[:-1]+new_vowel+"remos"				
				
			elif person==SECOND_PERSON_PLURAL:
				conjugate_verb = subjunctive_stem+"reis"
			elif person==THIRD_PERSON_PLURAL:
				conjugate_verb = subjunctive_stem+"ren"			
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

##################### PHONOLOGY CODE #####################

	def phonology(self, original_verb, morph_verb, tense, person):
		phon_verb = morph_verb;
		if tense==PRESENT:
			#Find boot verbs 
				# e->ie boots
				# e->i boots
				# o->ue boots
				# -uir boots
			if (not person==FIRST_PERSON_PLURAL) and (not person==SECOND_PERSON_PLURAL):
				phon_verb = self.bootCheck(original_verb, morph_verb, tense, person)

			if person==FIRST_PERSON_SINGULAR:
				phon_verb = self.irregFstSing(original_verb, morph_verb, tense, person)

			if person==FIRST_PERSON_PLURAL:
				pass

			#-cer verbs (Yo only)
			#-ger and -gir verbs (Yo only)
			#-eguir verbs
			

			# print("Present tense")			
		elif tense==PRETERITE:
			print("TODO: Implement {}".format(PRETERITE))
		elif tense==FUTURE:
			print("TODO: Implement {}".format(FUTURE))
		elif tense==CONDITIONAL:
			print("TODO: Implement {}".format(CONDITIONAL))
		elif tense==IMPERFECT:
			print("TODO: Implement {}".format(IMPERFECT))
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

		return phon_verb;

	def bootCheck(self, original_verb, morph_verb, tense, person):
		
		# e->ie boots
		if(original_verb in ie_boots):
			# print("Verb \'{}\' is an e->ie boot".format(original_verb))
			#Find index of second-to-last e
			to_change = original_verb.rfind("e",0,-2)
			morph_verb = morph_verb[:to_change]+"ie"+morph_verb[to_change+1:]
		# o->ue boots
		elif(original_verb in ue_boots):
			# print("Verb \'{}\' is an o->ue boot".format(original_verb))
			to_change = original_verb.rfind("o",0,-2)
			morph_verb = morph_verb[:to_change]+"ue"+morph_verb[to_change+1:]
		# e->i boots
		elif(original_verb in i_boots):
			# print("Verb \'{}\' is an e->i boot".format(original_verb))
			to_change = original_verb.rfind("e",0,-2)
			morph_verb = morph_verb[:to_change]+"i"+morph_verb[to_change+1:]
		#TODO: This can probably be replaced with a predictive rule
		# -uir boots
		elif(original_verb[-3:]=="uir"):
			# print("Verb \'{}\' is an -uir boot".format(original_verb))
			to_change = original_verb.rfind("u")
			morph_verb = morph_verb[:to_change+1]+"y"+morph_verb[to_change+1:]
		else:
			print("Verb \'{}\' is NOT a boot".format(original_verb))

		return morph_verb

	def irregFstSing(self, original_verb, morph_verb, tense, person):
		first_check = original_verb[-3:]
		second_check = original_verb[-4:]

		if(first_check=="ger" or first_check=="gir"):
			print("Yo, present, \'ger\' or \'gir\'")
			g_index = morph_verb.rfind("g")
			morph_verb = morph_verb[:g_index]+"j"+morph_verb[g_index+1:]
		elif(second_check=="guir"):
			print("Yo, present, \'guir\'")
			g_index = morph_verb.rfind("g")
			morph_verb = morph_verb[:g_index]+"o"

		# Unexplained irregulars
		elif(original_verb=="caber"):
			morph_verb = "quepo"
		elif(original_verb=="caer"):
			morph_verb = "caigo"
		elif(original_verb=="conocer"):
			morph_verb = "conozco"
		elif(original_verb=="dar"):
			morph_verb = "doy"
		elif(original_verb=="hacer"):
			morph_verb = "hago"
		elif(original_verb=="poner"):
			morph_verb = "pongo"
		elif(original_verb=="saber"):
			morph_verb = "sé"
		elif(original_verb=="salir"):
			morph_verb = "salgo"
		elif(original_verb=="traducir"):
			morph_verb = "traduzco"
		elif(original_verb=="traer"):
			morph_verb = "traigo"
		elif(original_verb=="valer"):
			morph_verb = "valgo"
		elif(original_verb=="ver"):
			morph_verb = "veo"
		
		return morph_verb

	def verbHasPrefix(self, verb, stem):
		#Check if base stem is located at the end of the provided verb
		has_prefix = verb.rfind(stem,len(verb)-len(stem))
		
		# return has_prefix > 0
		return has_prefix >= 0

if __name__ == "__main__":
	test = Conjugator()
	# print(len(test.conjugations.keys()))
	# test.englishToSpanish("to dance", PRESENT, FIRST_PERSON_SINGULAR)
	# test.englishToSpanish("to dance", PRESENT, SECOND_PERSON_SINGULAR)
	# test.englishToSpanish("to dance", PRESENT, THIRD_PERSON_SINGULAR)
	# test.englishToSpanish("to dance", PRESENT, FIRST_PERSON_PLURAL)
	# test.englishToSpanish("to dance", PRESENT, SECOND_PERSON_PLURAL)
	# test.englishToSpanish("to dance", PRESENT, THIRD_PERSON_PLURAL)
	# print("---------------")
	# test.englishToSpanish("to eat", PRESENT, FIRST_PERSON_SINGULAR)
	# test.englishToSpanish("to eat", PRESENT, SECOND_PERSON_SINGULAR)
	# test.englishToSpanish("to eat", PRESENT, THIRD_PERSON_SINGULAR)
	# test.englishToSpanish("to eat", PRESENT, FIRST_PERSON_PLURAL)
	# test.englishToSpanish("to eat", PRESENT, SECOND_PERSON_PLURAL)
	# test.englishToSpanish("to eat", PRESENT, THIRD_PERSON_PLURAL)
	# print("---------------")
	# test.englishToSpanish("to admit, accept, allow, recognize", PRESENT, FIRST_PERSON_SINGULAR)
	# test.englishToSpanish("to admit, accept, allow, recognize", PRESENT, SECOND_PERSON_SINGULAR)
	# test.englishToSpanish("to admit, accept, allow, recognize", PRESENT, THIRD_PERSON_SINGULAR)
	# test.englishToSpanish("to admit, accept, allow, recognize", PRESENT, FIRST_PERSON_PLURAL)
	# test.englishToSpanish("to admit, accept, allow, recognize", PRESENT, SECOND_PERSON_PLURAL)
	# test.englishToSpanish("to admit, accept, allow, recognize", PRESENT, THIRD_PERSON_PLURAL)