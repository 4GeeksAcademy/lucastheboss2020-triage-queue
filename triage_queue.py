from __future__ import annotations

import heapq
from dataclasses import dataclass, field
from datetime import datetime
from itertools import count


@dataclass(frozen=True)
class Patient:
    name: str
    triage_level: int
    arrived_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Patient name must not be empty.")
        if (
            isinstance(self.triage_level, bool)
            or not isinstance(self.triage_level, int)
            or self.triage_level not in (1, 2, 3)
        ):
            raise ValueError("Triage level must be 1, 2, or 3.")
        if not isinstance(self.arrived_at, datetime):
            raise TypeError("arrived_at must be a datetime.")


class TriageQueue:
    def __init__(self) -> None:
        self._patients: list[tuple[int, int, Patient]] = []
        self._sequence = count()

    def enqueue(self, patient: Patient) -> None:
        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient instance.")
        heapq.heappush(
            self._patients,
            (patient.triage_level, next(self._sequence), patient),
        )

    def dequeue(self) -> Patient:
        try:
            return heapq.heappop(self._patients)[2]
        except IndexError:
            raise IndexError("The triage queue is empty.") from None

    def peek(self) -> Patient:
        if not self._patients:
            raise IndexError("The triage queue is empty.")
        return self._patients[0][2]

    def list_queue(self) -> list[Patient]:
        return [entry[2] for entry in sorted(self._patients)]

    def stats(self) -> dict[int, int]:
        counts = {level: 0 for level in (1, 2, 3)}
        for triage_level, _, _ in self._patients:
            counts[triage_level] += 1
        return counts