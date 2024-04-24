from id_revc import revc


def test_revc() -> None:
    # given
    dna_string = 'AAAACCCGGT'

    # when
    result = revc.complement(dna_string)

    # then
    expected = 'ACCGGGTTTT'
    assert result == expected
