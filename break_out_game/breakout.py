"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao
"""
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3
BRICK_SCORE = 10

num_lives = NUM_LIVES
score = 0
graphics = BreakoutGraphics()
life_label = graphics.life_label
score_label = graphics.score_label


def main():
    """
    The main function of the Breakout game.
    """
    start()


def start():
    """
    Starts the game by resetting the ball location and adding labels to the window.
    """
    graphics.reset_ball_location()
    graphics.window.add(
        life_label,
        graphics.window.width - life_label.width - 30,
        life_label.height + 20,
    )
    graphics.window.add(score_label, 20, score_label.height + 20)
    onmouseclicked(serve)


def serve(event):
    """
    Serves the ball when the mouse is clicked.
    :param event: Mouse click event.
    """
    if 0 < event.x < graphics.window.width and 0 < event.y < graphics.window.height:
        global num_lives, score
        if (
            graphics.ball.x == (graphics.window_width -
                                graphics.ball.width) / 2
            and graphics.ball.y == (graphics.window_height - graphics.ball.height) / 2
        ):
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            while True:
                graphics.ball.move(dx, dy)
                if graphics.ball.x <= 0:
                    dx = -dx
                if graphics.ball.x >= graphics.window_width - graphics.ball.width:
                    dx = -dx
                if graphics.ball.y <= graphics.ball.height:
                    dy = -dy
                if graphics.ball.y >= graphics.window_height - graphics.ball.height:
                    graphics.window.remove(graphics.ball)
                    num_lives -= 1
                    lives = ""
                    for i in range(num_lives):
                        lives += "● "
                    life_label.text = lives
                    break
                if graphics.ball_collide_paddle():
                    dy = -dy
                if graphics.ball_collide_brick():
                    score += BRICK_SCORE
                    score_label.text = "score: " + str(score)
                    if score == BRICK_SCORE * graphics.brick_rows * graphics.brick_cols:
                        break
                    dy = -dy
                pause(FRAME_RATE)
            if num_lives > 0:
                if score == BRICK_SCORE * graphics.brick_rows * graphics.brick_cols:
                    graphics.win()
                else:
                    graphics.reset_ball_location()
            else:
                graphics.lose()


if __name__ == "__main__":
    main()
