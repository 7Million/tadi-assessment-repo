import pytest
from step2_self_trial import (
    find_first_illegal_character,
    get_completion_score_for_line,
    calculate_completion_score,
    solve_timmy_instruction,
)


class TestFindFirstIllegalCharacter:
    def test_balanced_line_returns_none(self):
        assert find_first_illegal_character("([])") is None

    def test_corrupted_line_returns_char(self):
        assert find_first_illegal_character("[[<[([]))<([[{}[[()]]]") == ")"


class TestGetCompletionScoreForLine:
    def test_incomplete_line_returns_score(self):
        assert get_completion_score_for_line("((({<>}<{<{<>}{[]{[]{}") == 16367558

    def test_corrupted_line_returns_none(self):
        assert get_completion_score_for_line("[[<[([]))<([[{}[[()]]]") is None

    def test_fully_balanced_line_returns_none(self):
        assert get_completion_score_for_line("([])") is None

    def test_another_incomplete_line(self):
        assert get_completion_score_for_line("{<[[]]>}<{[{[{(){()[[[]") == 87972043

    def test_simple_incomplete(self):
        score = get_completion_score_for_line("(")
        assert score == 11

    def test_line_with_whitespace(self):
        assert get_completion_score_for_line("  [({  ") is not None


class TestCalculateCompletionScore:
    def test_example_completion_string(self):
        assert calculate_completion_score("}]>})]}") == 2270621

    def test_empty_string_returns_zero(self):
        assert calculate_completion_score("") == 0

    def test_single_char(self):
        assert calculate_completion_score(")") == 11

    def test_single_bracket(self):
        assert calculate_completion_score("]") == 13

    def test_single_brace(self):
        assert calculate_completion_score("}") == 17

    def test_single_angle(self):
        assert calculate_completion_score(">") == 19

    def test_scoring_formula(self):
        assert calculate_completion_score("))") == (0 * 7 + 11) * 7 + 11


class TestSolveTimmyInstruction:
    def test_full_sample_dataset(self):
        data = "[({(<(())[]>[[{[]{<()<>>\n[(()[<>])]({[<{<<[]>>(\n{([(<{}[<>[]}>{[]{[(<()>\n((({<>}<{<{<>}{[]{[]{}\n[[<[([]))<([[{}[[()]]]\n[{[{({}]{}}([{[{{{}}([]\n{<[[]]>}<{[{(){()[[[]\n[<(<(<(<{}))><([]([]()\n<{([([[(<>()){}]>(<<{{\n<{([{{}}[<[[[<>{}]]]>[]]"
        result = solve_timmy_instruction(data)
        assert result == 1795351

    def test_single_incomplete_line(self):
        data = "(({{"
        result = solve_timmy_instruction(data)
        expected = get_completion_score_for_line("(({{")
        assert result == expected

    def test_score_sorting_and_middle(self):
        data = "[[<\n{{{"
        scores = []
        for line in data.split("\n"):
            s = get_completion_score_for_line(line)
            if s is not None:
                scores.append(s)
        scores.sort()
        expected = scores[len(scores) // 2]
        assert solve_timmy_instruction(data) == expected
