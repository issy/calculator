from main import do_operation

OPERATION = "3"  # Multiplication operation


def test_two_positive_ints():
    assert do_operation(5, OPERATION, 7) == 35


def test_positive_and_negative_ints():
    assert do_operation(5, OPERATION, -3) == -15


def test_two_negative_ints():
    assert do_operation(-7, OPERATION, -5) == 35


def test_float_and_int_both_positive():
    assert do_operation(5.7, OPERATION, 16) == 91.2


def test_negative_float_and_positive_int():
    assert do_operation(-2.56, OPERATION, 7) == -17.92


def test_float_and_int_both_negative():
    assert do_operation(-7.6, OPERATION, -10) == 76


def test_two_positive_floats():
    assert do_operation(6.2, OPERATION, 8.9) == 55.18000000000001


def test_two_negative_floats():
    assert do_operation(-7.8, OPERATION, -3.5) == 27.3
