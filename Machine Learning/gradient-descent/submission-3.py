class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: float) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        for i in range(iterations) :
            next_init = 0
            next_init = init - learning_rate * 2 * init
            init = next_init
        return round(init, 5)