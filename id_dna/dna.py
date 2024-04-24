def count(sequence: str) -> str:
    """
    Count the occurrences of each nucleotide (A, C, G, T) in a DNA sequence.

    Args:
    - sequence (str): The DNA sequence to be analyzed.

    Returns:
    - str: A string containing the counts of A, C, G, and T nucleotides in the sequence,
           separated by spaces.
    """
    count_a, count_c, count_g, count_t = 0, 0, 0, 0

    for base in sequence:
        if base == 'A':
            count_a += 1
        elif base == 'C':
            count_c += 1
        elif base == 'G':
            count_g += 1
        elif base == 'T':
            count_t += 1

    return f"{count_a} {count_c} {count_g} {count_t}"
