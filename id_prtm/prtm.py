MONOISOTOPIC_MASS_TABLE = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}


def calculate(amino_acid_sequence: str) -> float:
    """
    Calculates the total molecular weight of a protein sequence.

    Args:
    - amino_acid_sequence (str): The sequence of amino acids for which the molecular weight is to be calculated.

    Returns:
    - weight (float): The total molecular weight of the protein sequence, rounded to 3 decimal places.
    """
    weight = 0.0
    for aa in amino_acid_sequence:
        weight += MONOISOTOPIC_MASS_TABLE[aa]

    return round(weight, 3)
