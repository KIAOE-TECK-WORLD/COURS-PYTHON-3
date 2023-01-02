# Resultats [('AISSATA', 28, 300000), ..., ('KUASSI', 28, 100000)]
# fonction map
# fonction filter
# Grace a filter retrouver les users qui ont plus de 100000 comme salaire


import pathlib


def treating(path):
    with open(path, 'r') as file:
        datas = file.readlines()

        for index, value in enumerate(datas):
            datas[index] = value.replace('\n', '').split(',')

            datas[index][1] = int(datas[index][1])
            datas[index][2] = float(datas[index][2])

            datas[index] = tuple(datas[index])

        file.close()

    return datas


def main():

    path = pathlib.Path(__file__).parent / 'salaries.txt'

    datas = treating(path)
    
    print(datas)


if __name__ == '__main__':
    main()

