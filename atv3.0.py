# crie uma duncao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7
n1 = float(input("insira a sua nota"))
n2 = float(input("insira a sua nota"))
n3 = float(input("insira a sua nota"))
media = (n1+n2+n3)/3
if media >= 7:
    print("aprovado")
else:
    print("reprovado")
    print(media)
