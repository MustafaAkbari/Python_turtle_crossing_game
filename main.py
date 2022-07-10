import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    # Detect collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Detect when the player has reached to other side
    if player.ycor() > 290:
        score.increase_score()
        player.goto(0, -280)
        car.car_speed_increase()



screen.mainloop()

