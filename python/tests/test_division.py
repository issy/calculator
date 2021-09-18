from main import do_operation

OPERATION = "4"  # Division operation


def test_two_positive_ints():
    assert do_operation(5, OPERATION, 7) == 0.7142857142857143


def test_positive_and_negative_ints():
    assert do_operation(5, OPERATION, -3) == -1.6666666666666667


def test_two_negative_ints():
    assert do_operation(-7, OPERATION, -5) == 1.4


def test_float_and_int_both_positive():
    assert do_operation(5.7, OPERATION, 16) == 0.35625


def test_negative_float_and_positive_int():
    assert do_operation(-2.56, OPERATION, 7) == -0.3657142857142857


def test_float_and_int_both_negative():
    assert do_operation(-7.6, OPERATION, -10) == 0.76


def test_two_positive_floats():
    assert do_operation(6.2, OPERATION, 8.9) == 0.6966292134831461


def test_two_negative_floats():
    assert do_operation(-7.8, OPERATION, -3.5) == 2.2285714285714286
