from practicetdd.refactoring_legacy_code.compute_stats import compute_stats


class TestComputeStats:
    def test_compute_stats_is_function(self):
        assert callable(compute_stats)