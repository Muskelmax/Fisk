from math import sqrt

class Vector:
  def __init__(self, x, y):
    self.__x = x
    self.__y = y
  def getter(self):
    return [self.__x, self.__y]
  @property
  def x(self):
    return self.__x
  @property
  def y(self):
    return self.__y
  def setter(self, x, y):
    self.__x = x
    self.__y = y
  def getLængde(self):
    return(sqrt(self.__x**2+self.__y**2))
  def prikProdukt(self, Prik):
    return Vector(self.__x * Prik.__x, self.__y * Prik.__y)
  def __add__(self, other):
    return Vector(self.__x + other.__x, self.__y + other.__y)
  def __sub__(self, other):
    return Vector(self.__x - other.__x, self.__y - other.__y)
  def __mul__(self, other):
    return Vector(self.__x * other, self.__y * other)
  def __str__(self):
    return(f"x: {self.__x}, y:{self.__y}")
  def __truediv__(self, other):
    return Vector(self.__x/other, self.__y/other)
