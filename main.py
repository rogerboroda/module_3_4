def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:                # проверка на наличие слов с root_word
        other_word_lower = word.lower()     # создаем переменную other_word_lower равную word в нижнем регистре
        root_word_lower = root_word.lower() # создаем переменную root_word_lower равную root_word в нижнем регистре
        if root_word_lower in other_word_lower or other_word_lower in root_word_lower:
            same_words.append(word)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

# Вывод на консоль:
# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']invalid literal for int() with base 10word lower