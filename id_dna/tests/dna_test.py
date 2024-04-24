from id_dna import dna


def test_input_1():
    # given
    dna_sequence = "ACCGGGTTTT"

    # when
    result = dna.count(dna_sequence)

    # then
    expected = "1 2 3 4"
    assert result == expected
