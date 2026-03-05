"""
→ Debugger f-string

def multiplicador(num1: float, num2: float) -> float:
    return num1*num2


resultado: float = multiplicador(4.242,5.42452)

print(f'Resultado {resultado}')

print(f'Resultado {multiplicador(9,4):.2f}')

print(f'{(media := 8/2)} é a metade de {media*2}')
"""

geek: str = 'Geek University'

print(f"geek='{geek}'")

print(f'{geek=}')

print(f'{geek.upper()[::-1]=}')