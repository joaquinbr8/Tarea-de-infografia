import arcade
from bresenham import get_line
import math

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Figuras con Bresenham"

class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 10

    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        arcade.start_render()
        self.draw_grid()
        self.draw_triangle()
        self.draw_rectangle()
        self.draw_pentagon()

    def draw_grid(self):
        # Líneas verticales
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2, 
                0, 
                v_l + self.pixel_size / 2, 
                SCREEN_HEIGHT, 
                [50, 50, 50]
            )

        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l + self.pixel_size / 2, 
                SCREEN_WIDTH, 
                h_l + self.pixel_size / 2, 
                [50, 50, 50]
            )

    def draw_line_points(self, points, color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_triangle(self):
        p1 = (5, 5)
        p2 = (15, 20)
        p3 = (25, 5)

        points = []
        points += get_line(p1[0], p1[1], p2[0], p2[1])
        points += get_line(p2[0], p2[1], p3[0], p3[1])
        points += get_line(p3[0], p3[1], p1[0], p1[1])

        self.draw_line_points(points, arcade.color.AQUA)

    def draw_rectangle(self):
        p1 = (30, 10)
        p2 = (50, 10)
        p3 = (50, 20)
        p4 = (30, 20)

        points = []
        points += get_line(p1[0], p1[1], p2[0], p2[1])
        points += get_line(p2[0], p2[1], p3[0], p3[1])
        points += get_line(p3[0], p3[1], p4[0], p4[1])
        points += get_line(p4[0], p4[1], p1[0], p1[1])

        self.draw_line_points(points, arcade.color.YELLOW)

    def draw_pentagon(self):
        xc, yc = 50, 50  # Centro del pentágono
        r = 15  # Radio del pentágono
        points = []
        angles = [i * 2 * math.pi / 5 for i in range(5)]
        vertices = [(int(xc + r * math.cos(a)), int(yc + r * math.sin(a))) for a in angles]

        for i in range(5):
            next_i = (i + 1) % 5
            points += get_line(vertices[i][0], vertices[i][1], vertices[next_i][0], vertices[next_i][1])

        self.draw_line_points(points, arcade.color.PINK)

if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()


    #mover el cuadrado y hacer que rote
