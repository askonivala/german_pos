#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from ClassifierBasedGermanTagger import ClassifierBasedGermanTagger
import pickle

with open('nltk_german_classifier_data.pickle', 'rb') as f:
	tagger = pickle.load(f)

def tag_text(text):
	result = tagger.tag(text)
	return result

def main():
	text = "Was ich von der Geschichte des armen Werther nur habe auffinden können, habe ich mit Fleiß gesammelt und lege es euch hier vor, und weiß, daß ihr mir's danken werdet. Ihr könnt seinem Geist und seinem Charakter eure Bewunderung und Liebe, seinem Schicksale eure Tränen nicht versagen. Und du gute Seele, die du eben den Drang fühlst wie er, schöpfe Trost aus seinem Leiden, und laß das Büchlein deinen Freund sein, wenn du aus Geschick oder eigener Schuld keinen näheren finden kannst."
	token_text = nltk.word_tokenize(text)
	pos_text = tagger.tag(token_text)
	print(pos_text)

if __name__ == '__main__':
	main()

