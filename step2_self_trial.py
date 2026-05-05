def find_first_illegal_character(line):
    """
    Returns the first illegal character in a line, or None if line is not corrupted.
    """
    stack = []
    opening_chars = {'(', '[', '{', '<'}
    closing_chars = {')', ']', '}', '>'}
    matching_pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    
    for char in line:
        if char in opening_chars:
            stack.append(char)
        elif char in closing_chars:
            if not stack:
                # Closing character with no opening character
                return char
            expected_opening = matching_pairs[char]
            actual_opening = stack.pop()
            if actual_opening != expected_opening:
                # Mismatched closing character - this is the first illegal character
                return char
    
    # If we reach here, no illegal characters were found
    return None

def get_completion_score_for_line(line):
    """
    Returns the completion score for a line, or None if line is corrupted.
    """
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    completion_points = {')': 11, ']': 13, '}': 17, '>': 19}
    
    stack = []
    corrupted = False
    for char in line.strip():
        if char in pairs:
            stack.append(pairs[char])
        elif not stack or char != stack.pop():
            corrupted = True
            break
    
    # If not corrupted and stack is not empty, calculate completion score
    if not corrupted and stack:
        line_score = 0
        for char in reversed(stack):
            line_score = (line_score * 7) + completion_points[char]
        return line_score
    
    return None

def calculate_completion_score(completion_string):
    """
    Calculates the completion score for a completion string.
    """
    scores = {
        ')': 11,
        ']': 13,
        '}': 17,
        '>': 19
    }
    
    total_score = 0
    for char in completion_string:
        total_score = (total_score * 7) + scores[char]
    
    return total_score

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

def main():
    full_dataset = """[({(<(())[]>[[{[]{<()<>>
                    [(()[<>])]({[<{<<[]>>(
                    {([(<{}[<>[]}>{[]{[(<()>
                    (((({<>}<{<{<>}{[]{[]{}
                    [[<[([]))<([[{}[[()]]]
                    [{[{({}]{}}([{[{{{}}([]
                    {<[[]]>}<{[{[{(){()[[[]
                    [<(<(<(<{}))><([]([]()
                    <{([([[(<>()){}]>(<<{{
                    <{([{{}}[<[[[<>{}]]]>[]]"""
    
    result = solve_timmy_instruction(full_dataset)
    print("=" * 60)
    print(f"Middle completion score: {result}")
    print("=" * 60)
    

if __name__ == "__main__":
    main()
