import random

import win32api, win32con, time, pyautogui, cv2, numpy
from PIL import Image, ImageGrab
if __name__ == '__main__':
    def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        time.sleep(0.5)

    def first_shop_space():
        click(530, 700)

    def second_shop_space():
        click(666, 700)

    def third_shop_space():
        click(810, 700)

    def fourth_shop_space():
        click(955, 700)

    def fifth_shop_space():
        click(1100, 700)

    def first_food_space():
        click(1240, 700)

    def second_food_space():
        click(1390, 700)

    def first_team_space():
        click(525, 440)

    def second_team_space():
        click(670, 440)

    def third_team_space():
        click(800, 440)

    def fourth_team_space():
        click(950, 440)

    def fifth_team_space():
        click(1100, 440)

    def roll():
        click(200, 990)

    def freeze():
        click(1050, 990)

    def sell():
        click(1050, 990)

    def end_turn():
        click(1650, 990)


    pet_page = Image.open('pets/pet_page.png')

    scorpion_1 = Image.open('pets/scorpion_1.png')
    scorpion_2 = Image.open('pets/scorpion_2.png')
    scorpion_3 = Image.open('pets/scorpion_3.png')

    money_0 = Image.open('icons/money_0.png')
    money_1 = Image.open('icons/money_1.png')
    money_2 = Image.open('icons/money_2.png')
    coin = Image.open('icons/coin.png')
    name = Image.open('icons/name.png')

    while True:
        state_right = win32api.GetKeyState(0x02)
        state_middle = win32api.GetKeyState(0x04)

        while True:
            b = win32api.GetKeyState(0x02)
            if b != state_right:
                break

        team = [None] * 5

        # start of turn
        while True:
            money = 10
            end_of_turn = True
            while end_of_turn:
                action_table = []
                shop = [None] * 5
                first_shop_pet = pyautogui.screenshot(region=(480, 706, 91, 23))
                first_pet_check = pyautogui.locate(first_shop_pet, pet_page, confidence=0.75)
                if first_pet_check is not None:
                    first_pet_position = pyautogui.center(first_pet_check)
                    if first_pet_position[0] < 180:
                        if first_pet_position[1] < 180:
                            shop[0] = "fish"
                        elif first_pet_position[1] < 365:
                            shop[0] = "dodo"
                        elif first_pet_position[1] < 550:
                            shop[0] = "rhino"
                        elif first_pet_position[1] < 730:
                            shop[0] = "mammoth"
                        elif first_pet_position[1] < 910:
                            shop[0] = "penguin"
                    elif first_pet_position[0] < 325:
                        if first_pet_position[1] < 180:
                            shop[0] = "duck"
                        elif first_pet_position[1] < 365:
                            shop[0] = "shrimp"
                        elif first_pet_position[1] < 550:
                            shop[0] = "cow"
                        elif first_pet_position[1] < 730:
                            shop[0] = "shark"
                        elif first_pet_position[1] < 910:
                            shop[0] = "cat"
                    elif first_pet_position[0] < 470:
                        if first_pet_position[1] < 180:
                            shop[0] = "horse"
                        elif first_pet_position[1] < 365:
                            shop[0] = "dog"
                        elif first_pet_position[1] < 550:
                            shop[0] = "gorilla"
                        elif first_pet_position[1] < 730:
                            shop[0] = "rabbit"
                        elif first_pet_position[1] < 910:
                            shop[0] = "worm"
                    elif first_pet_position[0] < 615:
                        if first_pet_position[1] < 180:
                            shop[0] = "pig"
                        elif first_pet_position[1] < 365:
                            shop[0] = "blowfish"
                        elif first_pet_position[1] < 550:
                            shop[0] = "flamingo"
                        elif first_pet_position[1] < 730:
                            shop[0] = "giraffe"
                        elif first_pet_position[1] < 910:
                            shop[0] = "leopard"
                    elif first_pet_position[0] < 755:
                        if first_pet_position[1] < 180:
                            shop[0] = "otter"
                        elif first_pet_position[1] < 365:
                            shop[0] = "ox"
                        elif first_pet_position[1] < 550:
                            shop[0] = "rooster"
                        elif first_pet_position[1] < 730:
                            shop[0] = "swan"
                        elif first_pet_position[1] < 910:
                            shop[0] = "crocodile"
                    elif first_pet_position[0] < 900:
                        if first_pet_position[1] < 180:
                            shop[0] = "beaver"
                        elif first_pet_position[1] < 365:
                            shop[0] = "sheep"
                        elif first_pet_position[1] < 550:
                            shop[0] = "turtle"
                        elif first_pet_position[1] < 730:
                            shop[0] = "kangaroo"
                    elif first_pet_position[0] < 1040:
                        if first_pet_position[1] < 180:
                            shop[0] = "cricket"
                        elif first_pet_position[1] < 365:
                            shop[0] = "camel"
                        elif first_pet_position[1] < 550:
                            shop[0] = "badger"
                        elif first_pet_position[1] < 730:
                            shop[0] = "squirrel"
                    elif first_pet_position[0] < 1185:
                        if first_pet_position[1] < 180:
                            shop[0] = "mosquito"
                        elif first_pet_position[1] < 365:
                            shop[0] = "bison"
                        elif first_pet_position[1] < 550:
                            shop[0] = "fly"
                        elif first_pet_position[1] < 730:
                            shop[0] = "monkey"
                    elif first_pet_position[0] < 1290:
                        if first_pet_position[1] < 180:
                            shop[0] = "ant"
                        elif first_pet_position[1] < 365:
                            shop[0] = "skunk"
                        elif first_pet_position[1] < 550:
                            shop[0] = "snail"
                        elif first_pet_position[1] < 730:
                            shop[0] = "seal"
                    elif first_pet_position[0] < 1435:
                        if first_pet_position[1] < 180:
                            shop[0] = "hedgehog"
                        elif first_pet_position[1] < 365:
                            shop[0] = "hippo"
                        elif first_pet_position[1] < 550:
                            shop[0] = "whale"
                        elif first_pet_position[1] < 730:
                            shop[0] = "tiger"
                    elif first_pet_position[0] < 1560:
                        if first_pet_position[1] < 180:
                            shop[0] = "peacock"
                        elif first_pet_position[1] < 365:
                            shop[0] = "parrot"
                        elif first_pet_position[1] < 550:
                            shop[0] = "dragon"
                        elif first_pet_position[1] < 730:
                            shop[0] = "deer"
                    elif first_pet_position[0] < 1720:
                        if first_pet_position[1] < 180:
                            shop[0] = "spider"
                        elif first_pet_position[1] < 365:
                            shop[0] = "dolphin"
                        elif first_pet_position[1] < 550:
                            shop[0] = "turkey"
                        elif first_pet_position[1] < 730:
                            shop[0] = "snake"
                    elif first_pet_position[0] < 1865:
                        if first_pet_position[1] < 180:
                            shop[0] = "elephant"
                        elif first_pet_position[1] < 365:
                            shop[0] = "crab"
                        elif first_pet_position[1] < 550:
                            shop[0] = "rat"
                        elif first_pet_position[1] < 730:
                            shop[0] = "boar"
                else:
                    first_scorpion_ss = pyautogui.screenshot(region=(449, 609, 147, 145))
                    if pyautogui.locate(scorpion_1, first_scorpion_ss, confidence=0.8) is not None:
                        shop[0] = "scorpion"
                    elif pyautogui.locate(scorpion_2, first_scorpion_ss, confidence=0.8) is not None:
                        shop[0] = "scorpion"
                    elif pyautogui.locate(scorpion_3, first_scorpion_ss, confidence=0.8) is not None:
                        shop[0] = "scorpion"

                second_shop_pet = pyautogui.screenshot(region=(624, 705, 91, 23))
                second_pet_check = pyautogui.locate(second_shop_pet, pet_page, confidence=0.75)
                if second_pet_check is not None:
                    second_pet_position = pyautogui.center(second_pet_check)

                    if second_pet_position[0] < 180:
                        if second_pet_position[1] < 180:
                            shop[1] = "fish"
                        elif second_pet_position[1] < 365:
                            shop[1] = "dodo"
                        elif second_pet_position[1] < 550:
                            shop[1] = "rhino"
                        elif second_pet_position[1] < 730:
                            shop[1] = "mammoth"
                        elif second_pet_position[1] < 910:
                            shop[1] = "penguin"
                    elif second_pet_position[0] < 325:
                        if second_pet_position[1] < 180:
                            shop[1] = "duck"
                        elif second_pet_position[1] < 365:
                            shop[1] = "shrimp"
                        elif second_pet_position[1] < 550:
                            shop[1] = "cow"
                        elif second_pet_position[1] < 730:
                            shop[1] = "shark"
                        elif second_pet_position[1] < 910:
                            shop[1] = "cat"
                    elif second_pet_position[0] < 470:
                        if second_pet_position[1] < 180:
                            shop[1] = "horse"
                        elif second_pet_position[1] < 365:
                            shop[1] = "dog"
                        elif second_pet_position[1] < 550:
                            shop[1] = "gorilla"
                        elif second_pet_position[1] < 730:
                            shop[1] = "rabbit"
                        elif second_pet_position[1] < 910:
                            shop[1] = "worm"
                    elif second_pet_position[0] < 615:
                        if second_pet_position[1] < 180:
                            shop[1] = "pig"
                        elif second_pet_position[1] < 365:
                            shop[1] = "blowfish"
                        elif second_pet_position[1] < 550:
                            shop[1] = "flamingo"
                        elif second_pet_position[1] < 730:
                            shop[1] = "giraffe"
                        elif second_pet_position[1] < 910:
                            shop[1] = "leopard"
                    elif second_pet_position[0] < 755:
                        if second_pet_position[1] < 180:
                            shop[1] = "otter"
                        elif second_pet_position[1] < 365:
                            shop[1] = "ox"
                        elif second_pet_position[1] < 550:
                            shop[1] = "rooster"
                        elif second_pet_position[1] < 730:
                            shop[1] = "swan"
                        elif second_pet_position[1] < 910:
                            shop[1] = "crocodile"
                    elif second_pet_position[0] < 900:
                        if second_pet_position[1] < 180:
                            shop[1] = "beaver"
                        elif second_pet_position[1] < 365:
                            shop[1] = "sheep"
                        elif second_pet_position[1] < 550:
                            shop[1] = "turtle"
                        elif second_pet_position[1] < 730:
                            shop[1] = "kangaroo"
                    elif second_pet_position[0] < 1040:
                        if second_pet_position[1] < 180:
                            shop[1] = "cricket"
                        elif second_pet_position[1] < 365:
                            shop[1] = "camel"
                        elif second_pet_position[1] < 550:
                            shop[1] = "badger"
                        elif second_pet_position[1] < 730:
                            shop[1] = "squirrel"
                    elif second_pet_position[0] < 1185:
                        if second_pet_position[1] < 180:
                            shop[1] = "mosquito"
                        elif second_pet_position[1] < 365:
                            shop[1] = "bison"
                        elif second_pet_position[1] < 550:
                            shop[1] = "fly"
                        elif second_pet_position[1] < 730:
                            shop[1] = "monkey"
                    elif second_pet_position[0] < 1290:
                        if second_pet_position[1] < 180:
                            shop[1] = "ant"
                        elif second_pet_position[1] < 365:
                            shop[1] = "skunk"
                        elif second_pet_position[1] < 550:
                            shop[1] = "snail"
                        elif second_pet_position[1] < 730:
                            shop[1] = "seal"
                    elif second_pet_position[0] < 1435:
                        if second_pet_position[1] < 180:
                            shop[1] = "hedgehog"
                        elif second_pet_position[1] < 365:
                            shop[1] = "hippo"
                        elif second_pet_position[1] < 550:
                            shop[1] = "whale"
                        elif second_pet_position[1] < 730:
                            shop[1] = "tiger"
                    elif second_pet_position[0] < 1560:
                        if second_pet_position[1] < 180:
                            shop[1] = "peacock"
                        elif second_pet_position[1] < 365:
                            shop[1] = "parrot"
                        elif second_pet_position[1] < 550:
                            shop[1] = "dragon"
                        elif second_pet_position[1] < 730:
                            shop[1] = "deer"
                    elif second_pet_position[0] < 1720:
                        if second_pet_position[1] < 180:
                            shop[1] = "spider"
                        elif second_pet_position[1] < 365:
                            shop[1] = "dolphin"
                        elif second_pet_position[1] < 550:
                            shop[1] = "turkey"
                        elif second_pet_position[1] < 730:
                            shop[1] = "snake"
                    elif second_pet_position[0] < 1865:
                        if second_pet_position[1] < 180:
                            shop[1] = "elephant"
                        elif second_pet_position[1] < 365:
                            shop[1] = "crab"
                        elif second_pet_position[1] < 550:
                            shop[1] = "rat"
                        elif second_pet_position[1] < 730:
                            shop[1] = "boar"
                else:
                    second_scorpion_ss = pyautogui.screenshot(region=(598, 609, 147, 145))
                    if pyautogui.locate(scorpion_1, second_scorpion_ss, confidence=0.8) is not None:
                        shop[1] = "scorpion"
                    elif pyautogui.locate(scorpion_2, second_scorpion_ss, confidence=0.8) is not None:
                        shop[1] = "scorpion"
                    elif pyautogui.locate(scorpion_3, second_scorpion_ss, confidence=0.8) is not None:
                        shop[1] = "scorpion"

                third_shop_pet = pyautogui.screenshot(region=(771, 703, 91, 23))
                third_pet_check = pyautogui.locate(third_shop_pet, pet_page, confidence=0.75)
                if third_pet_check is not None:
                    third_pet_position = pyautogui.center(third_pet_check)

                    if third_pet_position[0] < 180:
                        if third_pet_position[1] < 180:
                            shop[2] = "fish"
                        elif third_pet_position[1] < 365:
                            shop[2] = "dodo"
                        elif third_pet_position[1] < 550:
                            shop[2] = "rhino"
                        elif third_pet_position[1] < 730:
                            shop[2] = "mammoth"
                        elif third_pet_position[1] < 910:
                            shop[2] = "penguin"
                    elif third_pet_position[0] < 325:
                        if third_pet_position[1] < 180:
                            shop[2] = "duck"
                        elif third_pet_position[1] < 365:
                            shop[2] = "shrimp"
                        elif third_pet_position[1] < 550:
                            shop[2] = "cow"
                        elif third_pet_position[1] < 730:
                            shop[2] = "shark"
                        elif third_pet_position[1] < 910:
                            shop[2] = "cat"
                    elif third_pet_position[0] < 470:
                        if third_pet_position[1] < 180:
                            shop[2] = "horse"
                        elif third_pet_position[1] < 365:
                            shop[2] = "dog"
                        elif third_pet_position[1] < 550:
                            shop[2] = "gorilla"
                        elif third_pet_position[1] < 730:
                            shop[2] = "rabbit"
                        elif third_pet_position[1] < 910:
                            shop[2] = "worm"
                    elif third_pet_position[0] < 615:
                        if third_pet_position[1] < 180:
                            shop[2] = "pig"
                        elif third_pet_position[1] < 365:
                            shop[2] = "blowfish"
                        elif third_pet_position[1] < 550:
                            shop[2] = "flamingo"
                        elif third_pet_position[1] < 730:
                            shop[2] = "giraffe"
                        elif third_pet_position[1] < 910:
                            shop[2] = "leopard"
                    elif third_pet_position[0] < 755:
                        if third_pet_position[1] < 180:
                            shop[2] = "otter"
                        elif third_pet_position[1] < 365:
                            shop[2] = "ox"
                        elif third_pet_position[1] < 550:
                            shop[2] = "rooster"
                        elif third_pet_position[1] < 730:
                            shop[2] = "swan"
                        elif third_pet_position[1] < 910:
                            shop[2] = "crocodile"
                    elif third_pet_position[0] < 900:
                        if third_pet_position[1] < 180:
                            shop[2] = "beaver"
                        elif third_pet_position[1] < 365:
                            shop[2] = "sheep"
                        elif third_pet_position[1] < 550:
                            shop[2] = "turtle"
                        elif third_pet_position[1] < 730:
                            shop[2] = "kangaroo"
                    elif third_pet_position[0] < 1040:
                        if third_pet_position[1] < 180:
                            shop[2] = "cricket"
                        elif third_pet_position[1] < 365:
                            shop[2] = "camel"
                        elif third_pet_position[1] < 550:
                            shop[2] = "badger"
                        elif third_pet_position[1] < 730:
                            shop[2] = "squirrel"
                    elif third_pet_position[0] < 1185:
                        if third_pet_position[1] < 180:
                            shop[2] = "mosquito"
                        elif third_pet_position[1] < 365:
                            shop[2] = "bison"
                        elif third_pet_position[1] < 550:
                            shop[2] = "fly"
                        elif third_pet_position[1] < 730:
                            shop[2] = "monkey"
                    elif third_pet_position[0] < 1290:
                        if third_pet_position[1] < 180:
                            shop[2] = "ant"
                        elif third_pet_position[1] < 365:
                            shop[2] = "skunk"
                        elif third_pet_position[1] < 550:
                            shop[2] = "snail"
                        elif third_pet_position[1] < 730:
                            shop[2] = "seal"
                    elif third_pet_position[0] < 1435:
                        if third_pet_position[1] < 180:
                            shop[2] = "hedgehog"
                        elif third_pet_position[1] < 365:
                            shop[2] = "hippo"
                        elif third_pet_position[1] < 550:
                            shop[2] = "whale"
                        elif third_pet_position[1] < 730:
                            shop[2] = "tiger"
                    elif third_pet_position[0] < 1560:
                        if third_pet_position[1] < 180:
                            shop[2] = "peacock"
                        elif third_pet_position[1] < 365:
                            shop[2] = "parrot"
                        elif third_pet_position[1] < 550:
                            shop[2] = "dragon"
                        elif third_pet_position[1] < 730:
                            shop[2] = "deer"
                    elif third_pet_position[0] < 1720:
                        if third_pet_position[1] < 180:
                            shop[2] = "spider"
                        elif third_pet_position[1] < 365:
                            shop[2] = "dolphin"
                        elif third_pet_position[1] < 550:
                            shop[2] = "turkey"
                        elif third_pet_position[1] < 730:
                            shop[2] = "snake"
                    elif third_pet_position[0] < 1865:
                        if third_pet_position[1] < 180:
                            shop[2] = "elephant"
                        elif third_pet_position[1] < 365:
                            shop[2] = "crab"
                        elif third_pet_position[1] < 550:
                            shop[2] = "rat"
                        elif third_pet_position[1] < 730:
                            shop[2] = "boar"
                else:
                    third_scorpion_ss = pyautogui.screenshot(region=(740, 609, 147, 145))
                    if pyautogui.locate(scorpion_1, third_scorpion_ss, confidence=0.8) is not None:
                        shop[2] = "scorpion"
                    elif pyautogui.locate(scorpion_2, third_scorpion_ss, confidence=0.8) is not None:
                        shop[2] = "scorpion"
                    elif pyautogui.locate(scorpion_3, third_scorpion_ss, confidence=0.8) is not None:
                        shop[2] = "scorpion"

                fourth_shop_pet = pyautogui.screenshot(region=(911, 706, 101, 31))
                fourth_pet_check = pyautogui.locate(fourth_shop_pet, pet_page, confidence=0.75)
                if fourth_pet_check is not None:
                    fourth_pet_position = pyautogui.center(fourth_pet_check)
                    if fourth_pet_position[0] < 180:
                        if fourth_pet_position[1] < 180:
                            shop[3] = "fish"
                        elif fourth_pet_position[1] < 365:
                            shop[3] = "dodo"
                        elif fourth_pet_position[1] < 550:
                            shop[3] = "rhino"
                        elif fourth_pet_position[1] < 730:
                            shop[3] = "mammoth"
                        elif fourth_pet_position[1] < 910:
                            shop[3] = "penguin"
                    elif fourth_pet_position[0] < 325:
                        if fourth_pet_position[1] < 180:
                            shop[3] = "duck"
                        elif fourth_pet_position[1] < 365:
                            shop[3] = "shrimp"
                        elif fourth_pet_position[1] < 550:
                            shop[3] = "cow"
                        elif fourth_pet_position[1] < 730:
                            shop[3] = "shark"
                        elif fourth_pet_position[1] < 910:
                            shop[3] = "cat"
                    elif fourth_pet_position[0] < 470:
                        if fourth_pet_position[1] < 180:
                            shop[3] = "horse"
                        elif fourth_pet_position[1] < 365:
                            shop[3] = "dog"
                        elif fourth_pet_position[1] < 550:
                            shop[3] = "gorilla"
                        elif fourth_pet_position[1] < 730:
                            shop[3] = "rabbit"
                        elif fourth_pet_position[1] < 910:
                            shop[3] = "worm"
                    elif fourth_pet_position[0] < 615:
                        if fourth_pet_position[1] < 180:
                            shop[3] = "pig"
                        elif fourth_pet_position[1] < 365:
                            shop[3] = "blowfish"
                        elif fourth_pet_position[1] < 550:
                            shop[3] = "flamingo"
                        elif fourth_pet_position[1] < 730:
                            shop[3] = "giraffe"
                        elif fourth_pet_position[1] < 910:
                            shop[3] = "leopard"
                    elif fourth_pet_position[0] < 755:
                        if fourth_pet_position[1] < 180:
                            shop[3] = "otter"
                        elif fourth_pet_position[1] < 365:
                            shop[3] = "ox"
                        elif fourth_pet_position[1] < 550:
                            shop[3] = "rooster"
                        elif fourth_pet_position[1] < 730:
                            shop[3] = "swan"
                        elif fourth_pet_position[1] < 910:
                            shop[3] = "crocodile"
                    elif fourth_pet_position[0] < 900:
                        if fourth_pet_position[1] < 180:
                            shop[3] = "beaver"
                        elif fourth_pet_position[1] < 365:
                            shop[3] = "sheep"
                        elif fourth_pet_position[1] < 550:
                            shop[3] = "turtle"
                        elif fourth_pet_position[1] < 730:
                            shop[3] = "kangaroo"
                    elif fourth_pet_position[0] < 1040:
                        if fourth_pet_position[1] < 180:
                            shop[3] = "cricket"
                        elif fourth_pet_position[1] < 365:
                            shop[3] = "camel"
                        elif fourth_pet_position[1] < 550:
                            shop[3] = "badger"
                        elif fourth_pet_position[1] < 730:
                            shop[3] = "squirrel"
                    elif fourth_pet_position[0] < 1185:
                        if fourth_pet_position[1] < 180:
                            shop[3] = "mosquito"
                        elif fourth_pet_position[1] < 365:
                            shop[3] = "bison"
                        elif fourth_pet_position[1] < 550:
                            shop[3] = "fly"
                        elif fourth_pet_position[1] < 730:
                            shop[3] = "monkey"
                    elif fourth_pet_position[0] < 1290:
                        if fourth_pet_position[1] < 180:
                            shop[3] = "ant"
                        elif fourth_pet_position[1] < 365:
                            shop[3] = "skunk"
                        elif fourth_pet_position[1] < 550:
                            shop[3] = "snail"
                        elif fourth_pet_position[1] < 730:
                            shop[3] = "seal"
                    elif fourth_pet_position[0] < 1435:
                        if fourth_pet_position[1] < 180:
                            shop[3] = "hedgehog"
                        elif fourth_pet_position[1] < 365:
                            shop[3] = "hippo"
                        elif fourth_pet_position[1] < 550:
                            shop[3] = "whale"
                        elif fourth_pet_position[1] < 730:
                            shop[3] = "tiger"
                    elif fourth_pet_position[0] < 1560:
                        if fourth_pet_position[1] < 180:
                            shop[3] = "peacock"
                        elif fourth_pet_position[1] < 365:
                            shop[3] = "parrot"
                        elif fourth_pet_position[1] < 550:
                            shop[3] = "dragon"
                        elif fourth_pet_position[1] < 730:
                            shop[3] = "deer"
                    elif fourth_pet_position[0] < 1720:
                        if fourth_pet_position[1] < 180:
                            shop[3] = "spider"
                        elif fourth_pet_position[1] < 365:
                            shop[3] = "dolphin"
                        elif fourth_pet_position[1] < 550:
                            shop[3] = "turkey"
                        elif fourth_pet_position[1] < 730:
                            shop[3] = "snake"
                    elif fourth_pet_position[0] < 1865:
                        if fourth_pet_position[1] < 180:
                            shop[3] = "elephant"
                        elif fourth_pet_position[1] < 365:
                            shop[3] = "crab"
                        elif fourth_pet_position[1] < 550:
                            shop[3] = "rat"
                        elif fourth_pet_position[1] < 730:
                            shop[3] = "boar"
                else:
                    fourth_scorpion_ss = pyautogui.screenshot(region=(884, 609, 147, 145))
                    if pyautogui.locate(scorpion_1, fourth_scorpion_ss, confidence=0.8) is not None:
                        shop[3] = "scorpion"
                    elif pyautogui.locate(scorpion_2, fourth_scorpion_ss, confidence=0.8) is not None:
                        shop[3] = "scorpion"
                    elif pyautogui.locate(scorpion_3, fourth_scorpion_ss, confidence=0.8) is not None:
                        shop[3] = "scorpion"

                fifth_shop_pet = pyautogui.screenshot(region=(1052, 707, 101, 31))
                fifth_pet_check = pyautogui.locate(fifth_shop_pet, pet_page, confidence=0.75)
                if fifth_pet_check is not None:
                    fifth_pet_position = pyautogui.center(fifth_pet_check)
                    if fifth_pet_position[0] < 180:
                        if fifth_pet_position[1] < 180:
                            shop[4] = "fish"
                        elif fifth_pet_position[1] < 365:
                            shop[4] = "dodo"
                        elif fifth_pet_position[1] < 550:
                            shop[4] = "rhino"
                        elif fifth_pet_position[1] < 730:
                            shop[4] = "mammoth"
                        elif fifth_pet_position[1] < 910:
                            shop[4] = "penguin"
                    elif fifth_pet_position[0] < 325:
                        if fifth_pet_position[1] < 180:
                            shop[4] = "duck"
                        elif fifth_pet_position[1] < 365:
                            shop[4] = "shrimp"
                        elif fifth_pet_position[1] < 550:
                            shop[4] = "cow"
                        elif fifth_pet_position[1] < 730:
                            shop[4] = "shark"
                        elif fifth_pet_position[1] < 910:
                            shop[4] = "cat"
                    elif fifth_pet_position[0] < 470:
                        if fifth_pet_position[1] < 180:
                            shop[4] = "horse"
                        elif fifth_pet_position[1] < 365:
                            shop[4] = "dog"
                        elif fifth_pet_position[1] < 550:
                            shop[4] = "gorilla"
                        elif fifth_pet_position[1] < 730:
                            shop[4] = "rabbit"
                        elif fifth_pet_position[1] < 910:
                            shop[4] = "worm"
                    elif fifth_pet_position[0] < 615:
                        if fifth_pet_position[1] < 180:
                            shop[4] = "pig"
                        elif fifth_pet_position[1] < 365:
                            shop[4] = "blowfish"
                        elif fifth_pet_position[1] < 550:
                            shop[4] = "flamingo"
                        elif fifth_pet_position[1] < 730:
                            shop[4] = "giraffe"
                        elif fifth_pet_position[1] < 910:
                            shop[4] = "leopard"
                    elif fifth_pet_position[0] < 755:
                        if fifth_pet_position[1] < 180:
                            shop[4] = "otter"
                        elif fifth_pet_position[1] < 365:
                            shop[4] = "ox"
                        elif fifth_pet_position[1] < 550:
                            shop[4] = "rooster"
                        elif fifth_pet_position[1] < 730:
                            shop[4] = "swan"
                        elif fifth_pet_position[1] < 910:
                            shop[4] = "crocodile"
                    elif fifth_pet_position[0] < 900:
                        if fifth_pet_position[1] < 180:
                            shop[4] = "beaver"
                        elif fifth_pet_position[1] < 365:
                            shop[4] = "sheep"
                        elif fifth_pet_position[1] < 550:
                            shop[4] = "turtle"
                        elif fifth_pet_position[1] < 730:
                            shop[4] = "kangaroo"
                    elif fifth_pet_position[0] < 1040:
                        if fifth_pet_position[1] < 180:
                            shop[4] = "cricket"
                        elif fifth_pet_position[1] < 365:
                            shop[4] = "camel"
                        elif fifth_pet_position[1] < 550:
                            shop[4] = "badger"
                        elif fifth_pet_position[1] < 730:
                            shop[4] = "squirrel"
                    elif fifth_pet_position[0] < 1185:
                        if fifth_pet_position[1] < 180:
                            shop[4] = "mosquito"
                        elif fifth_pet_position[1] < 365:
                            shop[4] = "bison"
                        elif fifth_pet_position[1] < 550:
                            shop[4] = "fly"
                        elif fifth_pet_position[1] < 730:
                            shop[4] = "monkey"
                    elif fifth_pet_position[0] < 1290:
                        if fifth_pet_position[1] < 180:
                            shop[4] = "ant"
                        elif fifth_pet_position[1] < 365:
                            shop[4] = "skunk"
                        elif fifth_pet_position[1] < 550:
                            shop[4] = "snail"
                        elif fifth_pet_position[1] < 730:
                            shop[4] = "seal"
                    elif fifth_pet_position[0] < 1435:
                        if fifth_pet_position[1] < 180:
                            shop[4] = "hedgehog"
                        elif fifth_pet_position[1] < 365:
                            shop[4] = "hippo"
                        elif fifth_pet_position[1] < 550:
                            shop[4] = "whale"
                        elif fifth_pet_position[1] < 730:
                            shop[4] = "tiger"
                    elif fifth_pet_position[0] < 1560:
                        if fifth_pet_position[1] < 180:
                            shop[4] = "peacock"
                        elif fifth_pet_position[1] < 365:
                            shop[4] = "parrot"
                        elif fifth_pet_position[1] < 550:
                            shop[4] = "dragon"
                        elif fifth_pet_position[1] < 730:
                            shop[4] = "deer"
                    elif fifth_pet_position[0] < 1720:
                        if fifth_pet_position[1] < 180:
                            shop[4] = "spider"
                        elif fifth_pet_position[1] < 365:
                            shop[4] = "dolphin"
                        elif fifth_pet_position[1] < 550:
                            shop[4] = "turkey"
                        elif fifth_pet_position[1] < 730:
                            shop[4] = "snake"
                    elif fifth_pet_position[0] < 1865:
                        if fifth_pet_position[1] < 180:
                            shop[4] = "elephant"
                        elif fifth_pet_position[1] < 365:
                            shop[4] = "crab"
                        elif fifth_pet_position[1] < 550:
                            shop[4] = "rat"
                        elif fifth_pet_position[1] < 730:
                            shop[4] = "boar"
                else:
                    fifth_scorpion_ss = pyautogui.screenshot(region=(1030, 609, 147, 145))
                    if pyautogui.locate(scorpion_1, fifth_scorpion_ss, confidence=0.8) is not None:
                        shop[4] = "scorpion"
                    elif pyautogui.locate(scorpion_2, fifth_scorpion_ss, confidence=0.8) is not None:
                        shop[4] = "scorpion"
                    elif pyautogui.locate(scorpion_3, fifth_scorpion_ss, confidence=0.8) is not None:
                        shop[4] = "scorpion"
                if money >= 3:
                    if team[0] is None:
                        if shop[0] is not None:
                            action_table.append(("buy", "first_shop", "first_team"))
                        if shop[1] is not None:
                            action_table.append(("buy", "second_shop", "first_team"))
                        if shop[2] is not None:
                            action_table.append(("buy", "third_shop", "first_team"))
                        if shop[3] is not None:
                            action_table.append(("buy", "fourth_shop", "first_team"))
                        if shop[4] is not None:
                            action_table.append(("buy", "fifth_shop", "first_team"))
                    else:
                        if shop[0] == team[0][0] and team[0][1] < 6:
                            action_table.append(("buy", "first_shop", "first_team"))
                        if shop[1] == team[0][0] and team[0][1] < 6:
                            action_table.append(("buy", "second_shop", "first_team"))
                        if shop[2] == team[0][0] and team[0][1] < 6:
                            action_table.append(("buy", "third_shop", "first_team"))
                        if shop[3] == team[0][0] and team[0][1] < 6:
                            action_table.append(("buy", "fourth_shop", "first_team"))
                        if shop[4] == team[0][0] and team[0][1] < 6:
                            action_table.append(("buy", "fifth_shop", "first_team"))


                    if team[1] is None:
                        if shop[0] is not None:
                            action_table.append(("buy", "first_shop", "second_team"))
                        if shop[1] is not None:
                            action_table.append(("buy", "second_shop", "second_team"))
                        if shop[2] is not None:
                            action_table.append(("buy", "third_shop", "second_team"))
                        if shop[3] is not None:
                            action_table.append(("buy", "fourth_shop", "second_team"))
                        if shop[4] is not None:
                            action_table.append(("buy", "fifth_shop", "second_team"))
                    else:
                        if shop[0] == team[1][0] and team[1][1] < 6:
                            action_table.append(("buy", "first_shop", "second_team"))
                        if shop[1] == team[1][0] and team[1][1] < 6:
                            action_table.append(("buy", "second_shop", "second_team"))
                        if shop[2] == team[1][0] and team[1][1] < 6:
                            action_table.append(("buy", "third_shop", "second_team"))
                        if shop[3] == team[1][0] and team[1][1] < 6:
                            action_table.append(("buy", "fourth_shop", "second_team"))
                        if shop[4] == team[1][0] and team[1][1] < 6:
                            action_table.append(("buy", "fifth_shop", "second_team"))

                    if team[2] is None:
                        if shop[0] is not None:
                            action_table.append(("buy", "first_shop", "third_team"))
                        if shop[1] is not None:
                            action_table.append(("buy", "second_shop", "third_team"))
                        if shop[2] is not None:
                            action_table.append(("buy", "third_shop", "third_team"))
                        if shop[3] is not None:
                            action_table.append(("buy", "fourth_shop", "third_team"))
                        if shop[4] is not None:
                            action_table.append(("buy", "fifth_shop", "third_team"))
                    else:
                        if shop[0] == team[2][0] and team[2][1] < 6:
                            action_table.append(("buy", "first_shop", "third_team"))
                        if shop[1] == team[2][0] and team[2][1] < 6:
                            action_table.append(("buy", "second_shop", "third_team"))
                        if shop[2] == team[2][0] and team[2][1] < 6:
                            action_table.append(("buy", "third_shop", "third_team"))
                        if shop[3] == team[2][0] and team[2][1] < 6:
                            action_table.append(("buy", "fourth_shop", "third_team"))
                        if shop[4] == team[2][0] and team[2][1] < 6:
                            action_table.append(("buy", "fifth_shop", "third_team"))

                    if team[3] is None:
                        if shop[0] is not None:
                            action_table.append(("buy", "first_shop", "fourth_team"))
                        if shop[1] is not None:
                            action_table.append(("buy", "second_shop", "fourth_team"))
                        if shop[2] is not None:
                            action_table.append(("buy", "third_shop", "fourth_team"))
                        if shop[3] is not None:
                            action_table.append(("buy", "fourth_shop", "fourth_team"))
                        if shop[4] is not None:
                            action_table.append(("buy", "fifth_shop", "fourth_team"))
                    else:
                        if shop[0] == team[3][0] and team[3][1] < 6:
                            action_table.append(("buy", "first_shop", "fourth_team"))
                        if shop[1] == team[3][0] and team[3][1] < 6:
                            action_table.append(("buy", "second_shop", "fourth_team"))
                        if shop[2] == team[3][0] and team[3][1] < 6:
                            action_table.append(("buy", "third_shop", "fourth_team"))
                        if shop[3] == team[3][0] and team[3][1] < 6:
                            action_table.append(("buy", "fourth_shop", "fourth_team"))
                        if shop[4] == team[3][0] and team[3][1] < 6:
                            action_table.append(("buy", "fifth_shop", "fourth_team"))

                    if team[4] is None:
                        if shop[0] is not None:
                            action_table.append(("buy", "first_shop", "fifth_team"))
                        if shop[1] is not None:
                            action_table.append(("buy", "second_shop", "fifth_team"))
                        if shop[2] is not None:
                            action_table.append(("buy", "third_shop", "fifth_team"))
                        if shop[3] is not None:
                            action_table.append(("buy", "fourth_shop", "fifth_team"))
                        if shop[4] is not None:
                            action_table.append(("buy", "fifth_shop", "fifth_team"))
                    else:
                        if shop[0] == team[4][0] and team[4][1] < 6:
                            action_table.append(("buy", "first_shop", "fifth_team"))
                        if shop[1] == team[4][0] and team[4][1] < 6:
                            action_table.append(("buy", "second_shop", "fifth_team"))
                        if shop[2] == team[4][0] and team[4][1] < 6:
                            action_table.append(("buy", "third_shop", "fifth_team"))
                        if shop[3] == team[4][0] and team[4][1] < 6:
                            action_table.append(("buy", "fourth_shop", "fifth_team"))
                        if shop[4] == team[4][0] and team[4][1] < 6:
                            action_table.append(("buy", "fifth_shop", "fifth_team"))

                if (team[0] is not None) and (team[1] is not None) and (team[2] is not None) and (team[3] is not None) and (team[4] is not None):
                    action_table.append(("sell"))

                if money > 0:
                    action_table.append(("roll"))

                if money == 0:
                    action_table.append(("end_turn"))
                if (team[0] is not None) and (team[1] is not None) and (team[2] is not None) and (team[3] is not None) and (team[4] is not None):
                    if team[0][0] == team[1][0]:
                        action_table.append(("merge", "first_team", "second_team"))
                    if team[0][0] == team[2][0]:
                        action_table.append(("merge", "first_team", "third_team"))
                    if team[0][0] == team[3][0]:
                        action_table.append(("merge", "first_team", "fourth_team"))
                    if team[0][0] == team[4][0]:
                        action_table.append(("merge", "first_team", "fifth_team"))

                    if team[1][0] == team[2][0]:
                        action_table.append(("merge", "second_team", "third_team"))
                    if team[1][0] == team[3][0]:
                        action_table.append(("merge", "second_team", "fourth_team"))
                    if team[1][0] == team[4][0]:
                        action_table.append(("merge", "second_team", "fifth_team"))

                    if team[2][0] == team[3][0]:
                        action_table.append(("merge", "third_team", "fourth_team"))
                    if team[2][0] == team[4][0]:
                        action_table.append(("merge", "third_team", "fifth_team"))

                    if team[3][0] == team[4][0]:
                        action_table.append(("merge", "fourth_team", "fifth_team"))

                print(money)
                print(team)
                print(shop)
                print(action_table)

                action = random.choice(action_table)

                print(action)

                if action[0] == "buy":
                    money -= 3
                    if action[1] == "first_shop":
                        first_shop_space()
                    elif action[1] == "second_shop":
                        second_shop_space()
                    elif action[1] == "third_shop":
                        third_shop_space()
                    elif action[1] == "fourth_shop":
                        fourth_shop_space()
                    elif action[1] == "fifth_shop":
                        fifth_shop_space()

                    if action[2] == "first_team":
                        first_team_space()
                        if action[1] == "first_shop":
                            if team[0] is None:
                                team[0] = (shop[0], 1)
                            else:
                                team[0] = (shop[0], team[0][1]+1)
                        elif action[1] == "second_shop":
                            if team[0] is None:
                                team[0] = (shop[1], 1)
                            else:
                                team[0] = (shop[1], team[0][1]+1)
                        elif action[1] == "third_shop":
                            if team[0] is None:
                                team[0] = (shop[2], 1)
                            else:
                                team[0] = (shop[2], team[0][1]+1)
                        elif action[1] == "fourth_shop":
                            if team[0] is None:
                                team[0] = (shop[3], 1)
                            else:
                                team[0] = (shop[3], team[0][1]+1)
                        elif action[1] == "fifth_shop":
                            if team[0] is None:
                                team[0] = (shop[4], 1)
                            else:
                                team[0] = (shop[4], team[0][1]+1)
                    elif action[2] == "second_team":
                        second_team_space()
                        if action[1] == "first_shop":
                            if team[1] is None:
                                team[1] = (shop[0], 1)
                            else:
                                team[1] = (shop[0], team[1][1]+1)
                        elif action[1] == "second_shop":
                            if team[1] is None:
                                team[1] = (shop[1], 1)
                            else:
                                team[1] = (shop[1], team[1][1]+1)
                        elif action[1] == "third_shop":
                            if team[1] is None:
                                team[1] = (shop[2], 1)
                            else:
                                team[1] = (shop[2], team[1][1]+1)
                        elif action[1] == "fourth_shop":
                            if team[1] is None:
                                team[1] = (shop[3], 1)
                            else:
                                team[1] = (shop[3], team[1][1]+1)
                        elif action[1] == "fifth_shop":
                            if team[1] is None:
                                team[1] = (shop[4], 1)
                            else:
                                team[1] = (shop[4], team[1][1]+1)
                    elif action[2] == "third_team":
                        third_team_space()
                        if action[1] == "first_shop":
                            if team[2] is None:
                                team[2] = (shop[0], 1)
                            else:
                                team[2] = (shop[0], team[2][1]+1)
                        elif action[1] == "second_shop":
                            if team[2] is None:
                                team[2] = (shop[1], 1)
                            else:
                                team[2] = (shop[1], team[2][1]+1)
                        elif action[1] == "third_shop":
                            if team[2] is None:
                                team[2] = (shop[2], 1)
                            else:
                                team[2] = (shop[2], team[2][1]+1)
                        elif action[1] == "fourth_shop":
                            if team[2] is None:
                                team[2] = (shop[3], 1)
                            else:
                                team[2] = (shop[3], team[2][1]+1)
                        elif action[1] == "fifth_shop":
                            if team[2] is None:
                                team[2] = (shop[4], 1)
                            else:
                                team[2] = (shop[4], team[2][1]+1)
                    elif action[2] == "fourth_team":
                        fourth_team_space()
                        if action[1] == "first_shop":
                            if team[3] is None:
                                team[3] = (shop[0], 1)
                            else:
                                team[3] = (shop[0], team[3][1]+1)
                        elif action[1] == "second_shop":
                            if team[3] is None:
                                team[3] = (shop[1], 1)
                            else:
                                team[3] = (shop[1], team[3][1]+1)
                        elif action[1] == "third_shop":
                            if team[3] is None:
                                team[3] = (shop[2], 1)
                            else:
                                team[3] = (shop[2], team[3][1]+1)
                        elif action[1] == "fourth_shop":
                            if team[3] is None:
                                team[3] = (shop[3], 1)
                            else:
                                team[3] = (shop[3], team[3][1]+1)
                        elif action[1] == "fifth_shop":
                            if team[3] is None:
                                team[3] = (shop[4], 1)
                            else:
                                team[3] = (shop[4], team[3][1]+1)
                    elif action[2] == "fifth_team":
                        fifth_team_space()
                        if action[1] == "first_shop":
                            if team[4] is None:
                                team[4] = (shop[0], 1)
                            else:
                                team[4] = (shop[0], team[4][1]+1)
                        elif action[1] == "second_shop":
                            if team[4] is None:
                                team[4] = (shop[1], 1)
                            else:
                                team[4] = (shop[1], team[4][1]+1)
                        elif action[1] == "third_shop":
                            if team[4] is None:
                                team[4] = (shop[2], 1)
                            else:
                                team[4] = (shop[2], team[4][1]+1)
                        elif action[1] == "fourth_shop":
                            if team[4] is None:
                                team[4] = (shop[3], 1)
                            else:
                                team[4] = (shop[3], team[4][1]+1)
                        elif action[1] == "fifth_shop":
                            if team[4] is None:
                                team[4] = (shop[4], 1)
                            else:
                                team[4] = (shop[4], team[4][1]+1)

                if action == "sell":
                    sellable = []
                    if team[0] is not None:
                        sellable.append("first_team")
                    if team[1] is not None:
                        sellable.append("second_team")
                    if team[2] is not None:
                        sellable.append("third_team")
                    if team[3] is not None:
                        sellable.append("fourth_team")
                    if team[4] is not None:
                        sellable.append("fifth_team")
                    sell_target = random.choice(sellable)
                    if sell_target == "first_team":
                        first_team_space()
                        if team[0][1] < 3:
                            money += 1
                        elif team[0][1] < 6:
                            money += 2
                        else:
                            money += 3
                        if team[0][0] == "pig":
                            if team[0][1] < 3:
                                money += 1
                            elif team[0][1] < 6:
                                money += 2
                            else:
                                money += 3
                        team[0] = None
                    elif sell_target == "second_team":
                        second_team_space()
                        if team[1][1] < 3:
                            money += 1
                        elif team[1][1] < 6:
                            money += 2
                        else:
                            money += 3
                        if team[1][0] == "pig":
                            if team[1][1] < 3:
                                money += 1
                            elif team[1][1] < 6:
                                money += 2
                            else:
                                money += 3
                        team[1] = None
                    elif sell_target == "third_team":
                        third_team_space()
                        if team[2][1] < 3:
                            money += 1
                        elif team[2][1] < 6:
                            money += 2
                        else:
                            money += 3
                        if team[2][0] == "pig":
                            if team[2][1] < 3:
                                money += 1
                            elif team[2][1] < 6:
                                money += 2
                            else:
                                money += 3
                        team[2] = None
                    elif sell_target == "fourth_team":
                        fourth_team_space()
                        if team[3][1] < 3:
                            money += 1
                        elif team[3][1] < 6:
                            money += 2
                        else:
                            money += 3
                        if team[3][0] == "pig":
                            if team[3][1] < 3:
                                money += 1
                            elif team[3][1] < 6:
                                money += 2
                            else:
                                money += 3
                        team[3] = None
                    elif sell_target == "fifth_team":
                        fifth_team_space()
                        if team[4][1] < 3:
                            money += 1
                        elif team[4][1] < 6:
                            money += 2
                        else:
                            money += 3
                        if team[4][0] == "pig":
                            if team[4][1] < 3:
                                money += 1
                            elif team[4][1] < 6:
                                money += 2
                            else:
                                money += 3
                        team[4] = None
                    sell()

                if action[0] == "merge":
                    if action[1] == "first_team":
                        first_team_space()
                        if action[2] == "second_team":
                            second_team_space()
                            if team[0][1] < 3:
                                temp = (team[1][0], team[1][1] + 1)
                                team[1] = temp
                            elif team[0][1] < 6:
                                temp = (team[1][0], team[1][1] + 2)
                                team[1] = temp
                            else:
                                temp = (team[1][0], team[1][1] + 3)
                                team[1] = temp
                        elif action[2] == "third_team":
                            third_team_space()
                            if team[0][1] < 3:
                                temp = (team[2][0], team[2][1] + 1)
                                team[2] = temp
                            elif team[0][1] < 6:
                                temp = (team[2][0], team[2][1] + 2)
                                team[2] = temp
                            else:
                                temp = (team[2][0], team[2][1] + 3)
                                team[2] = temp
                        elif action[2] == "fourth_team":
                            fourth_team_space()
                            if team[0][1] < 3:
                                temp = (team[3][0], team[3][1] + 1)
                                team[3] = temp
                            elif team[0][1] < 6:
                                temp = (team[3][0], team[3][1] + 2)
                                team[3] = temp
                            else:
                                temp = (team[3][0], team[3][1] + 3)
                                team[3] = temp
                        elif action[2] == "fifth_team":
                            fifth_team_space()
                            if team[0][1] < 3:
                                temp = (team[4][0], team[4][1] + 1)
                                team[4] = temp
                            elif team[0][1] < 6:
                                temp = (team[4][0], team[4][1] + 2)
                                team[4] = temp
                            else:
                                temp = (team[4][0], team[4][1] + 3)
                                team[4] = temp
                        team[0] = None
                    elif action[1] == "second_team":
                        second_team_space()
                        if action[2] == "first_team":
                            second_team_space()
                            if team[1][1] < 3:
                                temp = (team[0][0], team[0][1] + 1)
                                team[0] = temp
                            elif team[1][1] < 6:
                                temp = (team[0][0], team[0][1] + 2)
                                team[0] = temp
                            else:
                                temp = (team[0][0], team[0][1] + 3)
                                team[0] = temp
                        elif action[2] == "third_team":
                            third_team_space()
                            if team[1][1] < 3:
                                temp = (team[2][0], team[2][1] + 1)
                                team[2] = temp
                            elif team[1][1] < 6:
                                temp = (team[2][0], team[2][1] + 2)
                                team[2] = temp
                            else:
                                temp = (team[2][0], team[2][1] + 3)
                                team[2] = temp
                        elif action[2] == "fourth_team":
                            fourth_team_space()
                            if team[1][1] < 3:
                                temp = (team[3][0], team[3][1] + 1)
                                team[3] = temp
                            elif team[1][1] < 6:
                                temp = (team[3][0], team[3][1] + 2)
                                team[3] = temp
                            else:
                                temp = (team[3][0], team[3][1] + 3)
                                team[3] = temp
                        elif action[2] == "fifth_team":
                            fifth_team_space()
                            if team[1][1] < 3:
                                temp = (team[4][0], team[4][1] + 1)
                                team[4] = temp
                            elif team[1][1] < 6:
                                temp = (team[4][0], team[4][1] + 2)
                                team[4] = temp
                            else:
                                temp = (team[4][0], team[4][1] + 3)
                                team[4] = temp
                        team[1] = None
                    elif action[1] == "third_team":
                        third_team_space()
                        if action[2] == "first_team":
                            second_team_space()
                            if team[2][1] < 3:
                                temp = (team[0][0], team[0][1] + 1)
                                team[0] = temp
                            elif team[2][1] < 6:
                                temp = (team[0][0], team[0][1] + 2)
                                team[0] = temp
                            else:
                                temp = (team[0][0], team[0][1] + 3)
                                team[0] = temp
                        elif action[2] == "second_team":
                            third_team_space()
                            if team[2][1] < 3:
                                temp = (team[1][0], team[1][1] + 1)
                                team[1] = temp
                            elif team[2][1] < 6:
                                temp = (team[1][0], team[1][1] + 2)
                                team[1] = temp
                            else:
                                temp = (team[1][0], team[1][1] + 3)
                                team[1] = temp
                        elif action[2] == "fourth_team":
                            fourth_team_space()
                            if team[2][1] < 3:
                                temp = (team[3][0], team[3][1] + 1)
                                team[3] = temp
                            elif team[2][1] < 6:
                                temp = (team[3][0], team[3][1] + 2)
                                team[3] = temp
                            else:
                                temp = (team[3][0], team[3][1] + 3)
                                team[3] = temp
                        elif action[2] == "fifth_team":
                            fifth_team_space()
                            if team[2][1] < 3:
                                temp = (team[4][0], team[4][1] + 1)
                                team[4] = temp
                            elif team[2][1] < 6:
                                temp = (team[4][0], team[4][1] + 2)
                                team[4] = temp
                            else:
                                temp = (team[4][0], team[4][1] + 3)
                                team[4] = temp
                        team[2] = None
                    elif action[1] == "fourth_team":
                        fourth_team_space()
                        if action[2] == "first_team":
                            second_team_space()
                            if team[3][1] < 3:
                                temp = (team[0][0], team[0][1] + 1)
                                team[0] = temp
                            elif team[3][1] < 6:
                                temp = (team[0][0], team[0][1] + 2)
                                team[0] = temp
                            else:
                                temp = (team[0][0], team[0][1] + 3)
                                team[0] = temp
                        elif action[2] == "third_team":
                            third_team_space()
                            if team[3][1] < 3:
                                temp = (team[2][0], team[2][1] + 1)
                                team[2] = temp
                            elif team[3][1] < 6:
                                temp = (team[2][0], team[2][1] + 2)
                                team[2] = temp
                            else:
                                temp = (team[2][0], team[2][1] + 3)
                                team[2] = temp
                        elif action[2] == "second_team":
                            fourth_team_space()
                            if team[3][1] < 3:
                                temp = (team[1][0], team[1][1] + 1)
                                team[1] = temp
                            elif team[3][1] < 6:
                                temp = (team[1][0], team[1][1] + 2)
                                team[1] = temp
                            else:
                                temp = (team[1][0], team[1][1] + 3)
                                team[1] = temp
                        elif action[2] == "fifth_team":
                            fifth_team_space()
                            if team[3][1] < 3:
                                temp = (team[4][0], team[4][1] + 1)
                                team[4] = temp
                            elif team[3][1] < 6:
                                temp = (team[4][0], team[4][1] + 2)
                                team[4] = temp
                            else:
                                temp = (team[4][0], team[4][1] + 3)
                                team[4] = temp
                        team[3] = None
                    elif action[1] == "fifth_team":
                        fifth_team_space()
                        if action[2] == "first_team":
                            second_team_space()
                            if team[4][1] < 3:
                                temp = (team[0][0], team[0][1] + 1)
                                team[0] = temp
                            elif team[4][1] < 6:
                                temp = (team[0][0], team[0][1] + 2)
                                team[0] = temp
                            else:
                                temp = (team[0][0], team[0][1] + 3)
                                team[0] = temp
                        elif action[2] == "third_team":
                            third_team_space()
                            if team[4][1] < 3:
                                temp = (team[2][0], team[2][1] + 1)
                                team[2] = temp
                            elif team[4][1] < 6:
                                temp = (team[2][0], team[2][1] + 2)
                                team[2] = temp
                            else:
                                temp = (team[2][0], team[2][1] + 3)
                                team[2] = temp
                        elif action[2] == "fourth_team":
                            fourth_team_space()
                            if team[4][1] < 3:
                                temp = (team[3][0], team[3][1] + 1)
                                team[3] = temp
                            elif team[4][1] < 6:
                                temp = (team[3][0], team[3][1] + 2)
                                team[3] = temp
                            else:
                                temp = (team[3][0], team[3][1] + 3)
                                team[3] = temp
                        elif action[2] == "second_team":
                            fifth_team_space()
                            if team[4][1] < 3:
                                temp = (team[1][0], team[1][1] + 1)
                                team[1] = temp
                            elif team[4][1] < 6:
                                temp = (team[1][0], team[1][1] + 2)
                                team[1] = temp
                            else:
                                temp = (team[1][0], team[1][1] + 3)
                                team[1] = temp
                        team[4] = None

                    if action[2] == "first_team":
                        first_team_space()
                    if action[2] == "second_team":
                        second_team_space()
                    if action[2] == "third_team":
                        third_team_space()
                    if action[2] == "fourth_team":
                        fourth_team_space()
                    if action[2] == "fifth_team":
                        fifth_team_space()

                if action == "roll":
                    roll()
                    money -= 1

                if action == "end_turn":
                    end_turn()
                    end_of_turn = False
            while (pyautogui.locateOnScreen(name, confidence=0.9)) is None:
                time.sleep(1)
            while (pyautogui.locateOnScreen(coin, confidence=0.9)) is None:
                time.sleep(3)
                click(200, 200)




    # TODO:
    # Check money at start of turn
    # Freezing