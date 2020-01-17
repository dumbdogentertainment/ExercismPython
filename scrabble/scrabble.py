one_point_letters = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
two_point_letters = ['D', 'G']
three_point_letters = ['B', 'C', 'M', 'P']
four_point_letters = ['F', 'H', 'V', 'W', 'Y']
five_point_letters = ['K']
eight_point_letters = ['J', 'X']
ten_point_letters = ['Q', 'Z']

def derive_score(word):
    score = 0
    for l in word.upper():
        score += derive_letter_score(l)
    
    return score

def derive_letter_score(letter):
    if letter in one_point_letters:
        return 1
    
    if letter in two_point_letters:
        return 2

    if letter in three_point_letters:
        return 3

    if letter in four_point_letters:
        return 4

    if letter in five_point_letters:
        return 5

    if letter in eight_point_letters:
        return 8

    if letter in ten_point_letters:
        return 10
    
    return 0