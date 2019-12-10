# Here's how to make the matrix above from a list of lists
from birdseye import eye
from cheap_repr import register_repr, normal_repr

my_matrix = [[1, 3, 5, 7],
             [2, 3, 4, 5],
             [5, 2, 20, 3]]
register_repr(object)(normal_repr)
register_repr(list)(normal_repr)
register_repr(str)(normal_repr)
# Fill out the 0th row
# Fill out the 1st row
# Fill out the 2nd row


print("[2][0]:", my_matrix[2][0])


# Here is a helper function to print out matrices

def print_matrix(mat):
    s = []
    for i, row in enumerate(mat):
        s.append([str(i), '|'] + [str(f'[  {e} ]') if len(str(e)) == 1 else str(f'[ {e} ]') for e in row])
    lens = []
    for col in zip(*s):
        lens.append(max(map(len, col)))
    fmt = '\t'.join(f'{{:{x}}}' for x in lens)
    heads = ''
    for j in range(len(lens) - 2):
        heads += f'\t\t\t {j}'
    seps = ''
    for j in range(len(lens) - 2):
        seps += f'\t\t\t---'
    table = [heads, seps]
    for row in s:
        table.append(fmt.format(*row))
    print('\n'.join(table), end='\n\n')


print_matrix(my_matrix)

# The format is always my_matrix[row][column].
# Use these values to calculate scores
GAP_PENALTY = -1
MATCH_AWARD = 1
MISMATCH_PENALTY = -1

# Make a score matrix with these two sequences
seq1 = "ATTACA"
seq2 = "ATGCT"


# A function for making a matrix of zeroes
def zeros(rows, cols):
    # Define an empty list
    retval = []
    # Set up the rows of the matrix
    for _ in range(rows):
        # For each row, add an empty list
        retval.append([])
        # Set up the columns in each row
        for _ in range(cols):
            # Add a zero to each column in each row
            retval[-1].append(0)
    # Return the matrix of zeros
    return retval


# A function for determining the score between any two bases in alignment
def match_score(alpha, beta):
    if alpha == beta:
        return MATCH_AWARD
    elif alpha == '-' or beta == '-':
        return GAP_PENALTY
    else:
        return MISMATCH_PENALTY


# The function that actually fills out a matrix of scores
@eye
def needleman_wunsch(sq1, sq2):
    # length of two sequences
    len_1 = len(sq1)
    len_2 = len(sq2)

    # Generate matrix of zeros to store scores
    score = zeros(len_2 + 1, len_1 + 1)

    # Calculate score table

    # Your code goes here

    # Fill out first column
    for i in range(0, len_2 + 1):
        score[i][0] = GAP_PENALTY * i

    # Fill out first row
    for j in range(0, len_1 + 1):
        score[0][j] = GAP_PENALTY * j

    # Fill out all other values in the score matrix
    for i in range(1, len_2 + 1):
        for j in range(1, len_1 + 1):
            # Calculate the score by checking the top, left, and diagonal cells
            match = score[i - 1][j - 1] + match_score(sq1[j - 1], sq2[i - 1])
            delete = score[i - 1][j] + GAP_PENALTY
            insert = score[i][j - 1] + GAP_PENALTY
            # Record the maximum score from the three possible scores calculated above
            score[i][j] = max(match, delete, insert)

    return score


print_matrix(needleman_wunsch(seq1, seq2))
