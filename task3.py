dict = {1:"АВЕИНОРСТAEIOULNSTR",
        2:"ДКЛЬПУDG",
        3:"БГЁЬЯBCMP",
        4:"ЙЫFHVWY",
        5:"ЖЗХЦЧK",
        8:"ШЭЮJX",
        10:"ЩЪQZ"}
count = 0
word = input("Введите слово ").upper()
for i in range(len(word)):
    for k,v in dict.items():
        if word[i] in v:
            count+=k
print(count)
