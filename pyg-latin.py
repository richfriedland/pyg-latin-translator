# Rich's PygLatin Translator (inspired by a code-academy lesson)
# define variable 'pyg' which is the string 'ay'
# this string will be used to be concatenated at the end of the word and preceded by the first letter of the word
pyg = 'ay'
# define variable 'original' to accept input to translate
# input must be a single word, only alpha characters
original = raw_input('Enter a word:')
# check the input to verify it is alpha, does not contain numbers, spaces or special characters
# check to make sure that the user inputted something instead of leaving it blank
if len(original) > 0 and original.isalpha():
    # define variable 'word' which is the original inputted text converted to lower case
    word = original.lower()
    # define variable 'first' which is the first character of the word that was inputted
    first = word[0]
    # define variable 'new_word' which is a concatenation of the lower case version of the inputted text, the first letter of the inputted text and the 'ay' suffix from the pyg variable
    new_word = word + first + pyg
    # slice new_word from the second character through the end
    new_word = new_word[1:]
    # print the resulting word which has been converted to PygLatin!
    print new_word
# if bad input is received, display this error message
else:
    print 'Please be sure to submit a single word, alpha only (no numeric or special characters).'
