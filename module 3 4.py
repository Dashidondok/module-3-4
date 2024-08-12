def single_root_words(root_word, *other_words):
    same_words = []
    word = root_word.lower()
    for i in other_words:
        if word in i.lower() or i.lower() in word:
            same_words.append(i)
    return same_words


print(single_root_words('Лен', 'Лена','Обь', 'Ленин', 'СПб', 'Ленинград'))
