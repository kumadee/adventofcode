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


class Edge:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2
        self.distance = p1.distance(p2)

    def contains(self, p: Point) -> bool:
        return self.p1 == p or self.p2 == p

    def __str__(self) -> str:
        return f"Edge({self.p1}={self.p2}, distance={self.distance})"


@dataclass
class Circuit:
    edges: list[Edge]
    box_count: int

    def index(self, edge: Edge) -> tuple[int, int]:
        p1_index, p2_index = (-1, -1)

        for i, e in enumerate(self.edges):
            if p1_index == -1 and e.contains(edge.p1):
                p1_index = i
            if p2_index == -1 and e.contains(edge.p2):
                p2_index = i

        return (p1_index, p2_index)


def newPoint(line: str) -> Point:
    positions = line.split(",")
    if len(positions) != 3:
        raise ValueError(f"Not a valid position entry: {line}")
    return Point(int(positions[0]), int(positions[1]), int(positions[2]))


def solve(data: list[str], connect_pairs: int = -1) -> int:
    if connect_pairs == -1:
        connect_pairs = len(data)
    box_locations = [newPoint(line.strip()) for line in data]
    edges: list[Edge] = []
    # calculate distances between each point
    # it is represented as a matrix
    for i, box1 in enumerate(box_locations[0 : len(box_locations) - 1]):
        for box2 in box_locations[i + 1 :]:
            if box1 == box2:
                continue
            edges.append(Edge(box1, box2))

    edges_sorted_by_distance = sorted(edges, key=lambda x: x.distance)

    circuits: list[Circuit] = []
    for i, edge in enumerate(edges_sorted_by_distance):
        if i > connect_pairs:
            break
        p1_index, p2_index = (-1, -1)
        for circuit in circuits:
            p1_index, p2_index = circuit.index(edge)
            # both points in the edge are already part of circuit
            # nothing to do.
            if p1_index > -1 and p2_index > -1:
                break
            if (p1_index > -1 and p2_index == -1) or (p1_index == -1 and p2_index > -1):
                circuit.edges.append(edge)
                circuit.box_count += 1
                # FIXME: Can immediately continue with next edge
                break
        if p1_index == -1 and p2_index == -1:
            # add a new circuit
            circuits.append(Circuit(edges=[edge], box_count=2))

    # print(circuits)

    if len(circuits) < 3:
        raise ValueError(f"Total number of circuits: {circuits} is less than 3")
    size_of_circuits = sorted([c.box_count for c in circuits], reverse=True)
    print(size_of_circuits)
    return reduce(lambda x, y: x * y, size_of_circuits[0:3])
