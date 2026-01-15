import pytest
from logic_utils import (
    check_guess,
    parse_guess,
    get_range_for_difficulty,
    get_attempt_limit,
    update_score,
)


class TestCheckGuess:
    """Test the check_guess function for correct feedback"""

    def test_winning_guess(self):
        """When guess equals secret, should return 'Win'"""
        outcome, message = check_guess(50, 50)
        assert outcome == "Win"
        assert "🎉" in message

    def test_guess_too_high(self):
        """When guess is greater than secret, should return 'Too High' with 'Go LOWER' hint"""
        outcome, message = check_guess(60, 50)
        assert outcome == "Too High"
        assert "Go LOWER" in message

    def test_guess_too_low(self):
        """When guess is less than secret, should return 'Too Low' with 'Go HIGHER' hint"""
        outcome, message = check_guess(40, 50)
        assert outcome == "Too Low"
        assert "Go HIGHER" in message

    def test_guess_way_too_high(self):
        """Test with guess far above secret"""
        outcome, message = check_guess(100, 10)
        assert outcome == "Too High"
        assert "Go LOWER" in message

    def test_guess_way_too_low(self):
        """Test with guess far below secret"""
        outcome, message = check_guess(5, 90)
        assert outcome == "Too Low"
        assert "Go HIGHER" in message


class TestParseGuess:
    """Test the parse_guess function for input validation"""

    def test_parse_valid_integer(self):
        """Should parse valid integer input"""
        ok, value, error = parse_guess("50")
        assert ok is True
        assert value == 50
        assert error is None

    def test_parse_float_converts_to_int(self):
        """Should convert float to integer"""
        ok, value, error = parse_guess("50.7")
        assert ok is True
        assert value == 50
        assert error is None

    def test_parse_empty_string(self):
        """Should reject empty string"""
        ok, value, error = parse_guess("")
        assert ok is False
        assert value is None
        assert error is not None

    def test_parse_non_numeric(self):
        """Should reject non-numeric input"""
        ok, value, error = parse_guess("abc")
        assert ok is False
        assert value is None
        assert error is not None


class TestDifficultyRanges:
    """Test difficulty range configuration"""

    def test_easy_range(self):
        """Easy difficulty should have range 1-20"""
        low, high = get_range_for_difficulty("Easy")
        assert low == 1
        assert high == 20

    def test_normal_range(self):
        """Normal difficulty should have range 1-50"""
        low, high = get_range_for_difficulty("Normal")
        assert low == 1
        assert high == 50

    def test_hard_range(self):
        """Hard difficulty should have range 1-100"""
        low, high = get_range_for_difficulty("Hard")
        assert low == 1
        assert high == 100


class TestAttemptLimits:
    """Test attempt limit configuration"""

    def test_easy_attempts(self):
        """Easy difficulty should allow 6 attempts"""
        limit = get_attempt_limit("Easy")
        assert limit == 6

    def test_normal_attempts(self):
        """Normal difficulty should allow 8 attempts"""
        limit = get_attempt_limit("Normal")
        assert limit == 8

    def test_hard_attempts(self):
        """Hard difficulty should allow 5 attempts"""
        limit = get_attempt_limit("Hard")
        assert limit == 5


class TestUpdateScore:
    """Test scoring logic"""

    def test_win_first_attempt(self):
        """Winning on first attempt should give maximum points"""
        score = update_score(0, "Win", 0)
        assert score == 90

    def test_win_later_attempt(self):
        """Winning on later attempts gives fewer points"""
        score_attempt_1 = update_score(0, "Win", 0)
        score_attempt_5 = update_score(0, "Win", 4)
        assert score_attempt_5 < score_attempt_1

