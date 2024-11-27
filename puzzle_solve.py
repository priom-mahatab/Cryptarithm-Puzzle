def puzzle_solve(k, s, u, puzzle):
    """
    :param k: integer
    :param s: sequence
    :param u: set
    :param puzzle: list of words
    :return: s
    """
    if k == 0:
        letters = list("".join(puzzle))

        unique_letters = sorted(set(letters))
        mapping = {}

        # assigns values to the letters of the puzzle
        for i in range(len(s)):
            letter = unique_letters[i]
            mapping[letter] = s[i]

        # checks if any word has the initial letter as 0
        for word in puzzle:
            if mapping[word[0]] == 0:
                return None

        if is_valid_solution(mapping, puzzle):
            return mapping

        return None

    else:
        for digit in list(u):
            s.append(digit)
            u.remove(digit)
            result = puzzle_solve(k-1, s, u, puzzle)

            if result:
                return result
            else:
                s.remove(digit)
                u.add(digit)

def is_valid_solution(mapping, puzzle):
    
    # converts string to number
    def to_number(string):
        number = ""
        for char in string:
            number += str(mapping[char])
        return int(number)

    words = puzzle[:-1]
    result = puzzle[-1]

    left_val = 0
    for word in words:
        left_val += to_number(word)

    if left_val == to_number(result):
        return True
    
    return False

def main():
    puzzle = ("SEND", "MORE", "MONEY")
    letters = set("".join(puzzle))
    if len(letters) > 10:
        print("Too large to solve")
        return
    s = []
    u = set(range(10))

    solution = puzzle_solve(len(letters), s, u, puzzle)
    if solution:
        print("Solution found")
        for letter, digit in solution.items():
            print(f"{letter} = {digit}")
    else:
        print("No solution")

if __name__ == "__main__":
    main()
    
        