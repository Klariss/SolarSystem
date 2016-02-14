import pygame
import planet

pygame.init()

size = (1600, 900)
surface = pygame.display.set_mode(size)
pygame.display.set_caption("My game")

end = False
orange = (255, 167, 43)
gold = (250, 237, 50)
blue = (31, 176, 224)
darkblue = (0, 0, 102)
white = (255, 255, 255)
greyblue = (95, 95, 140)
brown = (201, 91, 8)
yellow = (255, 255, 153)
red = (255, 0, 0)
lightblue = (51, 255, 255)
seablue = (51, 51, 255)
grey = (128, 128, 128)

sun = planet.Planet("sun", [size[0]//2, size[1]//2], 0, 30, gold)
mercury = planet.Planet("mercury", [size[0]//2, size[1]//2], 50, 8, white)
venus = planet.Planet("venus", [size[0]//2, size[1]//2], 100, 10, orange)

earth = planet.Planet("earth", [size[0]//2, size[1]//2], 150, 10, blue)
moon = planet.Planet("moon", [size[0]//2 + 150, size[1]//2 + 150], 20, 4, grey)

mars = planet.Planet("mars", [size[0]//2, size[1]//2], 200, 9, red)
jupiter = planet.Planet("jupiter", [size[0]//2, size[1]//2], 250, 10, brown)
saturn = planet.Planet("saturn", [size[0]//2, size[1]//2], 300, 25, yellow)
uranus = planet.Planet("uranus", [size[0]//2, size[1]//2], 350, 20, lightblue)
neptune = planet.Planet("neptune", [size[0]//2, size[1]//2], 400, 10, seablue)
pluto = planet.Planet("pluto", [size[0]//2, size[1]//2], 450, 6, grey)

sun.print_planet()

planets = [sun, venus, mercury, earth, moon, mars, jupiter, saturn, uranus, neptune, pluto]

texture = pygame.image.load("stars-carousel.jpg").convert()
texture_rect = [0, 0, size[0], size[1]]

while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    surface.fill(darkblue)
    surface.blit(texture, texture_rect)

    planet_center = planets[3].planet_center;
    for plan in planets:
        if plan.name == "moon":
            plan.update_gravity_center(planet_center)

        plan.draw(surface)


    pygame.display.flip()

pygame.quit()