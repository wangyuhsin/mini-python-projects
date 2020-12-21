"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout', __dy=INITIAL_Y_SPEED):
        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(self.window_width-paddle_width)/2, y=(self.window_height-paddle_offset-paddle_height))
        self.paddle.filled = True
        self.paddle.color = '#513743'
        self.paddle.fill_color = '#513743'
        self.window.add(self.paddle)

        self.life_label = GLabel('● ● ●')
        self.life_label.font = '-15'
        self.life_label.color = '#c53d43'

        self.score_label = GLabel('score: 0')
        self.score_label.font = '-15'
        self.score_label.color = '#455765'

        self.brick_rows = BRICK_ROWS
        self.brick_cols = BRICK_COLS

        # Initialize our mouse listeners.
        onmousemoved(self.reset_paddle_location)

        # Draw bricks.
        self.create_bricks()

    def create_bricks(self, brick_offset=BRICK_OFFSET, brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT, brick_spacing=BRICK_SPACING):
        d_y = brick_offset
        color = ['#96514d', '#d3381c', '#2c4f54', '#00a381', '#008899', '#3e62ad', '#316745', '#028760', '#fabf14', '#274a78']
        for i in range(self.brick_rows):
            c = color[random.randint(0, 9)]
            d_x = 0
            for j in range(self.brick_cols - 1):
                brick = GRect(brick_width, brick_height, x=d_x, y=d_y)
                brick.filled = True
                brick.color = c
                brick.fill_color = brick.color
                self.window.add(brick)
                d_x = d_x + brick_width + brick_spacing
            brick = GRect(brick_width, brick_height, x=d_x, y=d_y)
            brick.filled = True
            brick.color = c
            brick.fill_color = brick.color
            self.window.add(brick)
            d_y = d_y + brick_height + brick_spacing

    def reset_paddle_location(self, mouse):
        if mouse.x >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width/2
        elif mouse.x <= 0:
            self.paddle.x = -self.paddle.width/2
        else:
            self.paddle.x = mouse.x - self.paddle.width/2

        # Default initial velocity for the ball.
    def get_dx(self):
        __dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            __dx = -__dx
        return __dx

    def get_dy(self):
        __dy = INITIAL_Y_SPEED
        return __dy

    def ball_collide_paddle(self):
        if self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height) is self.paddle:
            return True
        if self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height) is self.paddle:
            return True
        if self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y) is self.paddle:
            return True
        if self.window.get_object_at(self.ball.x, self.ball.y) is self.paddle:
            return True

    def ball_collide_brick(self):
        if self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height) is not None and self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height) is not self.paddle and self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height) is not self.life_label and self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height) is not self.score_label:
            self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height))
            return True
        if self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height) is not self.paddle and self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height) is not None and self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height) is not self.life_label and self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height) is not self.score_label:
            self.window.remove(self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height))
            return True
        if self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y) is not self.paddle and self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y) is not None and self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y) is not self.life_label and self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y) is not self.score_label:
            self.window.remove(self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y))
            return True
        if self.window.get_object_at(self.ball.x, self.ball.y) is not self.paddle and self.window.get_object_at(self.ball.x, self.ball.y) is not None and self.window.get_object_at(self.ball.x, self.ball.y) is not self.life_label and self.window.get_object_at(self.ball.x, self.ball.y) is not self.score_label:
            self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
            return True

    # Center a filled ball in the graphical window.
    def reset_ball_location(self, ball_radius=BALL_RADIUS):
        self.ball = GOval(ball_radius*2, ball_radius*2, x=self.window_width/2-ball_radius, y=self.window_height/2-ball_radius)
        self.ball.filled = True
        self.ball.color = '#705b67'
        self.ball.fill_color = self.ball.color
        self.window.add(self.ball)

    def lose(self):
        self.window.clear()
        lose_background = GRect(self.window.width, self.window.height)
        lose_background.filled = True
        lose_background.color = '#a6a5c4'
        lose_background.fill_color = '#a6a5c4'
        lose_label = GLabel('LOSE')
        lose_label.font = '-50'
        lose_label.color = '#e7e7eb'
        self.window.add(lose_background)
        self.window.add(lose_label, self.window.width/2-lose_label.width/2, self.window.height/2.5)
        self.window.add(self.score_label, (self.window_width-self.score_label.width)/2, lose_label.y+50)

    def win(self):
        self.window.clear()
        win_background = GRect(self.window.width, self.window.height)
        win_background.filled = True
        win_background.color = '#e5abbe'
        win_background.fill_color = '#e5abbe'
        win_label = GLabel('WIN')
        win_label.font = '-50'
        win_label.color = '#fdeff2'
        self.window.add(win_background)
        self.window.add(win_label, self.window.width/2-win_label.width/2, self.window.height/2.5)
        self.window.add(self.score_label, (self.window_width-self.score_label.width)/2, win_label.y+50)