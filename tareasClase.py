text = "English=68 Logic=75 Uml=87 Code=80"
notes = [int(i[-2:])
for i in text.split()]

print("The total is: {} and The a verage is: {}".format(sum(notes), sum(notes)/len(notes)))

print ("*************************")

options = [5, 10, 15, 20, 25, 30, 4, 20]

index = options.index(20)
options[index] = 2000

print(options)