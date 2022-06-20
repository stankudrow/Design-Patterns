from borg import Borg

class Singleborg(Borg):
    """Singleton based on Borg/Monostate pattern."""

    def __init__(self, **kwargs):
        super().__init__()
        self._state.update(kwargs)

def print_attrs(*args):
    """Print __dict__ of each argument."""
    for arg in args:
        print(f"{arg}: {arg.__dict__}")
    print()

if __name__ == '__main__':
    parent = Borg()
    child1 = Singleborg()
    parent.pr = "Parent"
    print_attrs(parent, child1)
    child1.ch1 = 'Child 1'
    print_attrs(parent, child1)
    child2 = Singleborg(question=21, answer=42)
    child2.ch2 = 'Child 2'
    print_attrs(parent, child1, child2)
