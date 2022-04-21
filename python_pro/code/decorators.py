from datetime import datetime

def execution_time(func):
    def wrapper(*args,**kwargs):
        initial_time = datetime.now()
        func(*args,**kwargs)
        final_time = datetime.now()
        time_enlapsed = final_time - initial_time
        print('Pasaron ' + str(time_enlapsed.total_seconds()) + ' segundos')
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass

@execution_time
def saludo(nombre='Cesar'):
    print('Hola ' + nombre)
    

@execution_time
def suma(a: int, b:int ) -> int:
    return a + b

suma(5,5)
saludo('Robin')
#random_func()