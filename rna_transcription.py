# простенькая домашка из вуза на транскрибирование ДНК в РНК
# Simple homework from university on DNA transcription to RNA


def to_rna(dna_strand):
    rna_strand = ''
    """Computes the result of RNA transcription
    :param dna_strand: DNA string consisting of characters ACGT
    :return: RNA string consisting of characters UGCA
    """
    map = {
            "A":"U",
            "C":"G",
            "G":"C",
            "T":"A"
    }

    return ''.join(map[ch] for ch in dna_strand)
