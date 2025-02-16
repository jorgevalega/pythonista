
medida_cabelo = float(input('Qual o tamanho do cabelo em cm:\n')) 
if medida_cabelo <= 20:
    print(f'O comprimento do seu cabelo é de {medida_cabelo}cm, paga o valor de R$50,00.')
elif 20 < medida_cabelo <= 30:
    print(f'O comprimento do seu cabelo é de {medida_cabelo}cm, paga o valor de R$70,00.')
elif 30 < medida_cabelo <= 50:
    print(f'O comprimento do seu cabelo é de {medida_cabelo}cm, paga o valor de R$100,00.')
else:
    print(f'O comprimento do seu cabelo é de {medida_cabelo}cm, favor consultar na recepção.')
