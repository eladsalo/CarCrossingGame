from turtle import Screen, Turtle
from turtle_runner import TurtleRunner
from car import Car
from level_board import LevelBoard
import time
import pandas

def run():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle crossing game")
    screen.tracer(0)

    board = LevelBoard()
    player = TurtleRunner()

    screen.listen()
    screen.onkey(key="Up", fun=player.up)
    screen.onkey(key="n", fun=run)

    cars = []
    game_is_on = True
    start = time.time()
    game_speed = 0.3
    car_speed = 20
    car_creation_speed = 1
    while game_is_on:

        # create cars
        if time.time()-start >= car_creation_speed:
            start = time.time()
            c = Car()
            cars.append(c)

        # move all the cars
        for car in cars:
            if car.xcor() <= -320:
                cars.remove(car)
            else:
                car.forward(car_speed)

        # cross successfully to next level
        if player.ycor() >= 310:
            player.goto(0, -310)
            car_speed *= 1.1
            car_creation_speed *= 0.9
            #game_speed *= 0.9
            board.increase_level()

        # check collision with cars
        for car in cars:
            if player.distance(car.xcor(), car.ycor()) <= 25:
                game_is_on = False

        screen.update()
        time.sleep(game_speed)

    changed_index =check_highest_score(board)
    game_over(screen, board, changed_index )

    screen.exitonclick()


def game_over(screen, board,  changed_index):
    screen.clear()
    end_massage = Turtle()
    end_massage.penup()
    end_massage.hideturtle()
    end_massage.goto(0, 250)
    end_massage.write(f"GAME OVER!", True, align="center", font=("Ariel", 30, "normal"))
    screen.update()
    end_massage.goto(0, 100)
    end_massage.write(f"The game ended\n your level score is: {board.level} ",
                       True, align="center", font=("Ariel", 20, "normal"))
    screen.update()
    if changed_index >= 0:
        name = screen.textinput(title="New record", prompt="Enter your name")
        data = pandas.read_csv("best_scores.csv")
        data.loc[changed_index, 'name'] = name
        data.to_csv("best_scores.csv", index=False)

    data = pandas.read_csv("best_scores.csv")
    end_massage.goto(0, -100)
    end_massage.write(data, True, align="center", font=("Ariel", 20, "normal"))
    screen.update()

    time.sleep(5)
    screen.clear()
    end_massage.goto(0, -100)
    end_massage.write(f" press 'n' to start again", True, align="center", font=("Ariel", 24, "normal"))
    time.sleep(3)
    screen.clear()
    screen.listen()
    screen.onkey(key="n", fun=run)


def check_highest_score(board_game):
    data = pandas.read_csv("best_scores.csv")
    score_list = data["score"].to_list()
    names_list = data["name"].to_list()

    found_changes = False
    change_index = -1
    for num in range(3):
        if found_changes:
            break
        if board_game.level > score_list[0] and num == 0:

            data.loc[0, 'score'] = board_game.level

            data.loc[1, 'score'] = score_list[0]
            data.loc[1, 'name'] = names_list[0]

            data.loc[2, 'score'] = score_list[1]
            data.loc[2, 'name'] = names_list[1]
            change_index = 0
            found_changes = True
        elif board_game.level > score_list[1] and num == 1:

            data.loc[1, 'score'] = board_game.level

            data.loc[2, 'score'] = score_list[1]
            data.loc[2, 'name'] = names_list[1]
            change_index = 1
            found_changes = True
        elif board_game.level > score_list[2] and num == 2:
            data.loc[2, 'score'] = board_game.level
            change_index = 2
            found_changes = True

    data.to_csv("best_scores.csv", index=False)

    return change_index