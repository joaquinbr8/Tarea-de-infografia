import arcade

# Definición de constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Triángulo con Python"

class TrianguloWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.draw_triangle(20, 20, 30, 40, arcade.color.CYAN)

    def draw_triangle(self, x0, y0, base, height, color):
        x1, y1 = x0 + base, y0
        x2, y2 = x0 + base // 2, y0 + height

        # Lados del triángulo
        self.draw_line(x0, y0, x1, y1, color)
        self.draw_line(x0, y0, x2, y2, color)
        self.draw_line(x1, y1, x2, y2, color)

    def draw_line(self, x0, y0, x1, y1, color):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        while True:
            arcade.draw_point(x0, y0, color, 1)  # Add size argument
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

if __name__ == "__main__":
    window = TrianguloWindow()
    arcade.run()