tabuleiro = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

# Exibindo o tabuleiro de forma organizada
for linha in tabuleiro:
    print("| ".join(linha))