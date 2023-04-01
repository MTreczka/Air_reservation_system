class Temperature:
    def __init__(self, temp):
        self.temp_c = temp

    @property
    def temp_c(self):
        return f'{self._temp}°C'

    @temp_c.setter
    def temp_c(self, new_temp):
        if new_temp < -273.15:
            raise ValueError('Something is no yes!')
        self._temp = new_temp

    @property
    def temp_f(self):
        return f'{self._temp * 9/5 + 32}°F'

    @property
    def temp_k(self):
        return f'{self._temp + 273.15}K'

    @temp_k.setter
    def temp_k(self, new_temp):
        self.temp_c = new_temp - 273.15

    def __str__(self):
        return f'Temperature {self.temp_c}'

    def __repr__(self):
        return f'{type(self)}({self._temp})'

class TemperatureMars(Temperature):
    def __repr__(self):
        return f'{type(self).__name__}({self.temp_f})'
        
     


t = Temperature(20)
tm=(TemperatureMars(50))
print(tm, repr(tm))
print(str(t), repr(t))
print((tm), repr(tm))
t = Temperature(20)
print(t.temp_c)
print(t.temp_f)
t.temp_c = -200
print(t.temp_c)
print(t.temp_f)

class TemperatureJupiter:
    def __init__(self):
        self.temp = temp

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def _temp(self, value):
        if value < 10:
            raise TypeError(f'Something is no yes')
        self._temp = value

class Devil:
    pass


class Magic:
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls, *args, **kwargs)
        self.xd = 42
        return Devil()

    def __init__(self, param):
        print(vars(self))
        self.param = param

m = Magic()
print(m, type(m))
print(m.param)