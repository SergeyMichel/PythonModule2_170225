text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"

worter = text.split()

wortlange = [word for word in worter if len(word) > 5]

zahl_worter= len(wortlange)

print("Anzahl der Wörter mit mehr als 5 Zeichnen:", zahl_worter)
