# Queue Design

`TriageQueue` uses Python's `heapq` because the next patient is selected by
priority, not simply by arrival time. Each heap entry contains the triage level,
an increasing enqueue sequence, and the patient. Since level 1 is the highest
priority, lower level numbers sort first. The sequence number makes equal-level
patients FIFO and prevents Python from needing to compare patient objects.

When a level-1 patient joins while level-2 or level-3 patients are waiting, the
heap places that patient ahead of them automatically. Existing patients are not
re-sorted or interrupted: the patient currently being attended to has already
been removed from the waiting queue. Triage priority does not change over time.

`enqueue` adds one patient and `dequeue` removes the next patient to be attended.
`peek`, `list_queue`, and `stats` only inspect the queue; listing sorts a copy
of the heap entries and does not change the underlying queue. Keeping removal in
`dequeue` means that viewing or checking the queue cannot mark a patient as
served or cause them to be processed twice. The simulator is single-threaded,
so each menu action completes before the next one begins. If a level-1 patient
arrives while another patient is already being attended, the new patient moves
ahead of the remaining level-2 and level-3 patients but does not interrupt the
patient already called. A multi-worker version would need to make queue updates
and dequeue claims atomic, for example with a lock, so two workers cannot claim
the same patient. Thread-safe concurrent access and persistent storage are
outside this simulator's scope.