from .e71_man_made_thing import E71ManMadeThing
from dataclasses import dataclass


@dataclass
class E28ConceptualObject(E71ManMadeThing):
    """
Scope note:
This class comprises non-material products of our minds and other human produced data that have become objects of a discourse about their identity, circumstances of creation or historical implication. The production of such information may have been supported by the use of technical devices such as cameras or computers.

Characteristically, instances of this class are created, invented or thought by someone, and then may be documented or communicated between persons. Instances of E28 Conceptual Object have the ability to exist on more than one particular carrier at the same time, such as paper, electronic signals, marks, audio media, paintings, photos, human memories, etc.

They cannot be destroyed. They exist as long as they can be found on at least one carrier or in at least one human memory. Their existence ends when the last carrier and the last memory are lost. 


Examples:
- Beethoven?s ?Ode an die Freude? (Ode to Joy) (E73) (Kershaw, 1999)
- the definition of ?ontology? in the Oxford English Dictionary (E73)
- the knowledge about the victory at Marathon carried by the famous runner (E89)
[explanation note: In the following examples we illustrate the distinction between a propositional object,
its names and its encoded forms. The Maxwell equations are a good example, because they belong to the
fundamental laws of physics and their mathematical content yields identical, unambiguous results
regardless formulation and encoding]
- ?Maxwell equations? [preferred subject access point from LCSH] (E41)  http://lccn.loc.gov/sh85082387 [5], as of 19 November 2012]
**explanation: This is only the name for the Maxwell equations as standardized by the Library of Congress and NOT the equations themselves.
- ?Equations, Maxwell? [variant subject access point, from the same source] (E41)
**explanation: This is another name for the equation standardized by the Library of Congress and not the equations themselves
- Maxwell's equations (E89)
** explanation: This is the propositional content of the equations proper, independent of any particular notation or mathematical formalism.
- The encoding of Maxwells equations as in https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Maxwell [6]'s Equations.svg/500pxMaxwell'sEquations.svg.png (E73)
** explanation: This is one possible symbolic encoding of the propositional content of the equations.


In First Order Logic:
E28(x) ? E71(x)
    """


