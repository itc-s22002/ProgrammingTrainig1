import random
import math


class Ball:
 
    def __init__(self, canvas, color, paddle):
        
        self.canvas = canvas
        self.paddle = paddle
   
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
   
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        

        self.init_x = self.canvas_width / 2 - 7.5
        self.init_y = self.canvas_height / 2 - 7.5

        self.speed = 0
  
        self.x = 0
        self.y = 0

        self.ans = 0
        self.id_2 = canvas.create_text(250, 10, text=self.ans)
        self.id_3 = canvas.create_text(200, 10, text="score:")



    

        

    def start(self, evt):

        if self.speed != 0:
            return
        
      
        self.canvas.moveto(self.id, self.init_x, self.init_y)
        self.speed = 3  

        angle = math.radians(random.choice(list(range(20, 65, 5))))
        direction = random.choice([1, -1])  
        self.x = math.cos(angle) * self.speed * direction
        self.y = math.sin(angle) * self.speed

            
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

       
        if pos[0] <= 0:
            self.fix(pos[0] - 0, 0)

      
        if pos[1] <= 0:
            self.fix(0, pos[1])

   
        if pos[2] >= self.canvas_width:
            self.fix(pos[2] - self.canvas_width, 0)


        if pos[3] >= self.canvas_height:
            self.fix(0, pos[3] - self.canvas_height)
            self.failed()

  
        paddle_pos = self.canvas.coords(self.paddle.id)
        
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] \
           and paddle_pos[1] <= pos[3] <= paddle_pos[3]:
            self.fix(0, pos[3] - paddle_pos[1])  
            self.canvas.delete(self.id_2)
            self.ans = self.ans + 1
            self.id_2 = self.canvas.create_text(250, 10, text=self.ans)



         

        
    def fix(self, diff_x, diff_y):
        self.canvas.move(self.id, -(diff_x * 2), -(diff_y * 2))

        
        if diff_x != 0:
            self.x = -self.x
            
        if diff_y != 0:
            self.y = -self.y


            


    def failed(self):
        
        self.x = 0
        self.y = 0
        self.speed = 0

            
