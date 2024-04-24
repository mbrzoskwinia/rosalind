from id_fib import fib


def test_fib() -> None:
    # given
    n = 5
    k = 3

    # when
    result = fib.fib(n, k)

    # then
    expected = 19
    assert result == expected
