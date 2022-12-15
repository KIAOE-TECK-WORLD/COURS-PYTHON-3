# Ecriture d'un module python

import pathlib
from typing import Union


def read_file(path: pathlib.PosixPath) -> str:
    with open(path, 'r') as f:
        data = f.read()
        f.close()
    return data


def write_file(path: pathlib.PosixPath, data: str) -> None:
    with open(path, 'w') as f:
        f.write(data.strip())
        f.close()


def treat_file(
    path: pathlib.PosixPath,
    mode="r",
    data: str = None
) -> Union[str, None]:
    if mode == "r":
        return read_file(path=path)
    else:
        write_file(path=path, data=data)
