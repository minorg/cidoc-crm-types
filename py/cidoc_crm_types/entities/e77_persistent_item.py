from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E77PersistentItem(E1CRMEntity):
    """
Scope note:
This class comprises items that have persistent characteristics of structural nature substantially related to their identity and their integrity, sometimes known as ?endurants? in philosophy. Persistent Items may be physical entities, such as people, animals or things, conceptual entities such as ideas, concepts, products of the imagination or even names.

Instances of E77 Persistent Item may be present or be part of interactions in different periods or events. They can repeatedly be recognized at disparate occasions during their existence by characteristics of structural nature. The respective characteristics need not be exactly the same during all the existence of an instance of E77 Persistent Item. Often, they undergo gradual change, still bearing some similarities with that of previous times, or dissappear completely and new emerge. For instance, a person, from the time of being born on, will gradually change all its features and acquire new ones, such as a scar. Even the DNA in different body cells will develop defects and mutations. Nevertheless, relevant characteristics use to be sufficiently similar to recognize the instance for some substantial period of time. 
The more specific criteria that determine the identity of instances of subclasses of E77 Persistent Item may vary considerably and are described of referred to in the respective scope notes. The decision about which exact criteria to use depends on whether the observable behaviour of the respective part of reality such confined conforms to the reasoning the user is interested in. For example, a building can be regarded as no longer existing if it is dismantled and the materials reused in a different configuration. On the other hand, human beings go through radical and profound changes during their life-span, affecting both material composition and form, yet preserve their identity by other criteria, such as being bodily separated from other persons. Similarly, inanimate objects may be subject to exchange of parts and matter. On the opposite, the identity of a (version of a) text of a scientific publication is given by the exact arrangement of its relevant symbols.
The main classes of objects that fall outside the scope of the E77 Persistent Item class are temporal objects such as periods, events and acts, and descriptive properties. An instance of E77 Persistent Item does not require actual knowledge of the identifying features of the instance being currently known. There may be cases, where the actual identifying features of an instance
of E77 Persistent Item are not decidable at a particular state of knowledge. 


Examples:
- Leonard da Vinci (Strano, 1953)
- Stonehenge (Richards, 2005)
- the hole in the ozone layer (Hufford and Horwitz, 2005)
- the First Law of Thermodynamics (Craig and Gislason, 2002)
- the Bermuda Triangle (Dolan, 2005)


In First Order Logic:
E77(x) ? E1(x)
    """

    P12_was_present_at: Tuple[object, ...] = ()  # Range: E5Event
    P92_was_brought_into_existence_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P93_was_taken_out_of_existence_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
