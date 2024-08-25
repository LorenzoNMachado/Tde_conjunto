nome_do_arquivo= ['texto1.txt', 'texto2.txt', 'texto3.txt']

for arquivo in nome_do_arquivo:
    with open(arquivo, 'r') as file:
        lines = file.readlines()
    num_operations = int(lines[0].strip())
    index = 1

    for i in range(num_operations):
        op_code = lines[index].strip()

        set1 = set(lines[index + 1].strip().split(','))
        set2 = set(lines[index + 2].strip().split(','))

        if op_code == 'U':
            result = set1.union(set2)
        elif op_code == 'I':
            result = set1.intersection(set2)
        elif op_code == 'D':
            result = set1.difference(set2)
        elif op_code == 'C':
            result = {(x, y) for x in set1 for y in set2}

        print("Resultado da operação", op_code, "no arquivo", arquivo, ":", result)

        index += 3
