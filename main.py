
"""
Module pour tester la primalité d'un nombre et afficher les nombres premiers inférieurs à 100.
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Détermine si un entier est un nombre premier.
    Args:
        p (int): Nombre à tester.
    Returns:
        bool: True si p est premier, False sinon.
    """
    if p <= 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, int(sqrt(p)) + 1, 2):
        if p % i == 0:
            return False
    return True

#### Fonction principale


def main():

    """
    Fonction principale pour tester la fonction isprime et afficher les nombres premiers < 100.
    """
    # Tests simples de la fonction isprime
    print("Tests de isprime :")
    print("isprime(0) :", isprime(0))      # False
    print("isprime(1) :", isprime(1))      # False
    print("isprime(2) :", isprime(2))      # True
    print("isprime(3) :", isprime(3))      # True
    print("isprime(4) :", isprime(4))      # False
    print("isprime(17) :", isprime(17))    # True
    print("isprime(18) :", isprime(18))    # False

    print("\nNombres premiers < 100 :")
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()

    print()


if __name__ == "__main__":
    main()
