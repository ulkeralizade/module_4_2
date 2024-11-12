def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function() #не выводится предложение
test_function() #проверка
inner_function() #ошибка


