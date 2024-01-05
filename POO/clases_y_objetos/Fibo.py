

class Fibo:
    def __init__(self,n) -> None:
        self.__n = n

    # get set

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self,n):
        self.__n = n

    def serie(self):

        def fibo(n):
            if n <= 1:
                return n
            else:
                return fibo(n-1) + fibo(n-2)

        for i in range(self.__n):
            print(f'{fibo(i+1)} ,')    


    
    