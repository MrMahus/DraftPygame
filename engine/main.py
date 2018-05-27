import pygame

pygame.init()
disp = pygame.display.set_mode((640,640))

surfaceTest = pygame.Surface((200,200))

surfaceTest.fill((0,200,0))

xsurf = 0
ysurf = -200

while(True):

    for _event in pygame.event.get():
        pygame.key.set_repeat(0, 500)

        if _event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Keydown Events
        if _event.type == pygame.KEYDOWN:
            if _event.key == pygame.K_UP:
                ysurf += 10


    disp.fill((0,0,0))

    disp.blit(surfaceTest,(xsurf,ysurf))




    pygame.display.flip()