from id_prtm import prtm


def test_prtm() -> None:
    # given
    aa_sequence = "SKADYEK"

    # when
    result = prtm.calculate(aa_sequence)

    # then
    expected = 821.392
    assert result == expected
