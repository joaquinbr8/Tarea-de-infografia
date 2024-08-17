import arcade
import numpy as np


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Zorro 3D con Matrices"

class FoxApp(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.pyramid_position = np.array([0, 0, -150, 0])  
        self.rotation_matrix = np.eye(4)
        self.projection_matrix = self.create_perspective_projection_matrix(60, width / height, 0.1, 1000)
        self.mouse_coords = (0, 0)  
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):
        
        scale_factor = 0.5

        
        self.body_vertices = np.array([
            [0, 5 * scale_factor, 0, 1],    
            [-5 * scale_factor, -5 * scale_factor, 5 * scale_factor, 1],  
            [5 * scale_factor, -5 * scale_factor, 5 * scale_factor, 1],  
            [5 * scale_factor, -5 * scale_factor, -5 * scale_factor, 1],  
            [-5 * scale_factor, -5 * scale_factor, -5 * scale_factor, 1]  
        ])
        self.body_faces = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1), (1, 2, 3, 4)]

    
        ear_scale = 0.3
        self.ear1_vertices = np.array([
            [0, 6 * scale_factor, 0, 1],  
            [-3 * ear_scale, 2 * scale_factor, 3 * ear_scale, 1],  
            [3 * ear_scale, 2 * scale_factor, 3 * ear_scale, 1],   
            [3 * ear_scale, 2 * scale_factor, -3 * ear_scale, 1],  
            [-3 * ear_scale, 2 * scale_factor, -3 * ear_scale, 1]  
        ])
        self.ear2_vertices = np.array([
            [0, 6 * scale_factor, 0, 1],  
            [-3 * ear_scale, 2 * scale_factor, 3 * ear_scale, 1],  
            [3 * ear_scale, 2 * scale_factor, 3 * ear_scale, 1],   
            [3 * ear_scale, 2 * scale_factor, -3 * ear_scale, 1],  
            [-3 * ear_scale, 2 * scale_factor, -3 * ear_scale, 1]  
        ])
        self.ear1_faces = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1)]
        self.ear2_faces = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1)]

    def create_perspective_projection_matrix(self, fov, aspect, near, far):
        """Crear la matriz de proyección en perspectiva."""
        f = 1.0 / np.tan(np.radians(fov) / 2)
        return np.array([
            [f / aspect, 0, 0, 0],
            [0, f, 0, 0],
            [0, 0, (far + near) / (near - far), (2 * far * near) / (near - far)],
            [0, 0, -1, 0]
        ])

    def on_draw(self):
        arcade.start_render()

        
        body_transformed = self.apply_transformations(self.body_vertices, self.pyramid_position)
        ear1_transformed = self.apply_transformations(self.ear1_vertices, self.pyramid_position + np.array([3 * 0.5, 7 * 0.5, 0, 0]))
        ear2_transformed = self.apply_transformations(self.ear2_vertices, self.pyramid_position + np.array([-3 * 0.5, 7 * 0.5, 0, 0]))

    
        for face in self.body_faces:
            points = [self.project_point(body_transformed[i]) for i in face]
            arcade.draw_polygon_outline(points, arcade.color.RED, 2)

        
        for face in self.ear1_faces:
            points = [self.project_point(ear1_transformed[i]) for i in face]
            arcade.draw_polygon_outline(points, arcade.color.ORANGE, 2)

        for face in self.ear2_faces:
            points = [self.project_point(ear2_transformed[i]) for i in face]
            arcade.draw_polygon_outline(points, arcade.color.ORANGE, 2)

    def on_update(self, delta_time):
        
        mouse_x, mouse_y = self.mouse_coords
        center_x, center_y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2

        
        diff_x = (mouse_x - center_x) / center_x
        diff_y = (mouse_y - center_y) / center_y

        
        max_angle = np.pi / 6  

        
        angle_x = max_angle * diff_y  
        angle_y = max_angle * diff_x  

        
        rotation_x = np.array([
            [1, 0, 0, 0],
            [0, np.cos(angle_x), -np.sin(angle_x), 0],
            [0, np.sin(angle_x), np.cos(angle_x), 0],
            [0, 0, 0, 1]
        ])

        rotation_y = np.array([
            [np.cos(angle_y), 0, np.sin(angle_y), 0],
            [0, 1, 0, 0],
            [-np.sin(angle_y), 0, np.cos(angle_y), 0],
            [0, 0, 0, 1]
        ])

        
        self.rotation_matrix = np.dot(rotation_y, rotation_x)

    def apply_transformations(self, vertices, position):
        
        transformed_vertices = []
        for vertex in vertices:
            transformed_vertex = np.dot(self.rotation_matrix, vertex) + position
            transformed_vertices.append(transformed_vertex)
        return transformed_vertices

    def project_point(self, vertex):
        """Proyectar un punto 3D en el espacio 2D utilizando la matriz de proyección en perspectiva."""
        projected_vertex = np.dot(self.projection_matrix, vertex)
        
        if projected_vertex[3] != 0:
            projected_vertex /= projected_vertex[3]
        
        x = (projected_vertex[0] + 1) * 0.5 * SCREEN_WIDTH
        y = (projected_vertex[1] + 1) * 0.5 * SCREEN_HEIGHT
        return x, y

    def on_mouse_motion(self, x, y, dx, dy):
        
        self.mouse_coords = (x, y)


def main():
    app = FoxApp(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    app.setup()
    arcade.run()

if __name__ == "__main__":
    main()

