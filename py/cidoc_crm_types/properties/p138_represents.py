from .p67_refers_to import P67RefersTo
from dataclasses import dataclass


@dataclass
class P138Represents(P67RefersTo):
    """
Scope note:
This property establishes the relationship between an instance of E36 Visual Item and the instance of E1 CRM Entity that it visually represents.

Any entity may be represented visually. This property is part of the fully developed path from E24 Physical Human-Made Thing through P65 shows visual item (is shown by), E36 Visual Item, P138 represents (has representation) to E1 CRM Entity, which is shortcut by P62depicts (is depicted by). P138.1 mode of representation allows the nature of the representation to be refined.

This property is also used for the relationship between an original and a digitisation of the original by the use of techniques such as digital photography, flatbed or infrared scanning. Digitisation is here seen as a process with a mechanical, causal component rendering the spatial distribution of structural and optical properties of the original and does not necessarily include any visual similarity identifiable by human observation."


Examples:
- the digital file found at http://www.emunch.no/N/full/No-MM_N0001-01.jpg (E36) represents page 1 of Edward Munch's manuscript MM N 1, Munch-museet (E22) mode of representation Digitisation(E55)
- The 3D model VAM_A.200-1946_trace_1M.ply (E73) represents Victoria & Albert Museum's Madonna and child sculpture (visual work) A.200-1946 (E22) mode of representation 3D surface (E55)


In First Order Logic:
P138(x,y) &#8835; E36(x)
P138(x,y) &#8835; E1(y)
P138(x,y,z) &#8835; [P138(x,y) &#8743; E55(z)]
P138(x,y) &#8835; P67(x,y)
    """

    URI = "http://erlangen-crm.org/current/P138_represents"
