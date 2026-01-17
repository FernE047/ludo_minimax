from enum import Enum
from typing import Literal


class TileType(Enum):
    START = 0
    PATH = 1
    END_PATH = 2
    END = 3


class BoardTile:
    def __init__(self, tile_type: TileType) -> None:
        self.tile_type = tile_type
        self.next_tiles: list["BoardTile"] = []
        # because a tile can lead to multiple tiles (e.g., branching paths)
        self.accessible_to: Literal["All"] | int = "All"

    def set_tile_type(self, tile_type: TileType) -> None:
        self.tile_type = tile_type

    def add_next_tile(self, tile: "BoardTile") -> None:
        self.next_tiles.append(tile)

    def set_accessible_to(self, player_index: int | Literal["All"]) -> None:
        self.accessible_to = player_index

    def is_accessible_to(self, player_index: int) -> bool:
        return self.accessible_to == "All" or self.accessible_to == player_index

    def next_tiles_accessible_to(self, player_index: int) -> list["BoardTile"]:
        return [tile for tile in self.next_tiles if tile.is_accessible_to(player_index)]

    def tiles_ahead(self, steps: int, player_index: int) -> list["BoardTile"]:
        if steps == 0:
            return [self]
        tiles: list["BoardTile"] = []
        for next_tile in self.next_tiles_accessible_to(player_index):
            tiles.extend(next_tile.tiles_ahead(steps - 1, player_index))
        return tiles

    def __repr__(self) -> str:
        return f"BoardTile(type={self.tile_type}, accessible_to={self.accessible_to})"
