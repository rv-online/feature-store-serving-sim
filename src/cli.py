
from __future__ import annotations

import json

from .engine import freshness_score, latest_before
from .models import FeatureValue


def main() -> None:
    values = [
        FeatureValue("user-1", "click_rate", 0.42, 100),
        FeatureValue("user-1", "spend_30d", 88.0, 101),
        FeatureValue("user-1", "click_rate", 0.51, 103),
    ]
    print(json.dumps({
        "online_features": latest_before(values, "user-1", 103),
        "freshness_score": freshness_score(values, 110),
    }, indent=2))


if __name__ == "__main__":
    main()
