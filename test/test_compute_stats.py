from practicetdd.refactoring_legacy_code.compute_stats import (
    average,
    count,
    read_ints,
    summation,
)
from pathlib import Path
import pytest


class TestReadInts:
    def test_read_ints_is_function(self):
        """Confirms existence and callability of read_ints() function."""
        assert callable(read_ints)

    def test_read_ints_returns_list(self):
        """The function read_ints() should return a list."""
        # setup
        file_name = Path.cwd() / "test" / "test_nums.txt"
        # execution
        data = read_ints(file_name)
        # validation
        assert isinstance(data, list)

    def test_read_ints_returns_list_of_ints(self):
        """The list data by read_ints() should contain only ints."""
        # setup
        file_name = Path.cwd() / "test" / "test_nums.txt"
        # execution
        data = read_ints(file_name)
        # validation
        all(isinstance(item, int) for item in data)

    @pytest.mark.parametrize("position,expected_value", [(0, 12), (1, 3), (2, 5)])
    def test_read_ints_returns_correct_values(self, position, expected_value):
        """Tests some known values and positions in the testing data."""
        # setup
        file_name = Path.cwd() / "test" / "test_nums.txt"
        # execution
        data = read_ints(file_name)
        # validation
        assert data[position] == expected_value


class TestCount:
    def test_count_is_function(self):
        """Confirms existence and callability of count() function."""
        assert callable(count)

    def test_count_returns_int(self):
        """The function count() should return an integer."""
        # setup
        file_name = Path.cwd() / "test" / "test_nums.txt"
        data = read_ints(file_name)
        # execution
        integer_count = count(data)
        # validation
        assert isinstance(integer_count, int)

    def test_count_returns_correct_answer(self):
        """The function count() should return expected value for
        the test data."""
        # setup
        file_name = Path.cwd() / "test" / "test_nums.txt"
        data = read_ints(file_name)
        # execution
        integer_count = count(data)
        # validation
        assert integer_count == 5


class TestSummation:
    def test_summation_is_function(self):
        """Confirms existence and callability of summation() function."""
        assert callable(summation)

    def test_count_returns_float(self):
        """The function count() should return an integer."""
        # setup
        file_name = Path.cwd() / "test" / "test_nums.txt"
        data = read_ints(file_name)
        # execution
        sum_of_ints = summation(data)
        # validation
        assert isinstance(sum_of_ints, int)

    def test_summation_returns_correct_answer(self):
        """The function summation() should return expected value for
        the test data."""
        # setup
        file_name = Path.cwd() / "test" / "test_nums.txt"
        data = read_ints(file_name)
        # execution
        sum_of_ints = summation(data)
        # validation
        assert sum_of_ints == 32


class TestAverage:
    def test_average_is_function(self):
        """Confirms existence and callability of summation() function."""
        assert callable(average)

    def test_count_returns_int(self):
        """The function count() should return a float."""
        # setup
        file_name = Path.cwd() / "test" / "test_nums.txt"
        data = read_ints(file_name)
        # execution
        mean_of_ints = average(data)
        # validation
        assert isinstance(mean_of_ints, float)

    def test_summation_returns_correct_answer(self):
        """The function summation() should return expected value for
        the test data."""
        # setup
        file_name = Path.cwd() / "test" / "test_nums.txt"
        data = read_ints(file_name)
        # execution
        mean_of_ints = average(data)
        # validation
        assert mean_of_ints == 6.4