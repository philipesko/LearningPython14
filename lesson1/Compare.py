def compare(olders):
    olders = int(olders)
    if 7 < olders <= 18:
        answer = "You must go to school!"
    elif 18 < olders <= 25:
        answer = "You must go to university!"
    elif 25 < olders <= 65:
        answer = "You must go to work!"
    else:
        answer = "This programm not for you!"

    return answer


answerToPrint = compare(input("How old are you: "))
print(answerToPrint)

