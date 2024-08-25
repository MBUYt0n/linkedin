import torch
from torch_geometric.data import Data
import json
import utils

g = utils.read_graph(path="data1.json")
nodes = [i["user"] for i in g]

x = torch.tensor([[g[node]["denom"]])