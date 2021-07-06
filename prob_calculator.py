import copy
import random

from typing import Dict, List


class Hat:
    contents: List[str]

    def __init__(self, **contents: Dict[str, int]):
        self.contents = []
        for color, count in contents.items():
            self.contents.extend([color for _ in range(count)])

    def draw(self, count: int) -> List[str]:
        selected = []
        if count >= len(self.contents):
            return self.contents
        for i in range(count):
            index = random.randint(0, len(self.contents) - 1)
            selected.append(self.contents.pop(index))
        return selected


def experiment(hat: Hat, expected_balls: Dict[str, int],
               num_balls_drawn: int, num_experiments: int):

    has_balls = 0
    for experiment_count in range(num_experiments):
        exp_hat = copy.deepcopy(hat)  # Get a fresh hat
        result = exp_hat.draw(num_balls_drawn)  # Draw the balls

        # If every color has at least the expected amount, increment `has_balls`
        if all(result.count(color) >= count
               for color, count in expected_balls.items()):
            has_balls += 1

    return has_balls / num_experiments
