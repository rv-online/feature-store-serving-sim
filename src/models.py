
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FeatureValue:
    entity_id: str
    feature_name: str
    value: float
    event_ts: int
