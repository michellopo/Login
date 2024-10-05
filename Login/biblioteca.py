usuario = [0]*3
senha = [0]*3
tent = 0
tam = len(usuario)
def cadastro(usuario,senha):
    novo_usuario = input("Digite seu nome: ")
    nova_senha = input("Digite sua senha: ")
    for x in range(tam):
        if senha[x] == 0 and usuario[x] == 0:
            senha[x] = nova_senha
            usuario[x] = novo_usuario
            return "Usuario cadastrado!!"


def mostrar(usuario,senha):
    for i in range (tam):
        print(f"Usuario{i+1}: {usuario[i]}\n"
              f"Senha{i+1}: {senha[i]}")

def login(usuario, senha,tent):
    while tent < 3:
        usuariol = input("Digite o seu nome: ")
        senhal = input("Digite sua senha: ")
        for j in range(tam):
            if usuariol == usuario[j] and senhal == senha[j]:
                print("Login efetuado com sucesso!!")
                tent = 4
            elif usuariol == usuario[j] and senhal != senha[j]:
                print("SENHA INVALIDA!!")
            elif usuariol != usuario[j] and senhal == senha[j]:
                print("USUARIO INVALIDO!!")
        tent +=1
        if tent ==3:
            print("USUARIO BLOQUEADO!!")
