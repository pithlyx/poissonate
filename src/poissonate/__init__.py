import numpy as np
from scipy.spatial import cKDTree


class PoissonDiscSampler:
    def __init__(self, width, height, radius, num_samples=5):
        self.width = width
        self.height = height
        self.radius = radius
        self.num_samples = num_samples

        self.tau = 2 * np.pi
        self.cell_size = self.radius / np.sqrt(2)

        self.grid_width = int(np.ceil(self.width / self.cell_size))
        self.grid_height = int(np.ceil(self.height / self.cell_size))
        self.grid = np.empty((self.grid_width, self.grid_height), dtype=object)

    def grid_coords(self, point):
        return int(np.floor(point[0] / self.cell_size)), int(np.floor(point[1] / self.cell_size))

    def generate_point_around(self, point):
        alpha = self.tau * np.random.random()
        rad = self.radius * (np.random.random() + 1)
        return point[0] + rad * np.cos(alpha), point[1] + rad * np.sin(alpha)

    def generate_samples(self):
        first_point = self.width * np.random.random(), self.height * np.random.random()
        queue = [first_point]
        samples = [first_point]
        grid_x, grid_y = self.grid_coords(first_point)
        self.grid[grid_x, grid_y] = first_point

        tree = cKDTree(samples)

        while queue:
            point = queue.pop(np.random.randint(len(queue)))
            for _ in range(self.num_samples):
                new_point = self.generate_point_around(point)
                if 0 <= new_point[0] < self.width and 0 <= new_point[1] < self.height:
                    grid_x, grid_y = self.grid_coords(new_point)
                    idxs = tree.query_ball_point(new_point, self.radius)
                    if not idxs:
                        queue.append(new_point)
                        samples.append(new_point)
                        tree = cKDTree(samples)  # update tree
                        self.grid[grid_x, grid_y] = new_point
        return samples
