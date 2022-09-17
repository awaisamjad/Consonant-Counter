text = input("ENTER TEXT: ")
vowels = ["a", "e", "i", "o", "u"]

def vowelCounter():
    SUM = 0
    for char in text:
        if char not in vowels:
            SUM = SUM+1
    print(SUM)
vowelCounter()
