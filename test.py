#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as p
import json

SPANISH_CONJ_NAME = "Spanish_Conjugations.json"
SP_EN_INF_NAME = "Spanish_to_English_Infinitives.json"
EN_SP_INF_NAME = "English_to_Spanish_Infinitives.json"

FIRST_PERSON_SINGULAR = "FIRST_PERSON_SINGULAR"
SECOND_PERSON_SINGULAR = "SECOND_PERSON_SINGULAR"
THIRD_PERSON_SINGULAR = "THIRD_PERSON_SINGULAR"
FIRST_PERSON_PLURAL = "FIRST_PERSON_PLURAL"
SECOND_PERSON_PLURAL = "SECOND_PERSON_PLURAL"
THIRD_PERSON_PLURAL = "THIRD_PERSON_PLURAL"

# spanish_conj[verb][tense][person] = conjugated verb
spanish_conj = {}

#Used for translating English to Spanish for parsing Excel sheet
en_sp_labels = {}

en_sp_tenses = {"Present" : "Presente", "Preterite" : "Pretérito", "Future" : "Futuro", "Conditional" : "Condicional", "Imperfect" : "Imperfecto", "Present Progressive" : "Presente progresivo", "Perfect Past" : "Pretérito perfecto", "Perfect Present" : "Pluscuamperfecto", "Perfect Future" : "Futuro perfecto", "Conditional Perfect" : "Condicional perfecto", "Preterite (Archaic)" : "Pretérito anterior", "Present Subjunctive" : "Subjuntivo presente", "Imperfect Subjunctive -RA" : "Subjuntivo imperfecto -RA", "Imperfect Subjunctive -SE" : "Subjuntivo imperfecto -SE", "Future Subjunctive" : "Subjuntivo futuro", "Past Perfect Subjunctive" : "Subjuntivo pretérito perfecto", "Pluperfect Subjunctive -RA" : "Subjuntivo pluscuamperfecto -RA", "Pluperfect Subjunctive -SE" : "Subjuntivo pluscuamperfecto -SE", "Future Perfect Subjunctive" : "Subjuntivo futuro perfecto", "Imperative Affirmative" : "Imperativo positivo", "Imperative Negative" : "Imperativo negativo"}

sp_en_tenses = {"Presente" : "Present", "Pretérito" : "Preterite", "Futuro" : "Future", "Condicional" : "Conditional", "Imperfecto" : "Imperfect", "Presente progresivo" : "Present Progressive", "Pretérito perfecto" : "Perfect Past", "Pluscuamperfecto" : "Perfect Present", "Futuro perfecto" : "Perfect Future", "Condicional perfecto" : "Conditional Perfect", "Pretérito anterior" : "Preterite (Archaic)", "Subjuntivo presente" : "Present Subjunctive", "Subjuntivo imperfecto -RA" : "Imperfect Subjunctive -RA", "Subjuntivo imperfecto -SE" : "Imperfect Subjunctive -SE", "Subjuntivo futuro" : "Future Subjunctive", "Subjuntivo pretérito perfecto" : "Past Perfect Subjunctive", "Subjuntivo pluscuamperfecto -RA" : "Pluperfect Subjunctive -RA", "Subjuntivo pluscuamperfecto -SE" : "Pluperfect Subjunctive -SE", "Subjuntivo futuro perfecto" : "Future Perfect Subjunctive", "Imperativo positivo" : "Imperative Affirmative", "Imperativo negativo" : "Imperative Negative"}

en_sp_person = {FIRST_PERSON_SINGULAR : "yo", SECOND_PERSON_SINGULAR : "tu", THIRD_PERSON_SINGULAR : "el", FIRST_PERSON_PLURAL : "ns", SECOND_PERSON_PLURAL : "vs", THIRD_PERSON_PLURAL : "ellos"}

sp_en_person = {"yo" : FIRST_PERSON_SINGULAR, "tu" : SECOND_PERSON_SINGULAR, "el" : THIRD_PERSON_SINGULAR, "ns" : FIRST_PERSON_PLURAL, "vs" : SECOND_PERSON_PLURAL, "ellos" : THIRD_PERSON_PLURAL}

#Flag specifically for parsing -RA and -SE conjugations of imperfect subjunctive
imperf_subj_ra = True

#Flag specifically for parsing -RA and -SE conjugations of pluperfect subjunctive
pluperf_subj_ra = True

def loadJson(file_path):
	json_data = {}

	if not file_path[-5:0]==".json":
		file_path = "{}.json".format(file_path)

	with open(file_path,"r") as f:
		json_data = json.load(f)
		return json_data

	return json_data

# Link infinitives and conjugations
# if __name__ == "__main__":
# 	print("Starting")
# 	excel_data = p.read_excel("jehle_dcomtois_updates.xls", sheetname="conjug")
# 	print("Parsing")

# 	for idx in excel_data.index:
# 		verb = excel_data["verbo"][idx]
# 		mood = excel_data["modo"][idx]
# 		tense = excel_data["tiempo"][idx]

# 		print("Verb: {}, Tense: {}".format(verb, tense))

# 		# If idx % 16 == 0 then 

# 		verb_entry = spanish_conj.get(verb,{})
# 		tense_entry = verb_entry.get(tense,{})
# 		# person_entry = verb_entry.get(tense,{})

# 		fst_s = excel_data["yo"][idx]
# 		scd_s = excel_data["tu"][idx]
# 		thd_s = excel_data["el"][idx]
# 		fst_p = excel_data["ns"][idx]
# 		scd_p = excel_data["vs"][idx]
# 		thd_p = excel_data["ellos"][idx]

# 		if tense=="Subjuntivo imperfecto":
# 			if imperf_subj_ra:
# 				tense = "Subjuntivo imperfecto -RA"
# 			else:
# 				tense = "Subjuntivo imperfecto -SE"
# 			imperf_subj_ra = not imperf_subj_ra
# 		elif tense=="Subjuntivo pluscuamperfecto":
# 			if pluperf_subj_ra:
# 				tense = "Subjuntivo pluscuamperfecto -RA"
# 			else:
# 				tense = "Subjuntivo pluscuamperfecto -SE"
# 			pluperf_subj_ra = not pluperf_subj_ra	

# 		if p.isnull(fst_s):
# 			fst_s = "N/A"

# 		tense_entry[FIRST_PERSON_SINGULAR] = fst_s
# 		tense_entry[SECOND_PERSON_SINGULAR] = scd_s
# 		tense_entry[THIRD_PERSON_SINGULAR] = thd_s
# 		tense_entry[FIRST_PERSON_PLURAL] = fst_p
# 		tense_entry[SECOND_PERSON_PLURAL] = scd_p
# 		tense_entry[THIRD_PERSON_PLURAL] = thd_p

# 		en_tense = sp_en_tenses[tense]

# 		verb_entry.update({en_tense:tense_entry})
# 		spanish_conj.update({verb:verb_entry})

# 	with open(SPANISH_CONJ_NAME,"w") as f:
# 		# json_data = json.dumps(spanish_conj)
# 		json.dump(spanish_conj, f, sort_keys=True, indent=4)

# 	# json_data = json.dumps(spanish_conj)
# 	# json.dump(json_data, SPANISH_CONJ_NAME)
# 	print("Done")

en_sp_inf = {}
sp_en_inf = {}

# Link Spanish infinitives and English infinitives
# if __name__ == "__main__":
# 	print("Starting")
# 	#excel_data = p.read_excel("jehle_verb_database.csv", sheetname="jehle_verb_database")
# 	#excel_data = p.read_excel("jehle_verb_database_excel.xlsx", sheetname="jehle_verb_database")
# 	excel_data = p.read_excel("jehle_dcomtois_updates - Edit.xls", sheetname="prop")
# 	print("Parsing")

# 	for idx in excel_data.index:		
# 		# sp_inf = excel_data["infinitive"][idx]
# 		# en_inf = excel_data["infinitive_english"][idx]
# 		sp_inf = excel_data["verbo"][idx]
# 		en_inf = excel_data["trad_en"][idx]

# 		print("Spanish: {}, English: {}".format(sp_inf, en_inf))

# 		en_sp_inf.update({en_inf:sp_inf})
# 		sp_en_inf.update({sp_inf:en_inf})

# 	with open(SP_EN_INF_NAME,"w") as f:
# 		json.dump(sp_en_inf, f, sort_keys=True, indent=4)

# 	with open(EN_SP_INF_NAME,"w") as f:
# 		json.dump(en_sp_inf, f, sort_keys=True, indent=4)
			
# 	print("Done")
