import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io


def bubble_sort(arr, visualizer):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            visualizer(arr, f'Iteration {i * n + j + 1}')


def visualize(arr, title, frames):
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color='blue')
    ax.set_title(title)
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = Image.open(buf)
    frames.append(img)
    plt.close(fig)


def main():
    np.random.seed(0)
    arr = np.random.randint(1, 100, 10)  # Generate an array of random integers
    frames = []

    def visualizer(arr, title):
        visualize(arr, title, frames)

    bubble_sort(arr, visualizer)

    # Save frames as GIF
    frames[0].save('Pics/sorting_visualization.gif', save_all=True, append_images=frames[1:], optimize=False,
                   duration=100,
                   loop=0)


if __name__ == '__main__':
    main()
