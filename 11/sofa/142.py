symbols=dict()
text=input('введите текст: ')
for i in range(len(text)):
    if text[i] not in symbols:
        symbols[text[i]]=i
print(len(symbols))