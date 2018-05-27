import pygame


class Events:

    def __init__(self):
        self.key_states = {

            "up"            : False,
            "down"          : False,
            "left"          : False,
            "right"         : False,
            "up_left"       : False,
            "up_right"      : False,
            "down_left"     : False,
            "down_right"    : False,
        }


    def processEvent(self):

        #pygame.key.set_repeat(0, 500)
        for _event in pygame.event.get():

            if _event.type == pygame.QUIT:
                self.triggerEventAction("quit")

            # Keydown Events
            if _event.type == pygame.KEYDOWN:
                if _event.key == pygame.K_ESCAPE:
                    pass

                # Arrows key
                if _event.key == pygame.K_UP:
                    self.key_states["up"] = True
                if _event.key == pygame.K_DOWN:
                    self.key_states["down"] = True
                if _event.key == pygame.K_LEFT:
                    self.key_states["left"] = True
                if _event.key == pygame.K_RIGHT:
                    self.key_states["right"] = True

            # Key Up Events
            if _event.type == pygame.KEYUP:

                if _event.key == pygame.K_UP:
                    self.key_states["up"] = False
                if _event.key == pygame.K_DOWN:
                    self.key_states["down"] = False
                if _event.key == pygame.K_LEFT:
                    self.key_states["left"] = False
                if _event.key == pygame.K_RIGHT:
                    self.key_states["right"] = False



        # Diagonal arrows
        if pygame.key.get_pressed()[pygame.K_RIGHT] == True and \
            pygame.key.get_pressed()[pygame.K_DOWN] == True:
            self.key_states["down_right"] = True
        else:
            self.key_states["down_right"] = False

        if pygame.key.get_pressed()[pygame.K_LEFT] == True and \
            pygame.key.get_pressed()[pygame.K_DOWN] == True:
            self.key_states["down_left"] = True
        else:
            self.key_states["down_left"] = False

        if pygame.key.get_pressed()[pygame.K_RIGHT] == True and \
            pygame.key.get_pressed()[pygame.K_UP] == True:
            self.key_states["up_right"] = True
        else:
            self.key_states["up_right"] = False

        if pygame.key.get_pressed()[pygame.K_LEFT] == True and \
            pygame.key.get_pressed()[pygame.K_UP] == True:
            self.key_states["up_left"] = True
        else:
            self.key_states["up_left"] = False




    def triggerEventAction(self, _action):

        if _action == 'quit':
            pygame.quit()
            quit(print("Exit successfull"))



    # Getters

    def getKeyStates(self):
        return self.key_states
