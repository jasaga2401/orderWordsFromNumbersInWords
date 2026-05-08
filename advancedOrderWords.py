
def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

words = "Thi1s is2 3a T4est"
print(order(words))
