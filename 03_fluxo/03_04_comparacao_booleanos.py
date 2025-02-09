idade = 21
possui_convite = False
filho_do_dono = True

print((idade >= 21) and  (possui_convite == True))
print(idade >= 21 or possui_convite == True)
print(idade >= 21 or possui_convite == True)

print((idade > 21 and possui_convite == True) or (filho_do_dono == True))


# Exemplo
maior_de_idade = True
possui_carteira_de_trabalho = True
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False

# Você só pode trabalhar aqui se for maior de idade e possuir carteira de trabalho
print(maior_de_idade == True and possui_carteira_de_trabalho == True)
print(maior_de_idade and possui_carteira_de_trabalho)

# Queremos contratar pessoas que ainda não possuem veículo próprio, mas já possuam uma carteira de trabalho
print(possui_carteira_de_trabalho == True and not possui_veiculo_proprio)