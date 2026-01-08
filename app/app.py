from textual.app import App, ComposeResult
from textual.widgets import Footer, ContentSwitcher
from app.frontend.monthview import MonthView
from app.frontend.weekview import WeekView


class Calendar(App):
    CSS_PATH = "frontend/css/calendar.css"
    ansi_colors = True

    BINDINGS = [
        ("q", "quit", "Quit the application"),
        ("m", "show_month_view", "Show Month View"),
        ("w", "show_week_view", "Show Week View"),
    ]

    def compose(self) -> ComposeResult:
        with ContentSwitcher(id="view-switcher", initial="week-view"):
            yield MonthView(id="month-view")
            yield WeekView(id="week-view")

        yield Footer()

    def action_show_month_view(self) -> None:
        """Switch to the month view."""
        view_switcher = self.query_one("#view-switcher", ContentSwitcher)
        view_switcher.current = "month-view"

    def action_show_week_view(self) -> None:
        """Switch to the week view."""
        view_switcher = self.query_one("#view-switcher", ContentSwitcher)
        view_switcher.current = "week-view"
