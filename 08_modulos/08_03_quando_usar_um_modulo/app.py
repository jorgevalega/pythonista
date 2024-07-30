# Quando usar módulos
# 1° - Separar funcionalidades relacionadas
# Não acoplar o seu código
# Não ter um aplicativo gigante

from banco_de_dados import buscar_usuario
from configuracoes import senha

buscar_usuario()
print(senha)