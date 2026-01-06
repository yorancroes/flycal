from textual.app import App, ComposeResult
from textual.widgets import Static, Label 

class WeekView(Static):
    HOURS = range(7, 23)
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def compose(self) -> ComposeResult:
        yield Label("", classes="header-corner")

        # Day Headers
        for day in self.DAYS:
            yield Label(day, classes="day-header")

        # Rows
        for hour in self.HOURS:
            # The time label on the left
            time_str = f"{hour:02d}:00"
            yield Label(time_str, classes="time-label")
            
            # The slots for each day
            for day in self.DAYS:
                slot_id = f"slot-{day.lower()}-{hour}"
                yield Static(id=slot_id, classes="calendar-slot")