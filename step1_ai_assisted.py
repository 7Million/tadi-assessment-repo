def solve_syntax_scoring(data_string):
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    # Scoring for Part 1 (Corrupted)
    error_points = {')': 3, ']': 11, '}': 107, '>': 10037}
    # Scoring for Part 2 (Incomplete)
    completion_points = {')': 1, ']': 2, '}': 3, '>': 4}
    
    total_error_score = 0
    completion_scores = []

    for line in data_string.strip().split('\n'):
        stack = []
        is_corrupted = False
        for char in line.strip():
            if char in pairs:
                stack.append(pairs[char])
            elif not stack or char != stack.pop():
                total_error_score += error_points[char]
                is_corrupted = True
                break
        
        # Only process completion score for NON-corrupted lines
        if not is_corrupted and stack:
            score = 0
            for char in reversed(stack):
                score = (score * 5) + completion_points[char]
            completion_scores.append(score)

    # The middle score of the sorted list
    completion_scores.sort()
    median_score = completion_scores[len(completion_scores) // 2]
    
    return total_error_score, median_score


raw_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


result = solve_syntax_scoring(raw_input)
print("=" * 60)
print(f"Syntax Scoring Error Score: {result[0]}")
print(f"Aggregation Score: {result[1]}")
print("=" * 60)
