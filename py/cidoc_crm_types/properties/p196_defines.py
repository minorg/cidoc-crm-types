from dataclasses import dataclass


@dataclass
class P196Defines:
    """
Scope note: 
This property associates an instance of E18 Physical Thing with the instance of E92 Spacetime Volume that constitutes the complete trajectory of its geometric extent through spacetime for the whole time of the existence of the instance of E18 Physical Thing.
An instance of E18 Physical Thing not only occupies a particular geometric space at each instant of its existence, but in the course of its existence it also forms a trajectory through spacetime, which occupies a real, that is phenomenal, volume in spacetime, i.e., the instance of E92 Spacetime Volume this property associates it with. This real spatiotemporal extent of the instance of E18 Physical Thing is regarded as being unique, in all its details and fuzziness; the identity and existence of the E92 Spacetime Volume depends uniquely on the identity of the instance of E18 Physical Thing, whose existence defines it. It constitutes a phenomenal spacetime volume as defined in CRMgeo (Doerr and Hiebel 2013).
Included in this spacetime volume are both the spaces filled by the matter of the physical thing and any inner space that may exist, for instance the interior of a box. Physical things consisting of aggregations of physically unconnected objects, such as a set of chessmen, occupy a finite number of individually contiguous subsets of this spacetime volume equal to the number of objects that constitute the set and that are never connected during its existence.


In First Order Logic:
P196(x,y) &#8835; E18(x)
P196(x,y) &#8835; E92(y)
    """

    URI = "http://erlangen-crm.org/current/P196_defines"
