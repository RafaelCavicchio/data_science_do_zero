class Acao():
    contador = 0
    
    def __init__(self, ticker, pl, valor_intrinseco, media_dividendo_ano = {}):
        self.ticker = ticker   
        self.pl = pl    
        self.valor_intrinseco = valor_intrinseco
        #self.media_dividendo_ano
        Acao.contador += 1

    

    