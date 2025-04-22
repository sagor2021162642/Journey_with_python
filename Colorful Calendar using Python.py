import calendar
from rich.console import Console
from rich.table import Table

def colorful_calendar(year):
    console = Console()
    calendar.setfirstweekday(calendar.MONDAY)
    months = [calendar.monthcalendar(year, m) for m in range(1, 13)]

    day_cols = [
        ("Mon", "green"), ("Tue", "green"), ("Wed", "green"),
        ("Thu", "green"), ("Fri", "green"), ("Sat", "red"), ("Sun", "red"),
    ]

    for m, weeks in enumerate(months, start=1):
        month_name = calendar.month_name[m]
        table = Table(title=f"[bold cyan]{month_name} {year}[/bold cyan]", show_lines=True)

        for name, style in day_cols:
            table.add_column(name, justify="center", style=style)

        for week in weeks:
            table.add_row(*(str(day) if day else "" for day in week))

        console.print(table)
        console.print()

if __name__ == "__main__":
    colorful_calendar(2025)
