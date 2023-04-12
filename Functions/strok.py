def gen_dic(str1):
    dict1 = {}
    for i in str1:
        dict1[i] = str1.count(i)
    return dict1

















def s_word(str1):
    str1 = str1.split()
    dict1 = {}
    for i in str1:
        dict1[i] = str1.count(i)
    return dict1
def max_word(str1):
    text = dict()
    for i in str1.split():
        count = text.get(i, 0)
        text[i] = count + 1
    max_count = max(text.values())
    list2 = []
    for i, j in text.items():
        if text[i] == max_count:
            list2.append((i, j))
    print(min(list2))



