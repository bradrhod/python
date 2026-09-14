from enum import Enum
from rich import print
from rich.table import Table
from rich.live import Live
from rich.console import Console
from rich.prompt import Prompt
from rich.layout import Layout
from rich.panel import Panel

def main():
    # program main entry point
    print("Staring main")
    game=BowlingGame()
    game.setup_game()
    game.start_game()
    console.print("game over")

class BowlingGame:
    def __init__(self):
#        print("BowlingGame init")
        self.frame=0
        self.console=Console()
        # self.layout=Layout()
        # self.layout.split_column(
        #     Layout(name="header"), 
        #     Layout(name="scores"),
        #     Layout("prmopt"))
        
        # self.layout["header"].update(Panel("Bowling Score Tracker", title="Header"))
        # self.live=Live(self.layout, console=self.console, auto_refresh=False)

    def setup_game(self):
        self.bowlers=int(Prompt.ask("Enter number of bowlers?:"))
        self.bowlers_array=[]
#        print("number of bowlers is:", self.bowlers)
        for i in range (0, self.bowlers):
            bowler_name=Prompt.ask("Enter bowler #"+ str(i) + " name?:")
            self.bowlers_array.append(Bowler(bowler_name))
#        print (self.bowlers_array)
        # self.live.start()
        
    def start_game(self):
        # Main game scoring loop
        for self.frame in range(1,10):
            for bowlerint in range(0,self.bowlers):
                bf_full=False
                for roll in range (0,2):
                    bowler=self.bowlers_array[bowlerint]
                    #if first roll was strike, skip
                    if(bf_full==False):
                        roll_score=int(self.console.input(f"[cyan]{bowler.name}[/] frame {self.frame} roll {roll}: "))
                        bowler.add_score(roll_score)
                        bf_full=bowler.calculate_score()
                        self.print_scorecard()
#                    print("bowler: ", bowler.name, " for frame: ", self.frame, 
#                          "for roll", roll, " total score is:", bowler.frames_array[bowler.frame].total_score)

    def print_scorecard(self):
        table = Table(title="Bowling Scores")
        table.add_column("Bowler")
        for column in range (0,self.frame):
            table.add_column(str(column))
        
        table.add_column("Totals")
        for bowler in range (0,self.bowlers):
            rowtext=[]
            rowtext.append(self.bowlers_array[bowler].name) 
            for frameint in range (0, len(self.bowlers_array[bowler].frames_array)):
                frame=self.bowlers_array[bowler].frames_array[frameint]
                if(frame.status==rollResult.INPROGRESS):
                    scorestr=str(frame.score)+'*'
                else:
                    scorestr=str(frame.score)    
                rowtext.append(scorestr)
            table.add_row(*rowtext)
        self.console.clear()
        self.console.print(table)    
        # self.layout["scores"].update(table)
        # self.live.refresh()
            
 #       print ("done")
        
    def __del__(self):
        print('delete runnning')
        # self.live.stop()


class Bowler:
    def __init__(self, name):
        self.name=name
        self.frames_array=[]
#        self.frames_array.append(Frame())
        self.frame=0
    
    def add_score(self,roll_score):
        cframe=self.frames_array[self.frame]
        cframe.add_score(roll_score)
         # if(self.frames_array[self.frame].full==False):
        #     self.frames_array[self.frame].add_score(roll_score)
        # else: 
        #     self.frame=self.frame+1
        #     self.frames_array.append(Frame())
        #     self.frames_array[self.frame].add_score(roll_score)
    def add_frame(self):
        self.frames_array.append(Frame())
    
    def calculate_score(self):
        # calculate frame score
        # frame=self.frames_array[self.frame]
        # if frame.full==False :
        #     frame.score = frame.score + frame.roll1
        #     frame.total_score = frame.score
        # else:
        #     frame.score = frame.score + frame.roll2
        #     frame.total_score = frame.score
            
        for i in range(len(self.frames_array)):
            cframe=self.frames_array[i]
            if(cframe.score_complete==False):
                if(cframe.roll1==10):
                    #strike handling
                    cframe.status = rollResult.STRIKE
                    extrascore, complete = self.get_next_rolls(i,2)
                    cframe.score_complete=False
                    cframe.score = cframe.roll1 + extrascore
                    cframe.full=True
                elif(cframe.roll==2 & (cframe.roll1+cframe.roll2==10)):
                    #spare handling
                    cframe.score = cframe.roll1
                    cframe.score = cframe.score+cframe.roll2
                    extrascore, complete = self.get_next_rolls(i,1)
                    cframe.score = cframe.score+extrascore
                    cframe.status = rollResult.SPARE
                    cframe.score_complete=True
                    cframe.full=True
                else:
                    if(cframe.roll==1):
                        cframe.score = cframe.roll1
                    else:
                        cframe.score = cframe.roll1+cframe.roll2
                        cframe.score_complete=True
                        cframe.full=True
                        cframe.status = rollResult.OPEN
        
        return cframe.full

    def get_next_rolls(self, frame_index, count):
        # safely get next 'count' rolls after the given frame.  Returns in fliht bonus fraems, and true if frame is fully score,  
        partial_result = True
        # either go to count frames, or length of the self.frames_array
        rolls=[]
        if(frame_index+1+count > len(self.frames_array)):
            length_next = len(self.frames_array)
        else:
            length_next = count
            
        for i in range(1, length_next):
            frame = self.frames_array[i] 
            if(frame.roll1 != -1):
                rolls.append(frame.roll1)
            if(len(rolls) < length_next):
                if( frame.roll2 != -1):
                    rolls.append(frame.roll2) 
        if( len(rolls) < count):
            # ran to end of frames before getting the count rolls, return a partial result.
            complete = True            
        else: 
            complete = False
            
        return sum(rolls), complete         
        
    def __repr__(self):
        return f"Bowler('{self.name}')"

class rollResult(Enum):
    INPROGRESS = "inProgress"
    SPARE = "spare"
    STRIKE = "strike"
    OPEN = "open"        
    
class Frame: 
    def __init__(self):
        self.roll1=-1
        self.roll2=-1
        self.roll=0
        self.full=False
        self.score=0
        self.total_score=0
        self.score_complete=False
        self.status=rollResult.INPROGRESS
        return

    def add_score(self,roll_score):
        self.roll=self.roll+1
        if(self.roll==1):
            self.roll1=roll_score
        else:
            self.roll2=roll_score
            self.full=True
            
            
        

if __name__ == "__main__":
    main()
