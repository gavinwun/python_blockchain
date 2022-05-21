def normalFunc(*someFuncs):
    print(someFuncs)
    for someFunc in someFuncs:
        print(f'Result of passed in function - {someFunc():^20}')

def someFunc():
    return 'I am from someFunc'

normalFunc(someFunc)

normalFunc(lambda : 'I am from lambda')

normalFunc(someFunc, lambda: 'I am from lambda', lambda: 20.1)