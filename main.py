import time
from app.Workbook import Workbook
from app.Cartao import Cartao


def main():
    wb = Workbook()
    cartao = Cartao()

    cartoes = 0
    ini = time.time()
    for key, cell in wb.get_rows():
        cartao.gerar(cell, "jpg")
        cartoes = cartoes + 1
    fim = time.time()

    print("Foram criados %d cartões" % cartoes)
    print("Se passaram %f segundos" % (fim - ini))


if __name__ == "__main__":
    main()
