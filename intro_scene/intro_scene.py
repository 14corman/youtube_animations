from manimlib import *

class Intro(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE_E, 1)

        # To get multiple animations done at once,
        # you the object into a VGroup, then you have
        # to make a function that performs the multiple
        # expected animates. Then, you can call ApplyFunction
        # on the VGroup passing in the function.
        group = VGroup(square)

        self.add(group)

        def square_left_func(mob):
            mob.shift(LEFT)
            mob.rotate(PI/2)
            return mob

        def square_right_func(mob):
            mob.shift(RIGHT)
            mob.rotate(-PI/2)
            return mob

        self.play(
            ApplyFunction(
                square_left_func,
                group,
                rate_func=there_and_back,
                run_time=2
            ),
        )

        self.play(
            ApplyFunction(
                square_right_func,
                group,
                rate_func=there_and_back,
                run_time=2
            ),
        )
        self.wait()