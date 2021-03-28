import pygame
from engine.engine import Node, Edge, Figure

pygame.init()
pygame.font.init()
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("3D")
clock = pygame.time.Clock()
running = True
figure = Figure()

size = 25

n_color = (255, 255, 255)
sq_tl_f = Node((-size, size, size), n_color)
sq_tr_f = Node((size, size, size), n_color)
sq_bl_f = Node((-size, -size, size), n_color)
sq_br_f = Node((size, -size, size), n_color)
te_l_f = Node((-size, 4 * size, size), n_color)
te_r_f = Node((size, 4 * size, size), n_color)
be_l_f = Node((-size, -4 * size, size), n_color)
be_r_f = Node((size, -4 * size, size), n_color)
le_l_f = Node((-4 * size, size, size), n_color)
le_r_f = Node((-4 * size, -size, size), n_color)
re_l_f = Node((4 * size, size, size), n_color)
re_r_f = Node((4 * size, -size, size), n_color)
sq_tl_b = Node((-size, size, -size), n_color)
sq_tr_b = Node((size, size, -size), n_color)
sq_bl_b = Node((-size, -size, -size), n_color)
sq_br_b = Node((size, -size, -size), n_color)
te_l_b = Node((-size, 4 * size, -size), n_color)
te_r_b = Node((size, 4 * size, -size), n_color)
be_l_b = Node((-size, -4 * size, -size), n_color)
be_r_b = Node((size, -4 * size, -size), n_color)
le_l_b = Node((-4 * size, size, -size), n_color)
le_r_b = Node((-4 * size, -size, -size), n_color)
re_l_b = Node((4 * size, size, -size), n_color)
re_r_b = Node((4 * size, -size, -size), n_color)

figure.add_edges(
    (Edge(te_l_f, te_r_f),
     Edge(te_r_f, sq_tr_f),
     Edge(sq_tr_f, re_l_f),
     Edge(re_l_f, re_r_f),
     Edge(re_r_f, sq_br_f),
     Edge(sq_br_f, be_r_f),
     Edge(be_r_f, be_l_f),
     Edge(be_l_f, sq_bl_f),
     Edge(sq_bl_f, le_r_f),
     Edge(le_r_f, le_l_f),
     Edge(le_l_f, sq_tl_f),
     Edge(sq_tl_f, te_l_f),

     Edge(te_l_b, te_r_b),
     Edge(te_r_b, sq_tr_b),
     Edge(sq_tr_b, re_l_b),
     Edge(re_l_b, re_r_b),
     Edge(re_r_b, sq_br_b),
     Edge(sq_br_b, be_r_b),
     Edge(be_r_b, be_l_b),
     Edge(be_l_b, sq_bl_b),
     Edge(sq_bl_b, le_r_b),
     Edge(le_r_b, le_l_b),
     Edge(le_l_b, sq_tl_b),
     Edge(sq_tl_b, te_l_b),

     Edge(te_l_f, te_l_b),
     Edge(te_r_f, te_r_b),
     Edge(sq_tr_f, sq_tr_b),
     Edge(re_l_f, re_l_b),
     Edge(re_r_f, re_r_b),
     Edge(sq_br_f, sq_br_b),
     Edge(be_r_f, be_r_b),
     Edge(be_l_f, be_l_b),
     Edge(sq_bl_f, sq_bl_b),
     Edge(le_l_f, le_l_b),
     Edge(le_r_f, le_r_b),
     Edge(sq_tl_f, sq_tl_b)),
    color=(255, 255, 255)
)

deg = 0


def draw():
    global deg
    display.fill((0, 0, 0))
    figure.draw(display, (250, 250), (deg, deg, deg))  # Make rotation point (250, 250)
    deg += 0.0175


while running:
    clock.tick(200)
    draw()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
