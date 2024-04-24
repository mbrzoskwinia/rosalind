from id_rna import rna


def test_rna() -> None:
    # given
    dna_string = "GATGGAACTTGACTACGTAAATT"

    # when
    result = rna.transcribe(dna_string)

    # then
    expected = "GAUGGAACUUGACUACGUAAAUU"
    assert result == expected
