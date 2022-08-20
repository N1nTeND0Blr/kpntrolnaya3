def card_num(number):
    return '*' * 12 + str(number)[12:]


print(card_num(input('номер карты: ')))

