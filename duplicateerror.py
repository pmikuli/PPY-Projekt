class DuplicateEventException(Exception):
    def __init__(self):
        super().__init__("A similar event already exists in the calendar")
