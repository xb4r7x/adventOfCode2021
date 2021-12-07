import numpy as np

SIZE = 5

def parseInput(filePath: str) -> tuple[np.ndarray, np.ndarray]:
    """ returns (input_sequence, boards), where boards is a 3D array """
    with open(filePath) as f:
        [firstline] = f.readline().rsplit()
        input_seq = np.fromstring(firstline, sep=',', dtype=int)
        boards = np.genfromtxt(f, dtype=int)
        return input_seq, boards.reshape((len(boards)//SIZE, SIZE, SIZE))

def find_winning_boards(masks: np.ndarray) -> list[int]:
    """ Returns the indices of masks(& boards) that have a row or col completed """
    return [i for i, masks in enumerate(masks)
                      if any(any(masks.sum(axis=axis) == SIZE) for axis in (0, 1))]

def get_winning_scores(input_seq: np.ndarray, boards: np.ndarray) -> list[int]:
    """ Returns the list of board scores in the order that the boards win """
    scores = []
    masks = np.zeros(shape=boards.shape)
    for num in input_seq:
        masks = np.logical_or(masks, boards == num)
        for board_idx in find_winning_boards(masks):
            scores.append(sum(boards[board_idx][~masks[board_idx]]) * num)
            boards[board_idx] = -1
            masks[board_idx] = False
    return scores

if __name__ == "__main__":
    winning_scores = get_winning_scores(*parseInput('input.txt'))
    print(winning_scores[0])
    print(winning_scores[-1])