b = input("ENTER YOUR NAME :")
g = input("ENTER YOUR CRUSH NAME")
b = list(b.upper())
g = list(g.upper())


flames = list("FLAMES")
firstlist = []
secondlist = []

flames_dict = {'F':'Friends',
'L':'Love',
'A':'Affection',
'M':'Marriage',
'E':'Enemy',
'S':'Siblings'}

for i in b:
    if i not in g:
        firstlist.append(i)

for j in g :
    if j not in b:
        secondlist.append(j)

n = len(firstlist) + len(secondlist)

while len(flames)>1:

    number = n%len(flames)
    flames.pop(number-1)

print(flames_dict[flames[0]])
