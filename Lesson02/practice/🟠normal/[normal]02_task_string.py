text = input("Geben Sie Text ein: ")
if text.startswith("id") and text[3:].isdigit():
    print("Ja")
else:
    print("nein")