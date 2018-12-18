import main
import pytest
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


def test_get_encryption_number():
    """Encryption key is calculated"""
    assert main.get_encryption_key(14) == 5
    assert main.get_encryption_key(10) == 3
    with pytest.raises(ValueError):
        assert main.get_encryption_key(6)
    with pytest.raises(ValueError):
        assert main.get_encryption_key(33.3)
