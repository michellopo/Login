import biblioteca
from biblioteca import cadastro, mostrar, login, usuario, senha, tent

menu = 0
opcao = 0
while opcao != 4:
    menu = int(input("====MENU====\n"
                 "[1] CADASTRO\n"
                 "[2] MOSTRAR\n"
                 "[3] LOGIN\n"
                 "[4] SAIR\n"
                 ""))
    if menu > 4 or menu <= 0:
        print("Operação Invalida!!")
    match menu:
        case 1:
            cadastro(usuario, senha)
        case 2:
            mostrar(usuario,senha)
        case 3:
            login(usuario,senha,tent)
        case 4:
            print("Processo Encerrado!!")
            opcao = 4


