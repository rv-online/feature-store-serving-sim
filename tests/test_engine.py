
import unittest

from src.engine import freshness_score, latest_before
from src.models import FeatureValue


class FeatureStoreTests(unittest.TestCase):
    def test_point_in_time_lookup(self) -> None:
        values = [
            FeatureValue("u1", "ctr", 0.2, 10),
            FeatureValue("u1", "ctr", 0.5, 12),
            FeatureValue("u1", "spend", 10, 11),
        ]
        self.assertEqual(latest_before(values, "u1", 11), {"ctr": 0.2, "spend": 10})

    def test_freshness_score_is_positive(self) -> None:
        values = [FeatureValue("u1", "ctr", 0.2, 90), FeatureValue("u1", "spend", 10, 95)]
        self.assertGreater(freshness_score(values, 100), 0)


if __name__ == "__main__":
    unittest.main()
