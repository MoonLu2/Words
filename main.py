memes = {
    "КРИНЖ": "Странное, Ужаснное, Плохое",
    "ЛОЛ": "Типо: Смешно обхахочишься",
    "БАГ": "Ошибка или недочет в программе. Относится к програмированию"
}

while True:
    print("")
    print("Введите слэнговое слово которое не знаете")
    print("ТОЛЬКО БОЛЬШИМИ БУКВАМИ КАК СДЕСЬ!")
    new_word = input('>')
    
    if new_word in memes:
        print("")
        print(memes[new_word])
    else:
        print("Ошибка", new_word, "Нет в словаре")
        print("")
