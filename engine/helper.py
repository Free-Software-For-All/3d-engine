import math


def rotate_z_axis(node, theta):
    (node_x, node_y) = node.pos[:2]  # Unpack node
    # dist = math.sqrt(node_x ** 2 + node_y ** 2)  # Distance from point to origin

    new_node_x = node_x * math.cos(theta) - node_y * math.sin(theta)
    new_node_y = node_y * math.cos(theta) + node_x * math.sin(theta)

    return new_node_x, new_node_y, node.pos[2]


def rotate_y_axis(node, theta):
    (node_x, node_z) = node.pos[0], node.pos[2]  # Unpack node
    # dist = math.sqrt(node_x ** 2 + node_z ** 2)  # Distance from point to origin

    new_node_x = node_x * math.cos(theta) - node_z * math.sin(theta)
    new_node_z = node_z * math.cos(theta) + node_x * math.sin(theta)

    return new_node_x, node.pos[1], new_node_z


def rotate_x_axis(node, theta):
    (node_y, node_z) = node.pos[1:]  # Unpack node
    # dist = math.sqrt(node_y ** 2 + node_z ** 2)  # Distance from point to origin

    new_node_y = node_y * math.cos(theta) - node_z * math.sin(theta)
    new_node_z = node_z * math.cos(theta) + node_y * math.sin(theta)

    return node.pos[0], new_node_y, new_node_z


def sign(num):
    if num == 0:  # Avoid division by 0
        return 0
    return num / abs(num)
