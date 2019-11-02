#Write a function called count_types. count_types
#should take as input a single string, and return a
#dictionary. In the dictionary, the keys should be
#types of characters, and the values should be the
#number of times each type of character appeared in
#the string.
#
#The types of characters that should be handled (and
#thus, the keys in the dictionary) are:
#
# - upper: the count of upper-case or capital letters
# - lower: the count of lower-case letters
# - punctuation: the count of punctuation characters.
#   You may assume this is limited to these punctuation
#   characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# - space: the count of spaces
# - numeral: the count of numerals, 0123456789
#
#Note, however, that any type of character that does
#NOT appear in the string should not be in the dictionary
#at all.
#
#For example:
#
#count_characters("aabbccc") -> 
# {"lower": 7}
#count_characters("ABC 123 doe ray me!") -> 
# {"upper": 3, "lower": 8, "punctuation": 1, "space": 4, "numeral": 3}
#
#Because the first string has only lower-case letters,
#"lower" is the only key in the dictionary.
#
#HINT: If you're sing the ord() function, capitals of
#ordinals between 65 and 90; lower-case letters have
#ordinals between 97 and 122; numerals are between 48
#and 57; spaces are 32; all other numbers between 33
#and 126 are punctuations, and no character will have
#an ordinal outside that range.

def count_types(string):
    dictionary = {}
    
    for letter in string:
        if 65 <= ord(letter) and ord(letter) <= 90:
            if "upper" in dictionary:
                dictionary["upper"] += 1
            else:
                dictionary["upper"] = 1
        
        elif 97 <= ord(letter) and ord(letter) <= 122:
            if "lower" in dictionary:
                dictionary["lower"] += 1
            else:
                dictionary["lower"] = 1
                
        elif ord(letter) == 32:
            if "space" in dictionary:
                dictionary["space"] += 1
            else:
                dictionary["space"] = 1
                
        elif 48 <= ord(letter) and ord(letter) <= 57:
            if "numeral" in dictionary:
                dictionary["numeral"] += 1
            else:
                dictionary["numeral"] = 1
                
        elif 33 <= ord(letter) and ord(letter) <= 126:
            if "punctuation" in dictionary:
                dictionary["punctuation"] += 1
            else:
                dictionary["punctuation"] = 1
                
    return dictionary
