import pygame
import math


class Planet:
    def __init__(self, name, gravity_center, radius, planet_radius, color):
        self.name = name
        self.gravity_center = gravity_center
        self.radius = radius
        self.color = color
        self.planet_radius = planet_radius
        self.planet_center = (self.gravity_center[0] + self.radius, self.gravity_center[1] + 0)

    def print_planet(self):
        print(self.name + ":" + str(self.gravity_center) + str(self.radius) + str(self.color) + str(self.planet_radius))

    def update_gravity_center(self, gravity_center):
        self.gravity_center = gravity_center

    def draw(self, surface):
        time = pygame.time.get_ticks() / ((self.radius + 1) * 10);
        self.planet_center = (int(self.gravity_center[0] + math.cos(time) * self.radius),
                         int(self.gravity_center[1] + math.sin(time) * self.radius))
        # planet_center = (self.gravity_center[0] + self.radius, self.gravity_center[1] + 0)
        pygame.draw.circle(surface, self.color, self.planet_center, self.planet_radius, 0)

