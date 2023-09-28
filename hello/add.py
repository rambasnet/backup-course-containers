"""Add module.
"""


import sys
sys.path.append("..")


def add(a, b):
    return a+b


if __name__ == "__main__":
    from utility import util
    print(util.sub(1, 2))
