from dataclasses import dataclass


@dataclass
class P179HadSalesPrice:
    """
Scope note:
This property establishes the relationship between an instance of E96 Purchase and the instance of E97 Monetary Amount that forms the compensation for the transaction. The monetary amount agreed upon maychange in the course of the purchase activity.


Examples:	
- The sale of Vincent van Gogh&#8217;s &#8220;Vase with Fifteen Sunflowers&#8221; on 1987/03/30 (E96) had sales price Christies&#8217; hammer price for &#8220;Vase with Fifteen Sunflowers&#8221; (E97)


In First Order Logic:
P179(x,y) &#8835; E96(x)
P179(x,y) &#8835; E97(y)
    """

    URI = "http://erlangen-crm.org/current/P179_had_sales_price"
