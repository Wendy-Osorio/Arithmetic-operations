''' 
Escribe un programa que resuelva a siguiente operación aritmetica (https://img-c.udemycdn.com/redactor/raw/article_lecture/2020-11-05_23-59-30-e5bb152c676fb083c4c02e79021ac6a4.jpg)'''


def principal():

    print('Operación algebraica: (a+b/c*d)^2\n')

    a = input('Ingresa el valor de a: ')

    b = input('\nIngresa el valor de b: ')

    c = input('\ningresa el valor de c: ')

    d = input('\nIngresa el valor de d: ')

    try:

        a = int(a)

        b = int(b)

        c = int(c)

        d= int(d)

        resultado = pow(((a + b) / (c * d)), 2)

        print('El resultado de ({} + {} / {} * {})^2 = {}'.format(a, b, c,d, resultado))

        repetir()
    
    except ValueError:

        try:

            a = float(a)

            b = float(b)

            c = float(c)

            d= float(d)

            resultado = pow(((a + b) / (c * d)), 2)

            print('El resultado de ({} + {} / {} * {})^2 = {}'.format(a, b, c,d, resultado))

            repetir()

        except ValueError:

            print('¡ERROR!: LOS VALORES INGRESADOS NO SON VALIDOS... INTENTELO NUEVAMENTE.\n')

            principal()
            

def repetir():

    resp = input('\n¿Quieres volver a empezar? S/N:' )

    if resp.lower() == 's':

        principal()

    if resp.lower() == 'n':

        print('Usted esta saliendo del programa...')

        exit()
    
    else:
        
        print('¡ERROR!: LOS VALORES INGRESADOS NO SON VALIDOS... INTENTELO NUEVAMENTE.\n')

        repetir()


principal()


