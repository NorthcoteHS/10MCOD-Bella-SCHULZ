def main():
    lst = [ 'sh' , 'gl' , 'ch' , 'ph' , 'tr' , 'br' , 'fr' , 'bl' , 'gr' , 'st' , 'sl' , 'cl' , 'pl' , 'fl']
# Text shown on screen
    sentence = input('Type what you would like translated into Piglatin and press ENTER: ')
    sentence = sentence.split()
    for k in range(len(sentence)):
        i = sentence[k]
        if i[0] in ['a' , 'e' , 'i' , 'o' , 'u']:
            sentence[k]
        elif t(i) in lst:
            sentence[k] = i[2:]+i[:2]+'ay'
        elif i.isalpha() == False:
            sentence[k] = i

        else:
            sentence[k] = i[1:]+i[0]+'ay'
  return ' '.join(sentence)

def t(str):
    return str[0]+str[1]

if _name_ == "_main_":
    x = main()
    print(x)
    
    
