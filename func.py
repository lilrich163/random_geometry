import tkinter as tk
import random

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

class RandomShapeGenerator:
    def __init__(self, canvas):
        self.canvas = canvas
        self.shape = None
        
    def generate_shape(self):

        shape_type = random.choice(['square', 'circle', 'triangle'])
        
        if shape_type == 'square':
            self.generate_square()
        elif shape_type == 'circle':
            self.generate_circle()
        elif shape_type == 'triangle':
            self.generate_triangle()
    
    def generate_square(self):

        x = random.randint(0, WINDOW_WIDTH-50)
        y = random.randint(0, WINDOW_HEIGHT-50)
        size = random.randint(20, 50)
        

        self.shape = self.canvas.create_rectangle(x, y, x+size, y+size, fill='red')
    
    def generate_circle(self):

        x = random.randint(0, WINDOW_WIDTH-50)
        y = random.randint(0, WINDOW_HEIGHT-50)
        radius = random.randint(10, 25)
        

        self.shape = self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill='green')
    
    def generate_triangle(self):
    
        x = random.randint(0, WINDOW_WIDTH-50)
        y = random.randint(0, WINDOW_HEIGHT-50)
        size = random.randint(20, 50)
        

        points = [x, y+size, x+size, y+size, x+size/2, y]
        

        self.shape = self.canvas.create_polygon(points, fill='blue')
    
    def clear_shape(self):
        if self.shape:
            self.canvas.delete(self.shape)
            self.shape = None

def generate_random_shape():
    generator.generate_shape()

def clear_canvas():
    generator.clear_shape()

root = tk.Tk()
root.title('Random Shape Generator')
root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')

canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

generate_button = tk.Button(root, text='Generate', command=generate_random_shape)
generate_button.pack(side=tk.LEFT)

clear_button = tk.Button(root, text='Clear', command=clear_canvas)
clear_button.pack(side=tk.RIGHT)

generator = RandomShapeGenerator(canvas)

generate_button.pack()

root.mainloop()