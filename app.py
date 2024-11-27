from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Dan', 10)
restaurante_praca.receber_avaliacao('João', 9)
restaurante_praca.receber_avaliacao('Maria', 8)
restaurante_praca.receber_avaliacao('Fabio', 3)
restaurante_praca.receber_avaliacao('Daniel', 10)



def main():
  restaurante_praca.listar_restaurantes()


if __name__ == '__main__':
  main()