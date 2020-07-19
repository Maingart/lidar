from numpy import partition
from matplotlib import pyplot, colors
from copy import deepcopy

def get_window(matrix:list, from_:int, to:int, column_index:int, n:int) -> list:
    return [matrix[i % n][column_index] for i in range(from_, to)]

def get_median(w:int) -> int:
    return (w - 1) // 2 if not (w % 2) else w // 2

def filter(matrix:list, n:int, m:int, w:int) -> list:
    median = get_median(w)
    for i in range(m):
        for j in range(n + w):
            from_, to = j, j + w
            window = get_window(matrix, from_, to, i, n)
            window[median] = partition(window, median)[median]
            matrix[(from_ + median) % n][i] = window[median]
    return matrix

def output_text(filtered_matrix:list):
    with open('output.txt', 'w') as fout:
        for scan in filtered_matrix:
            fout.write(' '.join(map(str, scan)) + '\n')

def output_graph(noisy_matrix:list, filtered_matrix:list):
    normlizer = colors.Normalize(vmin=min([min(scan) for scan in noisy_matrix]), 
                                 vmax=max([max(scan) for scan in noisy_matrix]))
    fig, axes = pyplot.subplots(2, 1)
    for ax, matrix in zip(axes.flat, [noisy_matrix, filtered_matrix]):
        im = ax.imshow(matrix, norm=normlizer)
    fig.colorbar(im, ax=axes.ravel().tolist(), orientation='horizontal')
    pyplot.show()

def main():
    fin = open('input.txt', 'r').read().split('\n')
    n, m, w = map(int, fin[0].split())
    matrix = [list(map(int, fin[i].split())) for i in range(1, n + 1)]
    filtered_matrix = filter(deepcopy(matrix), n, m, w)
    output_graph(matrix, filtered_matrix)

if __name__ == "__main__":
    main()
