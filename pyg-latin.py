# Rich's Enhanced Pig Latin Translator (inspired by a Codeacademy lesson, "pyglatin")
# define variables to be used as suffixes for translated source words 'ay' and 'way'
pyg = 'ay'
pyg_vowel = 'way'
# prompt the user for the original word to be translated (raw input)
original = raw_input('Enter a word to have it translated into Pig Latin:')
# check the input data to ensure it is more than zero characters and only contains alpha (no numbers, spaces or special characters)
if len(original) > 0 and original.isalpha():
	# define variable 'source_word' and convert all text into lowercase
	source_word = original.lower()
	# define variable 'first_letter' which is the first character of the word to translate
	first_letter = source_word[0]
	# determine if the first letter is a consonant
	if first_letter in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'):
		# define variable 'translated_word' which is a concatenation of the source word converted to lowercase, followed 
		# by the first letter of the source word and the suffix 'ay' (called by the 'pyg' variable)
		translated_word = source_word + first_letter + pyg
		# slice the translated word after the first letter
		translated_word = translated_word[1:]
	# determine if the first letter of the source word is a vowel, it will be processed differently
	elif first_letter in ('a', 'e', 'i', 'o', 'u', 'y'):
		# define variable 'translated_word' which is a concatenation of the source word converted to lowercase, followed
		#by the suffix 'way' (called by the 'pyg_vowel' variable)
		translated_word = source_word + pyg_vowel
	# print the translated word to the console
	print translated_word
# if the data provided contains numeric, special characters or was empty, print this error message to the console
else:
    print 'Please be sure to submit a single word, alpha only (no numeric or special characters).'
