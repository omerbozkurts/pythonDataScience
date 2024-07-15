text = 'The goal is to turn data into information, and information into insight.'
text=text.replace(',',' ')
text=text.replace('.',' ')
text=text.upper()
text=list(text.split())
print(text)