def trans(ph):
    trans= ""
    for i in ph:
        if i in "AEIOUaeiou":
            trans = trans + "g"
        else:
            trans = trans + i
    return trans

ph = input("Enter your word : ")

print(trans(ph))    


''

