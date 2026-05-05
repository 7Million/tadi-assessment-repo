import pytest
from step1_self_trial import (
    find_first_illegal_character,
    find_corrupted_lines,
    calculate_syntax_error_score,
)


class TestFindFirstIllegalCharacter:
    def test_balanced_line_returns_none(self):
        assert find_first_illegal_character("([])") is None

    def test_nested_balanced_returns_none(self):
        assert find_first_illegal_character("{[()]}") is None

    def test_empty_string_returns_none(self):
        assert find_first_illegal_character("") is None

    def test_only_opening_chars_returns_none(self):
        assert find_first_illegal_character("(([]") is None

    def test_mismatched_closing_returns_char(self):
        assert find_first_illegal_character("[)") == ")"

    def test_closing_with_empty_stack_returns_char(self):
        assert find_first_illegal_character(")") == ")"

    def test_returns_first_error_among_multiple(self):
        assert find_first_illegal_character("([)]") == ")"

    def test_complex_mismatch(self):
        assert find_first_illegal_character("{([(<{}[<>[]}>{[]{[(<()>") == "}"

    def test_angle_bracket_mismatch(self):
        assert find_first_illegal_character("<{([([[(<>()){}]>(<<{{") == ">"

    def test_deeply_nested_valid(self):
        assert find_first_illegal_character("(((({<>}<{<{<>}{[]{[]{}") is None


class TestFindCorruptedLines:
    def test_mixed_valid_and_corrupted(self):
        lines = [
            "[({(<(())[]>[[{[]{<()<>",
            "[(()[<>])]({[<{<<[]>>(",
            "{([(<{}[<>[]}>{[]{[(<()>",
        ]
        result = find_corrupted_lines(lines)
        assert len(result) == 1
        assert result[0][0] == 3  # line number
        assert result[0][2] == "}"  # illegal char

    def test_all_valid_returns_empty(self):
        lines = ["([])", "{[()]}", "(([]))"]
        assert find_corrupted_lines(lines) == []

    def test_all_corrupted(self):
        lines = [")", "([)", "}{"]
        result = find_corrupted_lines(lines)
        assert len(result) == 3

    def test_empty_list(self):
        assert find_corrupted_lines([]) == []

    def test_line_numbers_are_one_indexed(self):
        lines = ["([]", ")"]
        result = find_corrupted_lines(lines)
        assert len(result) == 1
        assert result[0][0] == 2


class TestCalculateSyntaxErrorScore:
    def test_single_corrupted_line(self):
        corrupted = [(1, "[)", ")")]
        total, details = calculate_syntax_error_score(corrupted)
        assert total == 3
        assert details == [(1, ")", 3)]

    def test_multiple_corrupted_lines(self):
        corrupted = [
            (1, "[)", ")"),
            (2, "{[}]", "}"),
            (3, "[>]", ">"),
        ]
        total, details = calculate_syntax_error_score(corrupted)
        assert total == 3 + 107 + 10037
        assert len(details) == 3

    def test_empty_list_returns_zero(self):
        total, details = calculate_syntax_error_score([])
        assert total == 0
        assert details == []

    def test_score_for_square_bracket(self):
        corrupted = [(1, "([)", "]")]
        total, details = calculate_syntax_error_score(corrupted)
        assert total == 11

    def test_full_sample_data(self):
        lines = [
            "[({(<(())[]>[[{[]{<()<>",
            "[(()[<>])]({[<{<<[]>>(",
            "{([(<{}[<>[]}>{[]{[(<()>",
            "(((({<>}<{<{<>}{[]{[]{}",
            "[[<[([]))<([[{}[[()]]]",
            "[{[{({}]{}}([{[{{{}}([]",
            "{<[[]]>}<{[{[{(){()[[[",
            "[<(<(<(<{}))><([]([]()",
            "<{([([[(<>()){}]>(<<{{",
            "<{([{{}}[<[[[<>{}]]]>[]]",
        ]
        corrupted = find_corrupted_lines(lines)
        total, _ = calculate_syntax_error_score(corrupted)
        assert total == 10161
