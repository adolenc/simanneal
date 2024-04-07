import random
from simanneal import Annealer


class NQueensProblem(Annealer):
    def move(self):
        """Move a queen on a random column to some different row."""
        column = random.randrange(len(self.state))
        new_row = random.randrange(len(self.state))
        self.state[column] = new_row

    def energy(self):
        """Calculates the number of attacks among the queens."""
        e = 0
        for i in range(len(self.state)):
            for j in range(i + 1, len(self.state)):
                e += self.state[i] == self.state[j]
                e += abs(i - j) == abs(self.state[i] - self.state[j])
        return e


if __name__ == '__main__':
    init_state = list(range(10))
    random.shuffle(init_state)
    print(init_state)

    nqueens = NQueensProblem(init_state)
    nqueens.set_schedule(nqueens.auto(minutes=0.2))
    # stop as soon as we hit 0 attacks
    nqueens.min_energy = 0
    nqueens.copy_strategy = "slice"
    state, e = nqueens.anneal()

    print()
    print("number of attacks: %i" % e)
    print(state)
