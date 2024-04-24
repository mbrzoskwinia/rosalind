from id_iprb.iprb import probabilities


def test_iprb() -> None:
    # given
    population = [2, 2, 2]

    # when
    result = probabilities(2, 2, 2)

    # then
    expected = 0.78333
    assert result == expected
