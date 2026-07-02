"""
Classic Snake Game using Python's built-in Turtle Graphics.
Runs smoothly on integrated graphics like Intel UHD.
Controls: Arrow Keys (Up, Down, Left, Right)
"""

import turtle
import time
import random

# ------------------------------
# Game Settings
# ------------------------------
WIDTH, HEIGHT = 600, 600
DELAY = 0.1  # seconds between frames (lower = faster)
SEGMENT_SIZE = 20

# Colors
BG_COLOR = "#1a1a2e"
SNAKE_HEAD_COLOR = "#e94560"
SNAKE_BODY_COLOR = "#0f3460"
FOOD_COLOR = "#f5c542"
TEXT_COLOR = "#ffffff"

# ------------------------------
# Setup Screen
# ------------------------------
screen = turtle.Screen()
screen.setup(WIDTH + 50, HEIGHT + 50)
screen.bgcolor(BG_COLOR)
screen.title("🐍 Snake Game - Python Turtle")
screen.tracer(0)  # Turn off automatic animation

# ------------------------------
# Snake Head
# ------------------------------
head = turtle.Turtle()
head.shape("square")
head.color(SNAKE_HEAD_COLOR)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake body list
segments = []

# ------------------------------
# Food
# ------------------------------
food = turtle.Turtle()
food.shape("circle")
food.color(FOOD_COLOR)
food.penup()
food.shapesize(stretch_len=0.8, stretch_wid=0.8)
food.goto(0, 100)

# ------------------------------
# Score Display
# ------------------------------
score_display = turtle.Turtle()
score_display.color(TEXT_COLOR)
score_display.penup()
score_display.hideturtle()
score_display.goto(0, HEIGHT//2 - 30)
score = 0
high_score = 0

def update_score_display():
    score_display.clear()
    score_display.write(f"Score: {score}   High Score: {high_score}",
                        align="center", font=("Courier", 20, "bold"))

update_score_display()

# ------------------------------
# Movement Functions
# ------------------------------
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + SEGMENT_SIZE)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - SEGMENT_SIZE)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - SEGMENT_SIZE)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + SEGMENT_SIZE)

# ------------------------------
# Keyboard Bindings
# ------------------------------
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# ------------------------------
# Helper: Generate New Food Location
# ------------------------------
def random_food_position():
    x = random.randint(-WIDTH//2 + SEGMENT_SIZE, WIDTH//2 - SEGMENT_SIZE)
    y = random.randint(-HEIGHT//2 + SEGMENT_SIZE, HEIGHT//2 - SEGMENT_SIZE)
    # Snap to grid for cleaner placement
    x = (x // SEGMENT_SIZE) * SEGMENT_SIZE
    y = (y // SEGMENT_SIZE) * SEGMENT_SIZE
    return x, y

# ------------------------------
# Collision Check with Body
# ------------------------------
def is_collision_with_body():
    for segment in segments:
        if head.distance(segment) < SEGMENT_SIZE // 2:
            return True
    return False

# ------------------------------
# Reset Game
# ------------------------------
def reset_game():
    global score, segments
    time.sleep(0.5)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide and clear old segments
    for seg in segments:
        seg.goto(1000, 1000)  # Move off-screen
    segments.clear()

    score = 0
    update_score_display()
    food.goto(random_food_position())

# ------------------------------
# Main Game Loop
# ------------------------------
def game_loop():
    global score, high_score

    while True:
        screen.update()

        # Check for border collision
        if (head.xcor() > WIDTH//2 - SEGMENT_SIZE or head.xcor() < -WIDTH//2 + SEGMENT_SIZE or
            head.ycor() > HEIGHT//2 - SEGMENT_SIZE or head.ycor() < -HEIGHT//2 + SEGMENT_SIZE):
            if score > high_score:
                high_score = score
            reset_game()

        # Check for food collision
        if head.distance(food) < SEGMENT_SIZE:
            # Move food to new spot
            food.goto(random_food_position())
            # Increase score
            score += 10
            if score > high_score:
                high_score = score
            update_score_display()

            # Add a new body segment
            new_segment = turtle.Turtle()
            new_segment.shape("square")
            new_segment.color(SNAKE_BODY_COLOR)
            new_segment.penup()
            new_segment.speed(0)
            segments.append(new_segment)

        # Move the body segments (last to first)
        for i in range(len(segments) - 1, 0, -1):
            x = segments[i-1].xcor()
            y = segments[i-1].ycor()
            segments[i].goto(x, y)

        # Move first segment to where the head is now
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        # Move the head
        move()

        # Check for self-collision
        if is_collision_with_body():
            if score > high_score:
                high_score = score
            reset_game()

        time.sleep(DELAY)

# ------------------------------
# Start the Game
# ------------------------------
try:
    game_loop()
except turtle.Terminator:
    # Handle window close gracefully
    pass