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

def find_corrupted_lines(lines):
    """
    Returns a list of corrupted lines with their first illegal character.
    """
    corrupted = []
    for i, line in enumerate(lines, 1):
        illegal_char = find_first_illegal_character(line)
        if illegal_char:
            corrupted.append((i, line, illegal_char))
    return corrupted

def calculate_syntax_error_score(corrupted_lines):
    """
    Calculates the aggregated syntax error score for corrupted lines.
    """
    scores = {
        ')': 3,
        ']': 11,
        '}': 107,
        '>': 10037
    }
    
    total_score = 0
    score_details = []
    
    for line_num, line, illegal_char in corrupted_lines:
        char_score = scores[illegal_char]
        total_score += char_score
        score_details.append((line_num, illegal_char, char_score))
    
    return total_score, score_details

def main():
    block_input = [
        "[({(<(())[]>[[{[]{<()<>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{(){()[[[",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]"
    ]
    
    print("Analyzing instruction subsystem for corrupted lines...")
    print("=" * 60)
    
    corrupted_lines = find_corrupted_lines(block_input)
    
    if corrupted_lines:
        print(f"Found {len(corrupted_lines)} corrupted line(s):")
        print("-" * 40)
        for line_num, line, illegal_char in corrupted_lines:
            print(f"Line {line_num}: {line}")
            print(f"  First illegal character: '{illegal_char}'")
        
        total_score, score_details = calculate_syntax_error_score(corrupted_lines)
        
        print("\nScore breakdown:")
        print("-" * 20)
        for line_num, illegal_char, char_score in score_details:
            print(f"Line {line_num}: '{illegal_char}' = {char_score} points")
        
        print(f"\nTotal error score: {total_score}")
    else:
        print("No corrupted lines found.")
    
    print("=" * 60)
    # print(f"Analysis complete. {len(corrupted_lines)} out of {len(block_input)} lines are corrupted.")

if __name__ == "__main__":
    main()
