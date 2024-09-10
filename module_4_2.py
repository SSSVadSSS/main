def test_function():

    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()


#  При попытке вызвать функцию inner_function() вне функции test_function()
#  выдает ошибку: NameError: name 'inner_function' is not defined - Функция не определена, т.е. находится
#  за пределами видимости
