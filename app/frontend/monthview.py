from textual.widgets import Static, Label, Placeholder
from textual.app import ComposeResult

class MonthView(Static):
    """A widget to display a month view in the application."""

    def compose(self) -> ComposeResult:
        yield Label("Month View", id="title")
        yield Placeholder(id="month-content")