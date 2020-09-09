from .e28_conceptual_object import E28ConceptualObject
from dataclasses import dataclass


@dataclass
class E89PropositionalObject(E28ConceptualObject):
    """
Scope note:
This class comprises immaterial items, including but not limited to stories, plots, procedural prescriptions, algorithms, laws of physics or images that are, or represent in some sense, sets of propositions about real or imaginary things and that are documented as single units or serve as topic of discourse.

This class also comprises items that are &#8220;about&#8221; something in the sense of a subject. In the wider sense, this class includes expressions of psychological value such as non-figural art and musical themes. However, conceptual items such as types and classes are not instances of E89 Propositional Object. This should not be confused with the definition of a type, which is indeed an instance of E89 Propositional Object.


Examples:
- Maxwell&#8217;s Equations (Huray, 2010)
- The ideational contents of Aristotle&#8217;s book entitled &#8216;Metaphysics&#8217; as rendered in the Greek texts translated in &#8230; Oxford edition&#8230;
- The underlying prototype of any &#8220;no-smoking&#8221; sign (E36)
- The common ideas of the plots of the movie "The Seven Samurai" by Akira Kurosawa and the movie &#8220;The Magnificent Seven&#8221; by John Sturges
- The image content of the photo of the Allied Leaders at Yalta published by UPI, 1945 (E36)
- The character "Little Red Riding Hood" variants of which appear amongst others in Grimm brothers&#8217; &#8216;Rotk&#228;ppchen&#8217;, other oral fairy tales and the film 'Hoodwinked'
- The place "Havnor" as invented by Ursula K. Le Guin for her &#8216;Earthsea&#8217; book series, the related maps and appearing in derivative works based on these novels


In First Order Logic:
E89(x) &#8835; E28(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E89_Propositional_Object"
