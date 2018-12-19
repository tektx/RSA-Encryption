import main
import pytest
from unittest import mock
import sympy


def test_get_nth_prime():
    """Prime numbers are generated"""
    assert sympy.prime(4) == 7
    assert sympy.prime(9999999) == 179424671
    with pytest.raises(ValueError):
        assert sympy.prime(0)


def test_get_totatives():
    """Totatives of n are calculated"""
    assert main.get_totatives(9) == [1, 2, 4, 5, 7, 8]
    assert main.get_totatives(15) == [1, 2, 4, 7, 8, 11, 13, 14]
    with pytest.raises(ValueError):
        assert main.get_totatives(0)
    with pytest.raises(ValueError):
        assert main.get_totatives(50.5)


def test_get_encryption_key():
    """Encryption key is calculated"""
    assert main.get_encryption_key(14, [1, 3, 5, 9, 11, 13]) == 5
    assert main.get_encryption_key(10, [1, 3, 7, 9]) == 3
    with pytest.raises(ValueError):
        assert main.get_encryption_key(6, [1, 5])
    with pytest.raises(ValueError):
        assert main.get_encryption_key(33.3, [])


def test_get_decryption_key():
    """Decryption key is calculated"""
    assert main.get_decryption_key(5, 6) == 5
    with mock.patch('random.randint', return_value=2):
        assert main.get_decryption_key(5, 6, True) == 11
