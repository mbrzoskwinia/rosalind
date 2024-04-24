
def complement(dna_string: str) -> str:
    """
    Generate the complementary DNA sequence for a given DNA sequence.

    Args:
    - dna_string (str): The input DNA sequence.

    Returns:
    - str: The complementary DNA sequence, obtained by replacing each nucleotide with its complementary base
           and reversing the resulting string.
    """
    complementary_string = ""
    for nucleotide in dna_string:
        if nucleotide == 'T':
            complementary_string += 'A'
        elif nucleotide == 'A':
            complementary_string += 'T'
        elif nucleotide == 'C':
            complementary_string += 'G'
        elif nucleotide == 'G':
            complementary_string += 'C'
    return complementary_string[::-1]
