# PROJETO EM PYTHON

secreto = 'perfume'
digitadas = []
chances= 3 

print('-=' * 20)
print('             JOGO DA FORCA PYTHON')
print('-=' * 20)

while True:

  letra = str(input('Digite uma letra:'))

  if len(letra)> 1:

    print('ERRO, Não vale digitar mais de uma letra.')







  secreto_temporario = ''
  for letra_secreta in secreto:
      if letra_secreta in digitadas:
          secreto_temporário += letra_secreta
  else:
    secreto_temporariosecreto_temporário += '*'
        
    if secreto_temporário == secreto: 
      print('Você venceu e escapou da forca!')
      break
    else:
      print(f'A palavra secreta está assim: {secreto_temporário}')
      if letra not in secreto:
        chances -= 1
    
    if chances <=0:
     print('Você perdeu! FORCA!')
     break
     
    print(f'Você tem {chances} chances. ')
    print()

    
    
