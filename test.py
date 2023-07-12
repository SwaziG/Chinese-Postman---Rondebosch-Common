import random 

choices = ['C1','C2','C3','C4','C5','C6','C7']
choose = ""
i = 7
while i > 0: 
    choose = random.choice(choices)
    choices.remove(choose)
    print (choose)
    print (choices)
    i -= 1
