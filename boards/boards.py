from typing import cast
from boards.board_tyles import TileType, BoardTile


class Board:
    """the board class represents the game board with tiles and their connections.
    it's not supposed to handle any game logic, just the structure of the board."""
    def __init__(self, end_path_size: int = 5, players_amount: int = 4) -> None:
        self.start_tiles: list[BoardTile] = []
        self.players_amount = players_amount
        self.end_path_size = end_path_size
        self.section_size = self.end_path_size * 2 + 3
        self.path_size = self.players_amount * self.section_size
        self.board_size = self.path_size + self.players_amount * (
            self.end_path_size + 2
        )
        self.path_tiles: list[BoardTile] = []
        self.end_path_tiles: list[list[BoardTile]] = [[] for _ in range(players_amount)]
        self.build_tiles()

    def build_tiles(self) -> None:
        start_tile = BoardTile(TileType.START)
        start_tile.set_accessible_to(0)
        self.start_tiles.append(start_tile)
        previous_tile = start_tile
        first_tile: BoardTile | None = None
        for index in range(self.path_size):
            locality = index % self.section_size
            path_tile = BoardTile(TileType.PATH)
            if first_tile is None:
                first_tile = path_tile
            if locality == 0 and index != 0:
                start_tile = BoardTile(TileType.START)
                start_tile.set_accessible_to(index // self.section_size)
                start_tile.add_next_tile(path_tile)
                self.start_tiles.append(start_tile)
            if locality == self.section_size - 2:
                end_player = (index // self.section_size + 1) % self.players_amount
                end_tile = BoardTile(TileType.END_PATH)
                end_tile.set_accessible_to(end_player)
                path_tile.add_next_tile(end_tile)
                previous_end_tile = path_tile
                self.end_path_tiles[end_player].append(end_tile)
                for _ in range(self.end_path_size - 1):
                    end_tile = BoardTile(TileType.END_PATH)
                    end_tile.set_accessible_to(end_player)
                    previous_end_tile.add_next_tile(end_tile)
                    previous_end_tile = end_tile
                    self.end_path_tiles[end_player].append(end_tile)
                final_end_tile = BoardTile(TileType.END)
                final_end_tile.set_accessible_to(end_player)
                previous_end_tile.add_next_tile(final_end_tile)
                self.end_path_tiles[end_player].append(final_end_tile)
            previous_tile.add_next_tile(path_tile)
            self.path_tiles.append(path_tile)
            previous_tile = path_tile
        first_tile = cast(BoardTile, first_tile)
        previous_tile.add_next_tile(first_tile)