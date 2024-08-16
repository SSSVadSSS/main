calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(a):
    count_calls()
    a = (len(a), a.upper(), a.lower())
    return a


def is_contains(a, b):
    count_calls()
    string = a
    list_to_search = b
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string.lower() in list_to_search:
        c = True
    else:
        c = False
    return c


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
# Переписал функцию is_contains так, чтобы было ближе к заданию,
# иначе смысл переменных string и list_to_search утрачивается