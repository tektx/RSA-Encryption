import math
import random
import sympy


def get_totatives(n: int) -> list:
    """ Gets the positive integers up to n that are relatively prime to n, aka Euler's totient function

    Args:
        n (int): Integer to get totatives of

    Returns:
        list: Totatives of n

    """
    if n < 1 or not isinstance(n, int):
        raise ValueError

    totatives = []
    for k in range(1, n+1):
        if math.gcd(n, k) == 1:
            totatives.append(k)
    return totatives


def get_encryption_key(product: int, totatives: list) -> int:
    """ Returns the encryption key

    Args:
        product: Product of two prime numbers
        totatives: Relative prime numbers to the product

    Returns:
        int: Encryption key

    """
    # Assert a minimum value based on the lowest possible prime numbers multiplied together
    # Can't use 6 (2*3) because no number satisfies the conditions 1<e<len(phi(6)) && e in phi(6)
    if product < 10 or not isinstance(product, int):
        raise ValueError

    # Get the upper bound of the encryption number range
    key_range = len(totatives)

    # Get the encryption key
    encryption_key = None
    while encryption_key is None:
        # Key must be in the range 1<e<len(phi(n)) and must be coprime to both n and phi(n)
        # 2 won't satisfy the criteria for any number, so 3 is the lower bound
        rand_int = random.randint(3, key_range-1)
        if math.gcd(rand_int, key_range) == 1 and rand_int in totatives:
            encryption_key = rand_int

    return encryption_key


def get_decryption_key(encryption_key: int, totient: int, randomize: bool = False) -> int:
    """ Returns the decryption key

    Args:
        encryption_key: RSA encryption key
        totient: Number of totatives of the modulus
        randomize: True to randomize the decryption value instead of using the first valid value

    Returns:
        int: RSA decryption key

    """
    decryption_key = None
    temp = 1

    # Use the nth valid value of the decryption key if randomize is True
    nth_value = random.randint(1, 500)  # Use an arbitrary limit for testing purposes
    valid_value_count = 0

    while decryption_key is None:
        # Formula: solve for d where de(mod(phi(n)) = 1. e = encryption key
        if (temp * encryption_key) % totient == 1:
            if randomize:
                valid_value_count += 1
                if valid_value_count >= nth_value:
                    decryption_key = temp
            else:
                decryption_key = temp
        temp += 1

    return decryption_key


def main():
    # Get prime numbers
    # TODO: Use random values to get primes
    prime1 = sympy.prime(1)
    prime2 = sympy.prime(4)

    modulus = prime1 * prime2
    totatives = get_totatives(modulus)
    encryption_key = get_encryption_key(modulus, totatives)
    public_key = (encryption_key, modulus)
    decryption_key = get_decryption_key(encryption_key, len(totatives))
    private_key = (decryption_key, modulus)


if __name__ == '__main__':
    main()
