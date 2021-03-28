import pygame
from .helper import rotate_z_axis, rotate_y_axis, rotate_x_axis


class Figure:
    def __init__(self):
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def add_edges(self, edges, *, color=(255, 255, 255)):
        for edge in edges:
            edge.line_color = color
            self.add_edge(edge)

    def draw(self, surface, offset=(0, 0), orientation=(0, 0, 0)):
        for edge in self.edges:
            edge.draw(surface, offset, orientation)


class Edge:
    def __init__(self, node_1, node_2, line_color=(255, 255, 255)):
        self.node_1 = node_1
        self.node_2 = node_2
        self.line_color = line_color

    def draw(self, surface, offset=(0, 0), orientation=(0, 0, 0)):
        node_1_pos = self.node_1.draw(surface, offset, orientation)
        node_2_pos = self.node_2.draw(surface, offset, orientation)

        pygame.draw.line(surface, self.line_color, node_1_pos, node_2_pos)


class Node:
    def __init__(self, pos, color=(255, 255, 255)):
        self.pos = pos
        self.color = color

    def draw(self, surface, offset=(0, 0), orientation=(0, 0, 0)):
        node_2d_pos = self.get_pos(offset, orientation)
        pygame.draw.circle(surface, self.color, node_2d_pos, 5)
        return node_2d_pos

    def get_pos(self, offset=(0, 0), orientation=(0, 0, 0)):
        (offset_x, offset_y) = offset

        node_copy = Node(self.pos, self.color)

        node_copy.pos = rotate_x_axis(node_copy, orientation[0])
        node_copy.pos = rotate_y_axis(node_copy, orientation[1])
        node_copy.pos = rotate_z_axis(node_copy, orientation[2])

        (node_x, node_y) = node_copy.pos[:2]

        node_2d_pos = (int(node_x + offset_x), int(node_y + offset_y))
        return node_2d_pos


class TextWrapper:
    def __init__(self, font_name, font_size=12, bold=False, italic=False):
        if font_name in pygame.font.get_fonts():
            self.font = pygame.font.SysFont(font_name, font_size, bold, italic)
        else:
            self.font = pygame.font.Font(font_name, font_size)

    def render_text(self, surface, text, pos, color, background_color=None, antialias=True):
        rendered_text = self.font.render(text, antialias, color, background_color)
        surface.blit(rendered_text, pos)
