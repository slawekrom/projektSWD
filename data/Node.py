from typing import List

from pandas import DataFrame
import dataclasses
from dataclasses import dataclass
from marshmallow.schema import BaseSchema
from marshmallow_dataclass import add_schema


@dataclass
@add_schema(base_schema=BaseSchema)
class Node:
    node_type: str
    node_attribute: str
    used_attributes: List[str]
    node_entropy: float
    df: DataFrame
    children: List['Node'] = dataclasses.field(default_factory=lambda: [])

    def __init__(self, node_type: str = '', node_attribute: str = '', df: DataFrame = None, children=None) -> None:
        if children is None:
            children = []
        self.children: List[Node] = children
        self.node_type: str = node_type
        self.node_attribute: str = node_attribute
        self.df = df
