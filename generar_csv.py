import secrets

CANTIDADES = {
    'hacker': 415,
    'mentor': 15,
    'organizacion': 35,
    'patrocinador': 35
}

salida = []
ocupados = set()


for tipo in CANTIDADES:
    curr = 0

    while curr != CANTIDADES[tipo]:
        token = secrets.token_hex(3)

        if token in ocupados:
            continue

        ocupados.add(token)
        salida.append((tipo, token))
        curr += 1


with open('salida.csv', 'w') as file:
    file.write("tipo; valor\n")

    for token in salida:
        file.write(f"{token[0]}; {token[1]}\n")

