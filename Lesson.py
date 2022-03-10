import tkinter as tk
from random import randint

WIDTH = 1200
HEIGHT = 800


class Ball:
    def __init__(self):
        self.radius = randint(20, 70)
        self.x = randint(self.radius, WIDTH - self.radius)
        self.y = randint(self.radius, HEIGHT - self.radius)
        self.colors = ["green", "yellow", "pink", "red", "blue", "brown", "orange", "purple", "fuchsia", "goldenrod"]
        self.dx, self.dy = (randint(-5, 5), randint(-5, 5))
        self.ball_id = canvas.create_oval(self.x - self.radius, self.y - self.radius,
                                          self.x + self.radius, self.y + self.radius,
                                          fill=self.colors[randint(0, len(self.colors) - 1)])

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.radius > WIDTH or self.x - self.radius <= 0:
            self.dx = -self.dx
        if self.y + self.radius > HEIGHT or self.y - self.radius <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def canvas_click_handler(event):
    print("canvas_click_handler: x=", event.x, 'y=', event.y)


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)

def main():
    global root, canvas, balls

    root = tk.Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.pack(anchor="center", fill=tk.BOTH, expand=True)
    canvas.bind('<Button-1>', canvas_click_handler)
    balls = [Ball() for i in range(50)]
    tick()
    root.mainloop()

if __name__ == "__main__":
    main()