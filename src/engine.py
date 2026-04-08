
from __future__ import annotations

from .models import FeatureValue


def latest_before(features: list[FeatureValue], entity_id: str, as_of_ts: int) -> dict[str, float]:
    chosen: dict[str, FeatureValue] = {}
    for feature in features:
        if feature.entity_id != entity_id or feature.event_ts > as_of_ts:
            continue
        current = chosen.get(feature.feature_name)
        if current is None or feature.event_ts > current.event_ts:
            chosen[feature.feature_name] = feature
    return {name: value.value for name, value in sorted(chosen.items())}


def freshness_score(features: list[FeatureValue], as_of_ts: int) -> float:
    if not features:
        return 0.0
    freshness = [max(0, 100 - (as_of_ts - feature.event_ts)) for feature in features]
    return round(sum(freshness) / len(freshness), 2)
