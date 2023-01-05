#!/usr/bin/env python3


# 1. cd here
# 2. run `python3 virus.py`


from time import time

from prototype import VirusCloner


class Virus(VirusCloner):
    """A submicroscopic infectious replicant."""

    def __init__(self, life_time: float, birth_rate: float):
        self.id = hash(time())
        self.life_time = life_time
        self.birth_rate = birth_rate

    def __repr__(self):
        return f"Virus({self.life_time}, {self.birth_rate})"

    def __str__(self):
        return f"{repr(self)}_{self.id}"


if __name__ == "__main__":
    virus = Virus(2.1, 4.2)
    pool = [virus.clone() for _ in range(10)]
    print(f"A pool of viruses:\n{pool}\n")
