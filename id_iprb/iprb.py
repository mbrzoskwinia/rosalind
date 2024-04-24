def probabilities(dominant, heterozygous, homozygous):
    """
    Calculates the probability of a certain genotype in the offspring population.

    Args:
    - dominant (int): The number of individuals with the dominant genotype.
    - heterozygous (int): The number of individuals with the heterozygous genotype.
    - homozygous (int): The number of individuals with the homozygous genotype.

    Returns:
    - probability (float): The probability of a randomly selected individual possessing a dominant allele.
    """

    total = dominant + heterozygous + homozygous

    # Probabilities
    prob_AA_AA = (dominant / total) * ((dominant - 1) / (total - 1))
    prob_AA_Aa = 2 * (dominant / total) * (heterozygous / (total - 1))
    prob_AA_aa = 2 * (dominant / total) * (homozygous / (total - 1))
    prob_Aa_Aa = (heterozygous / total) * ((heterozygous - 1) / (total - 1)) * 0.75
    prob_Aa_aa = 2 * (heterozygous / total) * (homozygous / (total - 1)) * 0.5
    prob_aa_aa = 0

    probability = prob_AA_AA + prob_AA_Aa + prob_AA_aa + prob_Aa_Aa + prob_Aa_aa + prob_aa_aa
    return round(probability, 5)
