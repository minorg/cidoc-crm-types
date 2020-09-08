from .e54_dimension import E54Dimension
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E97MonetaryAmount(E54Dimension):
    P179i_was_sales_price_of: Tuple[object, ...] = ()  # Range: E96Purchase
