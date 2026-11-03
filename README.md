# Triage Queue - Priority Queue Manager

A small Python terminal simulator for a hospital emergency-room waiting queue.
Patients are served by triage level (1 is highest priority, 3 is lowest), with
patients at the same level served in the order they arrived in the queue.

## Run

Requires Python 3.9 or later. No external packages are needed.

```bash
python main.py
```

Use the menu to add a patient, call the next patient, view the waiting queue,
view counts by triage level, or exit. Arrival timestamps are recorded when a
patient is added. Invalid levels and attempts to call from an empty queue are
reported without closing the program.

The queue model can also be used independently through `Patient` and
`TriageQueue` in `triage_queue.py`. Design details are in [DESIGN.md](DESIGN.md).