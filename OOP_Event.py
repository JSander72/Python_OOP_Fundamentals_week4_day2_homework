



### Task 2: Event Management System Enhancement

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = 0  # Initialize participant count to 0

    def add_participant(self):
        self.participants += 1

    def get_participant_count(self):
        return self.participants

event = Event("Music Festival", "2024-08-15")

event.add_participant()
event.add_participant()
event.add_participant()

print(f"Total Participants: {event.get_participant_count()}")
