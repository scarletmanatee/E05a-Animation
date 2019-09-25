#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines

"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade
# Dictates the size and name of the window created
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Move Mouse Example"


class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        # Sets the x postion of the ball to a variable
        self.position_x = position_x
        # Sets the y postion of the ball to a variable
        self.position_y = position_y
        # Sets the radius of the ball to a variable
        self.radius = radius
        # Sets the color of the ball to a variable
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # sets the background color to grey
        arcade.set_background_color(arcade.color.ASH_GREY) 

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)
        
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        # Gets rid of the ball at the old location
        arcade.start_render()
        # Draws the Ball
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        # sets ball position to mouse position x
        self.ball.position_x = x
        # sets ball position to mouse position y
        self.ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        # Prints a message when you click left mouse button, and also changes the color of the ball to black
        
        print(f"You clicked button number: {button}")
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.BLACK

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        # changes the color of the ball back to red
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.AUBURN


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()