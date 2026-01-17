from boards.boards import Board

def test_board_construction() -> None:
    board = Board(end_path_size=5, players_amount=1)
    assert len(board.start_tiles) == board.players_amount
    assert len(board.path_tiles) == board.path_size
    for player_index in range(board.players_amount):
        assert len(board.end_path_tiles[player_index]) == board.end_path_size + 1
    for player_index in range(board.players_amount):
        end_path = board.end_path_tiles[player_index]
        for tile in end_path:
            assert tile.is_accessible_to(player_index)
            for other_player in range(board.players_amount):
                if other_player != player_index:
                    assert not tile.is_accessible_to(other_player)
    assert board.board_size == len(board.path_tiles) + sum(len(end_path) for end_path in board.end_path_tiles) + len(board.start_tiles)
    first_path_tile = board.path_tiles[0]
    last_path_tile = board.path_tiles[-1]
    assert first_path_tile in last_path_tile.next_tiles
    section_size = board.section_size
    for index, path_tile in enumerate(board.path_tiles):
        if index % section_size == section_size - 2:
            end_player = (index // section_size + 1) % board.players_amount
            end_tile = path_tile.next_tiles[0]
            assert end_tile in board.end_path_tiles[end_player]
    print("Board construction test passed.")

test_board_construction()