import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((800, 1000))
tinyfont = pygame.font.SysFont('Corbel', 75)
smallfont = pygame.font.SysFont('Corbel', 100)
mediumfont = pygame.font.SysFont('Corbel', 175)
largefont = pygame.font.SysFont('Corbel', 250)


'''size uses'''
### tiny ###
#   large number error
#   divide by zero error

### small ###
#   numbers
#   divide
#   value error message

### medium ###
#   plus
#   negative

### large ###
#   equals
#   subtract
#   multiply


'''Button visuals'''
def set_default_display():
    screen.fill(white)
    #calculator screen
    pygame.draw.rect(screen, black, (150, 85, 500, 100), 1)
    #calculator outline
    pygame.draw.rect(screen, black, (100, 50, 600, 850), 1)

    ### row 1 ###
    #zero
    pygame.draw.rect(screen, black, (150, 750, 100, 100), 1)
    zero = smallfont.render('0', True, black)
    screen.blit(zero, (180, 770))
    #decimal
    pygame.draw.rect(screen, black, (275, 750, 100, 100), 1)
    pygame.draw.circle(screen, black, (325, 800), 12.5)
    #equals
    pygame.draw.rect(screen, black, (400, 750, 225, 100), 1)
    equals = largefont.render('=', True, black)
    screen.blit(equals, (460, 703))

    ### row 2 ###
    #one
    pygame.draw.rect(screen, black, (150, 625, 100, 100), 1)
    one = smallfont.render('1', True, black)
    screen.blit(one, (180, 645))
    #two
    pygame.draw.rect(screen, black, (275, 625, 100, 100), 1)
    two = smallfont.render('2', True, black)
    screen.blit(two, (305, 645))
    #three
    pygame.draw.rect(screen, black, (400, 625, 100, 100), 1)
    three = smallfont.render('3', True, black)
    screen.blit(three, (430, 645))
    #add
    pygame.draw.rect(screen, black, (525, 625, 100, 100), 1)
    plus = mediumfont.render('+', True, black)
    screen.blit(plus, (541, 605))

    ### row 3 ###
    #four
    pygame.draw.rect(screen, black, (150, 500, 100 ,100), 1)
    four = smallfont.render('4', True, black)
    screen.blit(four, (180, 520))
    #five
    pygame.draw.rect(screen, black, (275, 500, 100, 100), 1)
    five = smallfont.render('5', True, black)
    screen.blit(five, (305, 520))
    #six
    pygame.draw.rect(screen, black, (400, 500, 100, 100), 1)
    six = smallfont.render('6', True, black)
    screen.blit(six, (430, 520))
    #subtract
    pygame.draw.rect(screen, black, (525, 500, 100, 100), 1)
    minus = largefont.render('-', True, black)
    screen.blit(minus, (547, 460))

    ### row 4 ###
    #seven
    pygame.draw.rect(screen, black, (150, 375, 100, 100), 1)
    seven = smallfont.render('7', True, black)
    screen.blit(seven, (180, 395))
    #eight
    pygame.draw.rect(screen, black, (275, 375, 100, 100), 1)
    eight = smallfont.render('8', True, black)
    screen.blit(eight, (305, 395))
    #nine
    pygame.draw.rect(screen, black, (400, 375, 100, 100), 1)
    nine = smallfont.render('9', True, black)
    screen.blit(nine, (430, 395))
    #multiply
    pygame.draw.rect(screen, black, (525, 375, 100, 100), 1)
    asterisk = largefont.render('*', True, black)
    screen.blit(asterisk, (543, 385))

    ### row 5 ###
    #clear
    pygame.draw.rect(screen, black, (150, 250, 225, 100), 1)
    clear_all = smallfont.render('CA', True, black)
    screen.blit(clear_all, (215, 270))
    #negative
    pygame.draw.rect(screen, black, (400, 250, 100, 100), 1)
    negate = smallfont.render('+\-', True, black)
    screen.blit(negate, (410, 270))
    #divide
    pygame.draw.rect(screen, black, (525, 250, 100, 100), 1)
    division = smallfont.render('/', True, black)
    screen.blit(division, (565, 268))


'''Button Hitboxes'''
buttons = { '0' : (150, 750, 100, 100),
            '.' : (275, 750, 100, 100),
            'equals' : (400, 750, 225, 100),
            '1' : (150, 625, 100, 100),
            '2' : (275, 625, 100, 100),
            '3' : (400, 625, 100, 100),
            'add' : (525, 625, 100, 100),
            '4' : (150, 500, 100 ,100),
            '5' : (275, 500, 100, 100),
            '6' : (400, 500, 100, 100),
            'subtract' : (525, 500, 100, 100),
            '7' : (150, 375, 100, 100),
            '8' : (275, 375, 100, 100),
            '9' : (400, 375, 100, 100),
            'multiply' : (525, 375, 100, 100),
            'clear' : (150, 250, 225, 100),
            'negative' : (400, 250, 100, 100),
            'divide' : (525, 250, 100, 100)
}


'''Update Calculator Screen'''
def do_button_press(button):
    global pressed_buttons, index, is_decimal
    if button == '.':
        index -= 1
        is_decimal = True
    elif is_number(button):
        set_default_display()
        x = smallfont.render(pressed_buttons[-1], True, black)
        screen.blit(x, (correct_for_decimal(550 - (index * 43)), 100))
    elif button == 'clear':
        set_default_display()
        pressed_buttons = []
    elif button == 'equals':
        set_default_display()
        for i in pressed_buttons:
            if i == 'add':
                add()
            elif i == 'subtract':
                subtract()
            elif i == 'multiply':
                multiply()
            elif i == 'divide':
                divide()
        pressed_buttons = []
    elif button == 'add':
        plus = mediumfont.render('+', True, black)
        screen.blit(plus, (150, 60))
    elif button == 'subtract':
        minus = largefont.render('-', True, black)
        screen.blit(minus, (150, 45))
    elif button == 'multiply':
        asterisk = largefont.render('*', True, black)
        screen.blit(asterisk, (152, 90))
    elif button == 'divide':
        slash = smallfont.render('/', True, black)
        screen.blit(slash, (165, 100))
    elif button == 'negative':
        pressed_buttons[-1] = float(pressed_buttons[-1])
        pressed_buttons[-1] *= -1
        pressed_buttons[-1] = str(pressed_buttons[-1])
        minus = mediumfont.render('-', True, black)
        screen.blit(minus, (correct_for_decimal(500 - (index * 42)), 70))
    

'''math functions'''
def add():
    answer = float(pressed_buttons[0]) + float(pressed_buttons[2])
    answer = smallfont.render(str(answer), True, black)
    screen.blit(answer, (200, 100))

def subtract():
    answer = float(pressed_buttons[0]) - float(pressed_buttons[2])
    answer = smallfont.render(str(answer), True, black)
    screen.blit(answer, (200, 100))

def multiply():
    answer = float(pressed_buttons[0]) * float(pressed_buttons[2])
    answer = smallfont.render(str(answer), True, black)
    screen.blit(answer, (200, 100))

def divide():
    #check divide by 0
    try:
        answer = float(pressed_buttons[0]) / float(pressed_buttons[2])
        answer = round(answer, 8)
        answer = smallfont.render(str(answer), True, black)
        screen.blit(answer, (200, 100))
    except ZeroDivisionError:
        zero_error_message = tinyfont.render("Divide by Zero Error", True, black)
        screen.blit(zero_error_message, (149, 100))

# check if string represents a number
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

'''Initial Code'''
set_default_display()

# stores length of current number to adjust display
index = 0

# adjust display if there is a deciaml
is_decimal = False
def correct_for_decimal(x_value):
    if is_decimal is True:
        return x_value - 13.5
    else:
        return x_value

# store currently pressed buttons
pressed_buttons = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x_pos, y_pos = pos[0], pos[1]

            # check if mouse pos is withing the bounds of a button
            for key, value in buttons.items():
                x_low, x_high = value[0], value[0] + value[2]
                y_low, y_high = value[1], value[1] + value[3]
                # check if mouse clicked on a button
                if x_low <= x_pos <= x_high and y_low <= y_pos <= y_high:
                    # manage pressed buttons list
                    if len(pressed_buttons) == 0:
                        pressed_buttons.append(key)
                        index = 0
                        is_decimal = False

                    elif not is_number(pressed_buttons[-1]) and pressed_buttons[-1] != '.':
                        pressed_buttons.append(key)
                        index = 0
                        is_decimal = False

                    elif is_number(key) or key == '.':
                        x = pressed_buttons[-1]
                        x = x + key
                        pressed_buttons[-1] = x
                        index += 1

                    elif key == 'negative':
                        pass

                    else:
                        pressed_buttons.append(key)
                        index = 0
                        is_decimal = False
                    
                    #number is too large for screen
                    if index >= 10:
                        set_default_display()
                        large_number_error = tinyfont.render("Large Number Error", True, black)
                        screen.blit(large_number_error, (155, 110))
                        break

                    #ignore if button is pressed at wrong time
                    try:
                        do_button_press(key)
                    except ValueError:
                        pressed_buttons.pop(-1)
                        index = 0
                        is_decimal = False

                        error_message = smallfont.render("Error", True, black)
                        screen.blit(error_message, (400, 100))
                    finally:
                        break        

    pygame.display.update()
    pygame.time.delay(30)