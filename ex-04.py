nota1 =  int (input( ' Entre com uma nota1 ' ))
nota2 =  int (input( ' Entre com uma nota2 ' ))

media = (nota1 + nota2)/ 2
if (media >= 6): 
    print ( 'Parabéns! Você foi aprovado!', media)
elif (media < 6):
    print ( 'Você está de recuperação' , media)
