class Contas(object):
    def __init__(self, codigoConta, descricaoConta, tipoConta, codigoContabil):
        self.codigoConta = codigoConta
        self.descricaoConta = descricaoConta
        self.tipoConta = tipoConta
        self.codigoContabil = codigoContabil

    def setCodigoConta(self,codigoConta):
        if codigoConta in (1, 2, 3, 4):
            self.codigoConta = codigoConta
        else:
            self.codigoConta = 1

    def getCodigoConta(self):
        return self.codigoConta
    def setDescricaoConta(self, descricaoConta):
        self.descricaoConta = descricaoConta
    def getDescricaoConta(self):
        return self.descricaoConta
    def setTipoConta(self, tipoConta):
        self.tipoConta = tipoConta
    def getTipoConta(self):
        return self.tipoConta
    def setCodigoContabil(self, codigoContabil):
        self.codigoContabil = codigoContabil
    def getCodigoContabil(self):
        return self.codigoContabil

    def __str__(self):
        return "\n\nCodigo Conta: " +str(self.codigoConta)+ "\n Descrição da Conta: " +str(self.descricaoConta)+ "\nTipo da Conta: " +str(self.tipoConta)+ "\nConta Contábil: " +str(self.codigoContabil)+ "\n\n"
