'''                  Secret Messages
I'll be using an algorithm called a Carsar cipher.
    It maps to a letter that comes 13 letters later.
    A -> N
    B -> O
    C -> P
    D -> Q
    When run twice it reverts back to the original.
    N -> A
    O -> B
    P -> C
    Q -> D

'''



# MAPPING = {
#   'A': 'N', 
#   'B': 'O', 
#   'C': 'P', 
#   'D': 'Q', 
#   'E': 'R', 
#   'F': 'S', 
#   'G': 'T', 
#   'H': 'U', 
#   'I': 'V', 
#   'J': 'W', 
#   'K': 'X', 
#   'L': 'Y', 
#   'M': 'Z', 
#   'N': 'A', 
#   'O': 'B', 
#   'P': 'C', 
#   'Q': 'D', 
#   'R': 'E', 
#   'S': 'F', 
#   'T': 'G', 
#   'U': 'H', 
#   'V': 'I', 
#   'W': 'J', 
#   'X': 'K', 
#   'Y': 'L', 
#   'Z': 'M'






def cipher(original):
	text = ""
	for letter in original:
		letter = letter.upper()
		new_letter = MAPPING[letter]
		text = text + new_letter
	return text

text = input("Text or secret: ")
result = cipher(text)
print(result)
