letters = ["a", "b", "c"]

#add
letters.append("d")
letters.insert(0, "-")
print(letters)

#remove
letters.pop(0)
letters.remove("b")
del letters [0:3]
print(letters)