
def transcribe(dna_string: str) -> str:
    """
    Transcribes a DNA sequence into RNA sequence.
    
    Args: 
    - dna_string (str): The DNA sequence to be transcribed.

    Returns:
    - rna_string (str): The RNA sequence obtained by replacing T nucleotides with U.
    """
    rna_string = ""
    for nucleotide in dna_string:
        if nucleotide == 'T':
            rna_string += 'U'
        else:
            rna_string += nucleotide
    return rna_string
