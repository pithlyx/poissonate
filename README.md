# PoissonDiscSampler

This file implements a Poisson Disc Sampling algorithm using the `numpy` and `scipy` libraries in Python. The Poisson Disc Sampling algorithm generates a set of points in a given 2D space such that no two points are closer than a specified distance (radius) apart. It is commonly used in computer graphics, image processing, and simulations.

## Usage

To use the `PoissonDiscSampler` class, you can follow these steps:

1. Import the necessary libraries:

   ```python
   import numpy as np
   from scipy.spatial import cKDTree
   ```

2. Create an instance of the PoissonDiscSampler class, providing the width and height of the 2D space, the desired radius, and an optional number of samples per point:

   ```python
   sampler = PoissonDiscSampler(width, height, radius, num_samples=5)
   ```

3. Generate the samples by calling the `generate_samples` method:

   ```python
   samples = sampler.generate_samples()
   ```

   The generate_samples method returns a list of generated sample points in the form of (x, y) coordinates.

## **Class Details**

### `PoissonDiscSampler` Class

#### Constructor

```python
def __init__(self, width, height, radius, num_samples=5):
```

The constructor initializes the `PoissonDiscSampler` object with the specified parameters:

- `width` (float): The width of the 2D space in which the points will be generated.
- `height` (float): The height of the 2D space in which the points will be generated.
- `radius` (float): The minimum distance between any two generated points.
- `num_samples` (int, optional): The number of samples to generate around each point. Defaults to 5.

#### Attributes

- `width` (float): The width of the 2D space.
- `height` (float): The height of the 2D space.
- `radius` (float): The minimum distance between any two points.
- `num_samples` (int): The number of samples to generate around each point.
- `tau` (float): The value of 2 \* pi.
- `cell_size` (float): The size of a grid cell based on the radius.
- `grid_width` (int): The number of grid cells in the horizontal direction.
- `grid_height` (int): The number of grid cells in the vertical direction.
- `grid` (list): A list representing the grid used for spatial partitioning.

#### Methods

- `grid_coords(point)`:
  - Returns the grid coordinates (grid_x, grid_y) of a given point.
  - Arguments:
    - `point` (tuple): The (x, y) coordinates of a point.
  - Returns:
    - `(grid_x, grid_y)` (tuple): The grid coordinates of the point.
- `generate_point_around(point)`:
  - Generates a new point within a disc centered at the given point.
  - Arguments:
    - `point` (tuple): The (x, y) coordinates of a point.
  - Returns:
    - `(new_x, new_y)` (tuple): The (x, y) coordinates of the generated point.
- `generate_samples()`:
  - Generates the samples using the Poisson Disc Sampling algorithm.
  - Returns:
    - `samples` (list): A list of generated sample points in the form of (x, y) coordinates.

The `PoissonDiscSampler` class uses a grid-based approach to improve the efficiency of the algorithm. It divides the 2D space into a grid of cells, each with a size determined by the radius. This grid helps in quickly finding nearby points for a given point during the sampling process.

The algorithm starts by randomly selecting a point within the 2D space as the first sample point. It adds this point to the samples list and the grid. Then, it creates a `cKDTree` object from the sample points for efficient nearest neighbor searches.

Next, the algorithm enters a loop where it randomly selects a point from the queue. For each selected point, it generates a fixed number of new points around it using the `generate_point_around` method. These new points are checked against the boundary of the 2D space to ensure they are within the valid region.

For each new point, its grid coordinates are calculated using the `grid_coords` method. The algorithm queries the `cKDTree` to find any existing points within the specified radius of the new point. If no points are found, the new point is added to the queue, samples list, and grid. The `cKDTree` is updated to include the new point, improving subsequent nearest neighbor searches.

The loop continues until the queue becomes empty, meaning no more points are available to generate samples. Finally, the algorithm returns the list of generated sample points.

---

This `PoissonDiscSampler` implementation provides a convenient way to generate well-distributed points within a 2D space with a minimum distance constraint. It can be used in various applications such as terrain generation, pattern generation, and sampling-based algorithms in computer graphics and simulations.
