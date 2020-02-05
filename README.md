# number-code-validator

O sistema dos correios de Gotham City tiveram um problema e perderam seu validador de CEPs. Hoje, sua missão é criar um validador de CEPs baseados em algumas pequenas regras listadas abaixo:

1. O CEP é um número maior que 100.000 e menor que 999999
2. O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares
  121426 # Aqui, 1 é um dígito repetitivo alternado em par.
  523563 # Aqui nenhum digito é alternado.
  552523 # Aqui os números 2 e 5 são dígitos alternados repetitivos em par.
  112233 # Aqui nenhum dígito é repetitivo alternado em par.

Você deve desenvolver isto utilizando Python e TDD. Damos preferência a soluções utilizando REGEX e string slicing. Pode-se criar uma interface Web, TK ou ainda no próprio terminal! Queremos ver sua lógica de programação!

Por favor, não coloque este enunciado em seu repositório Git, e também não coloque o nome da empresa. Outros candidatos, se procurarem, acharão e copiarão sua resposta, por isso, evite estas práticas.
