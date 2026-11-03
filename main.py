from triage_queue import Patient, TriageQueue


def _show_patient(patient: Patient) -> str:
    arrival = patient.arrived_at.strftime("%Y-%m-%d %H:%M:%S")
    return f"{patient.name} (level {patient.triage_level}, arrived {arrival})"


def _add_patient(queue: TriageQueue) -> None:
    name = input("Patient name: ").strip()
    level_text = input("Triage level (1=critical, 2=urgent, 3=standard): ").strip()

    try:
        patient = Patient(name=name, triage_level=int(level_text))
    except ValueError as error:
        print(f"Could not add patient: {error}")
        return

    queue.enqueue(patient)
    print(f"Added {_show_patient(patient)}.")


def _call_next_patient(queue: TriageQueue) -> None:
    try:
        patient = queue.dequeue()
    except IndexError as error:
        print(error)
        return

    print(f"Calling {_show_patient(patient)}.")


def _show_queue(queue: TriageQueue) -> None:
    patients = queue.list_queue()
    if not patients:
        print("No patients are waiting.")
        return

    print("Waiting patients:")
    for position, patient in enumerate(patients, start=1):
        print(f"{position}. {_show_patient(patient)}")


def _show_stats(queue: TriageQueue) -> None:
    counts = queue.stats()
    print("Waiting patients by triage level:")
    print(f"Level 1 (critical): {counts[1]}")
    print(f"Level 2 (urgent): {counts[2]}")
    print(f"Level 3 (standard): {counts[3]}")


def main() -> None:
    queue = TriageQueue()
    actions = {
        "1": ("Add a patient", _add_patient),
        "2": ("Call next patient", _call_next_patient),
        "3": ("View waiting queue", _show_queue),
        "4": ("View queue stats", _show_stats),
    }

    while True:
        print("\nHospital Triage Queue")
        for option, (label, _) in actions.items():
            print(f"{option}. {label}")
        print("5. Exit")

        try:
            choice = input("Select an option: ").strip()
        except EOFError:
            print("\nExiting.")
            return

        if choice == "5":
            print("Goodbye.")
            return

        action = actions.get(choice)
        if action is None:
            print("Invalid option. Choose a number from 1 to 5.")
            continue

        action[1](queue)


if __name__ == "__main__":
    main()