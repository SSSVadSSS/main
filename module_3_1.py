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
    string = str(a)
    list_to_search = [b]
    n = 0
    c = False
    while n < len(b):
        if b[n].lower() != a.lower():
            n += 1
            continue
        else:
            c = True
            n += 1
    return c


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
