from .e8_acquisition import E8Acquisition
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E96Purchase(E8Acquisition):
    P179_had_sales_price: Tuple[object, ...] = ()  # Range: E97MonetaryAmount
