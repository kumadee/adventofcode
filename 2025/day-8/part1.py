from dataclasses import dataclass
from functools import reduce
from typing import Self


@dataclass
class Point:
    x: int
    y: int
    z: int

    def distance(self, other: Self) -> int:
        return (
            (other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return other.x == self.x and other.y == self.y and other.z == self.z
        return False

    def __hash__(self) -> int:
        return hash(f"{self.x},{self.y},{self.z}")


def newPoint(line: str) -> Point:
    positions = line.split(",")
    if len(positions) != 3:
        raise ValueError(f"Not a valid position entry: {line}")
    return Point(int(positions[0]), int(positions[1]), int(positions[2]))


def solve(data: list[str], connect_pairs: int = -1) -> int:
    if connect_pairs == -1:
        connect_pairs = len(data)
    box_locations = [newPoint(line) for line in data]
    distance_matrix: list[dict[Point, int]] = []
    # calculate distances between each point
    # it is represented as a matrix
    for box1 in box_locations:
        boxes_sorted_by_distance = {}
        for box2 in box_locations:
            if box1 == box2:
                continue
            boxes_sorted_by_distance[box2] = box1.distance(box2)
        distance_matrix.append(boxes_sorted_by_distance)

    circuits = []
    for i, box1 in enumerate(box_locations):
        if i > connect_pairs:
            break
        # find shortest distance from other
        boxes_sorted_by_distance = sorted(
            distance_matrix[i].keys(), key=lambda x: distance_matrix[i][x]
        )
        print("--------------")
        print(f"Boxes closer to {box1} are:")
        for box in boxes_sorted_by_distance:
            print(f"{box} => {distance_matrix[i][box]}")
        box2 = boxes_sorted_by_distance[0]
        # TODO: create a circuit between box1 and box2 if it doesn't already exist
        # directly or indirectly
        for circuit in circuits:
            if box2 in circuit:
                continue

        # if box1 and point 2 are already in the same existing circuit then nothing to do
        # else create a new circuit with box1 and box2
        circuits.append([box1, box2])
        continue

    if len(circuits) < 3:
        raise ValueError(f"Total number of circuits: {circuits} is less than 3")
    size_of_circuits = sorted([len(c) for c in circuits], reverse=False)
    return reduce(lambda x, y: x * y, size_of_circuits[0:3])
