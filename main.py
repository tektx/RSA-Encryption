import math
import random
import sympy


class RSA:

    def __init__(self):
        self.primes: tuple = None
        self.modulus: int = None
        self.totatives: list = None
        self.encryption_key: int = None
        self.decryption_key: int = None
        self.public_key: tuple = None
        self.private_key: tuple = None

    def get_primes(self):
        """ Generates prime numbers for the public and private key creation

        Returns:

        """
        prime1 = sympy.prime(random.randint(5, 500))  # Use arbitrary min and max primes
        prime2 = sympy.prime(random.randint(5, 500))
        self.primes = (prime1, prime2)
        self.modulus = prime1 * prime2

    def get_encryption_key(self):
        """ Gets the encryption key

        Returns:

        """
        if self.modulus is None:
            self.get_primes()

        # Get the upper bound of the encryption number range
        key_range = len(self.totatives)

        # Get the encryption key
        encryption_key = None
        while encryption_key is None:
            # Key must be in the range 1<e<len(phi(n)) and must be coprime to both n and phi(n)
            # 2 won't satisfy the criteria for any number, so 3 is the lower bound
            rand_int = random.randint(3, key_range - 1)
            if math.gcd(rand_int, key_range) == 1 and rand_int in self.totatives:
                encryption_key = rand_int

        self.encryption_key = encryption_key
        self.public_key = (encryption_key, self.modulus)

    def get_decryption_key(self, randomize: bool = False):
        """ Returns the decryption key

        Args:
            randomize: True to randomize the decryption value instead of using the first valid value

        Returns:

        """
        decryption_key = None
        temp = 1

        # Use the nth valid value of the decryption key if randomize is True
        nth_value = random.randint(1, 500)  # Use an arbitrary limit for testing purposes
        valid_value_count = 0

        while decryption_key is None:
            # Formula: solve for d where de(mod(phi(n)) = 1. e = encryption key
            if (temp * self.encryption_key) % len(self.totatives) == 1:
                if randomize:
                    valid_value_count += 1
                    if valid_value_count >= nth_value:
                        decryption_key = temp
                else:
                    decryption_key = temp
            temp += 1

        self.decryption_key = decryption_key
        self.private_key = (decryption_key, self.modulus)

    def get_totatives(self, n):
        """ Gets the positive integers up to n that are relatively prime to n, aka Euler's totient function

        Args:
            n: Integer to get totatives of

        Returns:

        """
        if n < 1 or not isinstance(n, int):
            raise ValueError

        totatives = []
        for k in range(1, n+1):
            if math.gcd(n, k) == 1:
                totatives.append(k)

        self.totatives = totatives

    def make_keys(self):
        """ Generates public and private keys

        Returns:

        """
        self.get_primes()
        self.get_totatives(self.modulus)
        self.get_encryption_key()
        self.get_decryption_key()


if __name__ == '__main__':
    rsa = RSA()
    rsa.make_keys()
