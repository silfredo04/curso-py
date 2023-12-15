class Color:

    def __init__(self,color) -> None:
        self.__color = color

    # get y set
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color = color

    def __str__(self) -> str:
        return f' Color -> {self.__color}'
    
