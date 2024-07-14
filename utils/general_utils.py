import torch
import itertools


def calculate_MMCS(learned_features, true_features, device):
    if not isinstance(true_features, torch.Tensor):
        true_features = torch.tensor(true_features, dtype=torch.float32)

    if learned_features.shape[0] != true_features.shape[0]:
        learned_features = learned_features.t()
        true_features = true_features.t()

    learned_features = learned_features.to(device).float()
    true_features = true_features.to(device).float()

    learned_norm = torch.nn.functional.normalize(learned_features, p=2, dim=0)
    true_norm = torch.nn.functional.normalize(true_features, p=2, dim=0)

    cos_sim_matrix = torch.matmul(learned_norm.t(), true_norm)
    max_cos_sims = torch.max(cos_sim_matrix, dim=0).values

    mmcs = torch.mean(max_cos_sims).item()

    return mmcs, cos_sim_matrix


def geometric_median(points: torch.Tensor, max_iter: int = 100, tol: float = 1e-5):
    points = torch.stack(points)
    points = points.unsqueeze(0)

    guess = points.mean(dim=0)
    prev = torch.zeros_like(guess)

    weights = torch.ones(len(points), device=points.device)

    for _ in range(max_iter):
        prev = guess

        diff = points - guess.unsqueeze(0)
        distances = torch.norm(diff, dim=1)

        weights = 1 / torch.clamp(distances, min=1e-8)
        weights /= weights.sum()

        guess = (weights.unsqueeze(1) * points).sum(dim=0)

        if torch.norm(guess - prev) < tol:
            break

    return guess


def find_combinations(grid):
    keys, values = zip(*grid.items())
    for v in itertools.product(*values):
        yield dict(zip(keys, v))
