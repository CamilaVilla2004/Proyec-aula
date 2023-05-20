'proyecto de aula'
print('PRMAPC: PLATAFORMA DE REPORTES PARA LA MEJORA DEL ALUMBRADO PÚBLICO DE LA CIUDAD DE CARTAGENA')
print('--------------------------------------------------------------------')
# DATOS PREDETERMINADOS
correo = 'valt@correo.com'
contraseña  =  1234
camiiiiii
#menú
while True:
    print("Menú:")
    print("1. Inicio de sesión")
    print("2. Registrarse")
    
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        print("Digite su correo y contraseña")
        if opcion == "1":
            correo1 = input(str("Ingrese su correo electrónico: "))
            contrasena1 = input(str("Ingrese su contraseña: "))
            if correo1 == correo and contrasena1 == contrasena:
                print("Inicio de sesión exitoso!")
        else:
            print("Correo o contraseña incorrectos. Inténtelo nuevamente.")
            

    elif opcion == "2":
        print("Ha seleccionado la opción 2")
        # Coloca aquí el código correspondiente a la opción 2

    else:
        print("Opción inválida. Por favor, ingrese un número válido.")
