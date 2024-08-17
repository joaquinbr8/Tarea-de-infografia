import arcade
import math  

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pentágono con Bresenham"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.radio = 150

    def on_draw(self):
        arcade.start_render()

        
        self.draw_pentagon(self.center_x, self.center_y, self.radio, arcade.color.WHITE)

    def draw_pentagon(self, x, y, radio, color):
        
        vertices = []
        for i in range(5):
            angle = 2 * math.pi * i / 5
            x_vertex = x + radio * math.cos(angle)
            y_vertex = y + radio * math.sin(angle)
            vertices.append((x_vertex, y_vertex))

        
        for i in range(5):
            start_x, start_y = vertices[i]
            end_x, end_y = vertices[(i + 1) % 5]
            self.draw_line_bresenham(int(start_x), int(start_y), int(end_x), int(end_y), color)

    def draw_line_bresenham(self, x1, y1, x2, y2, color):
        """
        Algoritmo de Bresenham para dibujar líneas
        """
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1

        # En lugar del operador ternario ? :, usamos esta estructura
        err = dx - dy

        while True:
            arcade.draw_point(x1, y1, color, 3)
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
