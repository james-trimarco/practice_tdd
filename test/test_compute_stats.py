from practicetdd.refactoring_legacy_code.compute_stats import read_ints, count
from pathlib import Path
import pytest


class TestReadInts:
    def test_read_ints_is_function(self):
        """Confirms existence and callabilityof function."""
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
    def test_read_ints_is_function(self):
        """Confirms existence and callabilityof function."""
        assert callable(count)

    def test_count_returns_int(self):
        """The function count() should return an integer."""
        # setup
        file_name = Path.cwd() / "test" / "test_nums.txt"
        data = read_ints(file_name)
        # execution
        counted = count(data)
        # validation
        assert isinstance(counted, int)
