def login(usuario, password):
    usuario_correcto = "Juan Perez"
    password_correcto = "123Hola"

    if usuario == usuario_correcto and password == password_correcto:
        print("BIENVENIDO")
    else:
        print("Usuario o password incorrectos")

usuario = input("Ingresa el usuario: ")
password = input("Ingresa el password: ")
login(usuario, password)