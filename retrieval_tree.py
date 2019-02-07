def trie(seq, k_max, alphabet=['A', 'C', 'G', 'T']):
    """
    Builds a retrieval tree for a given DNA sequence and a given spectrum.

    Returns:
    - tree = a list of dictionaries, indexed by the spectrum length
    """
    tree = []

    # Initialization
    tree.append(_init(seq, alphabet))

    # Recursions
    for k in range(k_max-1):
        tree.append(dict()) # New dictionary, will be updated with respect to subsequences previously spotted
        for subseq in tree[k]:
            index_seqs = tree[k][subseq] # Sequences of indices for a given DNA subsequence
            tree[k+1].update(_recursion(seq, subseq, index_seqs, alphabet))

    return tree


def _init(seq, alphabet):
    """
    """
    roots = dict()
    for i, a in enumerate(seq):
        if a in roots.keys():
            roots[a].append([i]) # New index for this letter
        else:
            roots[a] = [[i]] # New entry in the dictionary

    return roots


def _recursion(seq, subseq, index_seqs, alphabet):
    """
    Returns:
    - leaves: a dictionary. The keys are DNA subsequences of length k+1 and the values are arrays of sequence of indices corresponding to each key.

    """

    # Create a dictionary telling whether a given subsequence has already been spotted or not
    spotted = dict()
    for a in alphabet:
        spotted[a] = False

    leaves = dict()
    # Check every sequence of indices given as argument
    for ind_seq in index_seqs:
        current_ind = ind_seq[len(ind_seq)-1] # Last index in the sequence of indices
        if current_ind < len(seq) - 1: # Otherwise the end of the DNA sequence is reached
            next_ind = current_ind + 1 # Next index to check in the DNA sequence

            for a in alphabet:
                new_subseq = subseq + a
                new_index_seq = ind_seq + [next_ind]
                if seq[next_ind] == a:
                    if spotted[a]: # Add a new sequence of indices to this DNA subsequence
                        leaves[new_subseq].append(new_index_seq)
                    else: # Create a new entry in roots
                        leaves[new_subseq] = [new_index_seq]
                        spotted[a] = True

    return leaves
