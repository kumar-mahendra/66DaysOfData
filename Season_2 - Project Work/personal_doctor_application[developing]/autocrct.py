import autocorrect as acr 

spell = acr.Speller()
text = input()
text = spell(text)
print(text)