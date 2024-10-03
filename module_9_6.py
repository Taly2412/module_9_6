def all_variants(text):
    for y in range(len(text)):
        for j in range(len(text)-y):
            yield text[j:j+y+1]


a = all_variants("abc")
for i in a:
    print(i)