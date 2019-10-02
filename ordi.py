from random import choice

mots = ["tennis", "abrico", "mot", "riviere"]
mot = choice(mots)
i = 0
nb = 6
monMot = []
while i < len(mot):
    monMot += "_"
    i = i + 1

def game(n):
    pendu = ""
    lettre = input("choix de lettre: ")
    if lettre in mot:
        y = 0
        while y < len(mot):
            if mot[y] == lettre:
                monMot[y] = lettre
            y = y + 1
        s = ''.join(monMot)
        print(s)
        if "_" in s:
            game(n)
        else:
            print("tu a gagnier ;)")
            return
    else:
        n = n - 1
        if n == 5:
            pendu = """
            |
            |
            |
            |
            |
            """
        elif n == 4:
            pendu = """
       _____
            |
            |
            |
            |
            |
            """
        elif n == 3:
            pendu = """
       _____
       |    |
            |
            |
            |
            |
            """
        elif n == 2:
            pendu = """
       _____
       |    |
       o    |
            |
            |
            |
            """
        elif n == 1:
            pendu = """
       _____
       |    |
       o    |
      /|\   |
            |
            |
            """
        elif n == 0:
            pendu = """
       _____
       |    |
       o    |
      /|\   |
      / \   |
            |
            """
            print("perdu!!! :(")
            print(pendu)
            return 0
        print(pendu)
        game(n)


game(nb)



#  ____
# |    |
# o    |
#/|\   |
#/ \   |