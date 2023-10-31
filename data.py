class Dias(object):
  def __init__(self, Dia, Mes, Ano):
    self.Dia = Dia
    self.Mes = Mes
    self.Ano = Ano

  def setDia(self, Dia):
    if Dia in (1, 2, 3):
      self.Dia = Dia
    else:
      self.Dia = 1

  def getDia(self):
    return self.Dia

  def setMes(self, Mes):
    self.Mes = Mes

  def getMes(self):
    return self.Mes

  def setAno(self, Ano):
    self.Ano = Ano

  def getAno(self):
    return self.Ano



  def __str__(self):
    return "\n\nDia: " + str(self.Dia) + "\n Mes: " + str(
      self.Mes) + "\nAno: " + str(self.Ano)

