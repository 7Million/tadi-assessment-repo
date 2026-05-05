def solve_timmy_instruction(data):
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    # Step 2 Scoring Rules
    completion_points = {')': 11, ']': 13, '}': 17, '>': 19}
    
    scores = []
    
    for line in data.strip().split('\n'):
        stack = []
        corrupted = False
        for char in line.strip():
            if char in pairs:
                stack.append(pairs[char])
            elif not stack or char != stack.pop():
                corrupted = True
                break
        
        # Discard corrupted; process incomplete lines
        if not corrupted and stack:
            line_score = 0
            # Step 2 Logic: Reverse stack, multiply by 7, add points
            for char in reversed(stack):
                line_score = (line_score * 7) + completion_points[char]
            scores.append(line_score)
            
    # Sort and pick the middle score
    scores.sort()
    return scores[len(scores) // 2]


full_dataset = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

print(solve_timmy_instruction(full_dataset))
