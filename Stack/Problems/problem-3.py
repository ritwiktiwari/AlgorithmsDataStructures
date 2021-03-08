"""
Tower of Bramha
Tower of Hanoi
3 Tower
3 Rods
"""

steps = 0


def tower(disks: int, source: int, destination: int, middle: int):
    global steps
    steps += 1
    if disks == 1:
        print(f"Moving disk {disks} from {source} -> {destination}")
        return
    else:
        tower(disks - 1, source, middle, destination)
        print(f"Moving disk {disks} from {source} -> {destination}")
        tower(disks - 1, middle, destination, source)


tower(disks=4, source='A', destination='C', middle='B')
print("Total steps:", steps)
