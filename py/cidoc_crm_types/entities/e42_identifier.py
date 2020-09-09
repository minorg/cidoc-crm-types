from .e41_appellation import E41Appellation
from dataclasses import dataclass


@dataclass
class E42Identifier(E41Appellation):
    """
Scope note:
This class comprises strings or codes assigned to instances of E1 CRM Entity in order to identify them uniquely and permanently within the context of one or more organisations. Such codes are often known as inventory numbers, registration codes, etc. and are typically composed of alphanumeric sequences. The class E42 Identifier is not normally used for machine-generated identifiers used for automated processing unless these are also used by human agents.


Examples:
- "MM.GE.195"
- "13.45.1976"
- "OXCMS: 1997.4.1"
- ISSN "0041-5278"
- ISRC "FIFIN8900116"
- Shelf mark "Res 8 P 10"
- "Guillaume de Machaut (1300?-1377)" [a controlled personal name heading that follows
the French rules] (Reaney, 1974)
- &#8220;+41 22 418 5571&#8221;
- weasel@paveprime.com
- &#8220;1-29-3 Otsuka, Bunkyo-ku, Tokyo, 121, Japan&#8221;
- &#8220;Rue David Dufour 5, CH-1211, Gen&#232;ve&#8221;


In First Order Logic:
E42(x) &#8835; E41(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E42_Identifier"
