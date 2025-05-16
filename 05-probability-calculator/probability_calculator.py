import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.__contents = []
        for key, val in kwargs.items():
            self.__contents += [key] * val

    def __repr__(self):
        return f"{self.__class__.__name__}(elements = {len(self.contents)})"
    
    def __str__(self):
        return f'\n(elements: {len(self.contents)})\n{self.contents}'
    
    def draw(self, num):
        if num > len(self.__contents):
            elements = copy.deepcopy(self.__contents)
            self.__contents.clear()
        else:
            elements = []
            for _ in range(num):
                ball = random.choice(self.__contents)
                elements.append(ball)
                self.__contents.remove(ball)
        
        return elements
    
    @property
    def contents(self):
        return self.__contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    hat_copy = copy.deepcopy(hat)
    for _ in range(num_experiments):
        if len(hat_copy.contents) < num_balls_drawn:
            hat_copy = copy.deepcopy(hat)
        ball_list = hat_copy.draw(num_balls_drawn)

        if all(ball_list.count(key) >= val
                for key, val in expected_balls.items()):
            count += 1
    
    return round(count / num_experiments, 3)


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)

print(probability)
