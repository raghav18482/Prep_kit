from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Player:
    name: str
    mark: str


class Board:
    def __init__(self, size: int = 3) -> None:
        self.size = size
        self.cells = [[" " for _ in range(size)] for _ in range(size)]

    def place(self, row: int, col: int, mark: str) -> None:
        if not (0 <= row < self.size and 0 <= col < self.size) or self.cells[row][col] != " ":
            raise ValueError("invalid move")
        self.cells[row][col] = mark

    def winner(self, mark: str) -> bool:
        lines = self.cells + [[self.cells[r][c] for r in range(self.size)] for c in range(self.size)]
        lines += [[self.cells[i][i] for i in range(self.size)], [self.cells[i][self.size - 1 - i] for i in range(self.size)]]
        return any(all(cell == mark for cell in line) for line in lines)


class Game:
    def __init__(self, first: Player, second: Player) -> None:
        self.players, self.board, self.turn = (first, second), Board(), 0

    def move(self, row: int, col: int) -> str | None:
        player = self.players[self.turn]
        self.board.place(row, col, player.mark)
        if self.board.winner(player.mark): return f"{player.name} wins"
        self.turn = 1 - self.turn
        return None


if __name__ == "__main__":
    game = Game(Player("A", "X"), Player("B", "O"))
    for move in [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]:
        result = game.move(*move)
    print(result)
