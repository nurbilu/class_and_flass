class Pawn:
    def __init__(self, color, position_col, position_row):
        self.color = color
        self.position_col = position_col 
        self.position_row = position_row
        self.is_crowned = False
        
    def kill(self, target):
        print(f"{self.color} pawn at ({self.position_col}, {self.position_row}) kills {target.color} pawn at ({target.position_col}, {target.position_row})")
        target.get_killed()
        
    def get_killed(self):
        print(f"{self.color} pawn at ({self.position_col}, {self.position_row}) was killed")
        
    def crowned(self):
        self.is_crowned = True
        print(f"{self.color} pawn at ({self.position_col}, {self.position_row}) was crowned")
        
    def move(self, new_col, new_row):
        self.position_col = new_col
        self.position_row = new_row
        
p1 = Pawn("white", 1, 2)
p2 = Pawn("black", 4, 5)

p1.move(2, 3)
p2.move(3, 4)
p1.kill(p2)
p2.crowned()