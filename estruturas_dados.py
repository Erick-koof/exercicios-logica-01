# Tipos primitivos de dados em python

# - int: números inteiros
# - float: números decimas (ponto flutuante)
# - str: cadeia de caracteres (texto)
# - bool: valores lógicos (True ou False)

x = 5
type(x)
print(type(x))

x1 = 5.1
type(x1)
print(type(x1))

x2 = 'texto'
type(x2)
print(type(x2))

x3 = True
type(x3)
print(type(x3))

#=============================================================#

# Operadores aritméticos: +, -, *, /, //, %, **
# Operadores lógicos: and, or, not
# Operadores de strings: +, *, in, not in, [], [:], %, {}, f""
# Operadores de comparação: ==, !=, >, <, >=, <=
# Operadores bit a bit: &, |, ^, ~, <<, >>


# ============================================================
# TABELA DE OPERADORES EM PYTHON
# Salve como operadores.py ou operadores.md
# ============================================================

# TABELA_OPERADORES = r"""
# # 🔢 OPERADORES ARITMÉTICOS
# | Símbolo | Nome                  | Exemplo  | Resultado |
# |:-------:|:----------------------|:---------|:----------|
# | `+`     | Adição                | `5 + 3`  | `8`       |
# | `-`     | Subtração             | `5 - 3`  | `2`       |
# | `*`     | Multiplicação         | `5 * 3`  | `15`      |
# | `/`     | Divisão (float)       | `10 / 4` | `2.5`     |
# | `//`    | Divisão inteira       | `10 // 4`| `2`       |
# | `%`     | Módulo (resto)        | `10 % 4` | `2`       |
# | `**`    | Exponenciação         | `2 ** 3` | `8`       |

# # 🧠 OPERADORES LÓGICOS (booleanos)
# | Símbolo | Nome         | Exemplo          | Resultado |
# |:-------:|:-------------|:-----------------|:----------|
# | `and`   | E lógico     | `True and False` | `False`   |
# | `or`    | OU lógico    | `True or False`  | `True`    |
# | `not`   | NÃO lógico   | `not True`       | `False`   |

# # ⚖️ OPERADORES DE COMPARAÇÃO (retornam True/False)
# | Símbolo | Nome             | Exemplo  | Resultado |
# |:-------:|:-----------------|:---------|:----------|
# | `==`    | Igual a          | `5 == 5` | `True`    |
# | `!=`    | Diferente de     | `5 != 3` | `True`    |
# | `>`     | Maior que        | `5 > 3`  | `True`    |
# | `<`     | Menor que        | `5 < 3`  | `False`   |
# | `>=`    | Maior ou igual   | `5 >= 5` | `True`    |
# | `<=`    | Menor ou igual   | `4 <= 3` | `False`   |

# # ⚙️ OPERADORES BIT A BIT (bitwise)
# | Símbolo | Nome                | Regra                          | Exemplo    | Resultado |
# |:-------:|:--------------------|:-------------------------------|:-----------|:----------|
# | `&`     | AND bit a bit       | 1 só se ambos forem 1          | `5 & 3`    | `1`       |
# | `|`     | OR bit a bit        | 1 se pelo menos um for 1       | `5 | 3`    | `7`       |
# | `^`     | XOR bit a bit       | 1 se os bits forem diferentes  | `5 ^ 3`    | `6`       |
# | `~`     | NOT bit a bit       | inverte todos os bits          | `~5`       | `-6`      |
# | `<<`    | Shift left (×2)     | desloca bits à esquerda        | `5 << 1`   | `10`      |
# | `>>`    | Shift right (÷2)    | desloca bits à direita         | `5 >> 1`   | `2`       |

# # 📝 OPERADORES E MÉTODOS DE STRING
# | Símbolo/Método | Nome               | Exemplo                        | Resultado        |
# |:--------------:|:-------------------|:-------------------------------|:-----------------|
# | `+`            | Concatenação       | `"Olá" + " mundo"`             | `"Olá mundo"`    |
# | `*`            | Repetição          | `"ab" * 3`                     | `"ababab"`       |
# | `in`           | Pertence           | `"mundo" in "Olá mundo"`       | `True`           |
# | `not in`       | Não pertence       | `"xyz" not in "Olá"`           | `True`           |
# | `[]`           | Indexação          | `"Python"[0]`                  | `"P"`            |
# | `[:]`          | Fatiamento (slice) | `"Python"[1:4]`                | `"yth"`          |
# | `%`            | Formatação antiga  | `"Nome: %s" % "Ana"`           | `"Nome: Ana"`    |
# | `{}`           | `.format()`        | `"Nome: {}".format("Ana")`     | `"Nome: Ana"`    |
# | `f"..."`       | f-string (3.6+)    | `f"Nome: {nome}"`              | `"Nome: Ana"`    |

# # 🎯 OPERADORES DE ATRIBUIÇÃO COMPOSTA
# | Símbolo | Equivale a     | Exemplo    |
# |:-------:|:---------------|:-----------|
# | `=`     | atribuição     | `x = 5`    |
# | `+=`    | `x = x + y`    | `x += 2`   |
# | `-=`    | `x = x - y`    | `x -= 2`   |
# | `*=`    | `x = x * y`    | `x *= 2`   |
# | `/=`    | `x = x / y`    | `x /= 2`   |
# | `//=`   | `x = x // y`   | `x //= 2`  |
# | `%=`    | `x = x % y`    | `x %= 2`   |
# | `**=`   | `x = x ** y`   | `x **= 2`  |
# | `&=`    | `x = x & y`    | `x &= 2`   |
# | `|=`    | `x = x | y`    | `x |= 2`   |
# | `^=`    | `x = x ^ y`    | `x ^= 2`   |
# | `<<=`   | `x = x << y`   | `x <<= 2`  |
# | `>>=`   | `x = x >> y`   | `x >>= 2`  |

# # 🏆 PRECEDÊNCIA (do MAIOR para o MENOR)
# 1. `()`                          parênteses
# 2. `**`                          exponenciação
# 3. `~ +x -x`                     unários (bit a bit NOT, mais, menos)
# 4. `* / // %`                    multiplicação, divisão, módulo
# 5. `+ -`                         soma e subtração
# 6. `<< >>`                       shifts
# 7. `&`                           AND bit a bit
# 8. `^`                           XOR bit a bit
# 9. `|`                           OR bit a bit
# 10. `== != > < >= <= in not in`  comparações
# 11. `not`                        NÃO lógico
# 12. `and`                        E lógico
# 13. `or`                         OU lógico
# """

# if __name__ == "__main__":
#     print(TABELA_OPERADORES)






#=============================================================#
#converte dados em tipos defferente

x4 = 5.7 # aqui ele é float
int(x4)  # aqui eu converti ele para inteiro
print(type(x4))

#=============================================================#
#qualquer valor que não seja o zero para estrig ele é considerado verdadeiro

x5 = bool('njnjfnd')
print(x5)