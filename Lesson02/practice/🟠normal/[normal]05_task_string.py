text = "В теории, теория и практика неразделимы. На практике это не так."

vowels = "ауоыэяюёие"

text = text.lower()
vowel_buchstaben = sum(1 for char in text if char in vowels)

print("Anzahl der Vokale:", vowel_buchstaben)