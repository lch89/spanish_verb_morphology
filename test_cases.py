#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from json_globals import *

def loadJson(self, file_path):
	json_data = {}

	# if not file_path[-5:0]==".json":
	# 	file_path = "{}.json".format(file_path)

	with open(file_path,"r") as f:
		json_data = json.load(f)
		return json_data

	return json_data

def assertEquals(statement1, statement2):
	assert  statement1==statement2, "{} and {} are not equal".format(statement1,statement2)

if __name__ == "__main__":

	# cross_check = loadJson(SPANISH_CONJ_NAME)
	assertEquals(1,1)
	assertEquals(1,2)

	