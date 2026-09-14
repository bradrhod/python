from rich.console import Console
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.prompt import IntPrompt
from rich.prompt import Prompt


def main():
    console = Console()
    
    # layout = Layout()
    # layout.split_column(Layout(name="header"),
    #                     Layout(name="scores"),)
    # layout["header"].update(Panel("Score Tracker", title="Game"))
    
    data = []
    # live = Live(layout, console=console, auto_refresh=False)
    # live.start()    
    
    for i in range(3):
        # Stop live before prompting
#        live.stop()
#        name = Prompt.ask(f"Enter your bowler {i+1} name:")
        name  = console.input(f"[cyan]Enter name {i+1}: [/]")
#        score = IntPrompt.ask(f"Enter bowler {i+1} score:")
        score = int(console.input(f"Enter bowler {i+1} score:"))
#        live.start()

        # Update layout and refresh
        data.append((name, score))
        console.clear()
        console.print(build_table(data))
        # layout["scores"].update(build_table(data))
#        live.refresh()

    live.stop()
    console.print("Game over!")
    
    
def build_table(data):
    table = Table(title="Scores")
    table.add_column("Name")
    table.add_column("Score")
    for name, score in data:
        table.add_row(name, str(score))
    return table
    
    















if __name__ == "__main__":
    main()

