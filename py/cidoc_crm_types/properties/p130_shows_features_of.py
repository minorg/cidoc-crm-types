from dataclasses import dataclass


@dataclass
class P130ShowsFeaturesOf:
    """
Scope note:
This property generalises the notions of "copy of" and "similar to" into a directed relationship, where the domain expresses the derivative or influenced item and the range the source or influencing item, if such a direction can be established. The property can also be used to express similarity in cases that can be stated between two objects only, without historical knowledge about its reasons. The property expresses a symmetric relationship in case no direction of influence can be established either from evidence on the item itself or from historical knowledge. This holds in particular for siblings of a derivation process from a common source or non-causal cultural parallels, such as some weaving patterns.

The P130.1 kind of similarity property of the P130 shows features of (features are also found on) property enables the relationship between the domain and the range to be further clarified, in the sense from domain to range, if applicable. For example, it may be expressed if both items are product &#8220;of the same mould&#8221;, or if two texts &#8220;contain identical paragraphs&#8221;.

If the reason for similarity is a sort of derivation process, i.e., that the creator has used or had in mind the form of a particular thing during the creation or production, this process should be explicitly modelled. In these cases, P130 shows features of can be regarded as a shortcut of such a process. However, the current model does not contain any path specific enough to infer this property. Specializations of the CIDOC CRM may however be more explicit, for instance describing the use of moulds etc.


In First Order Logic:
P130 (x,y) &#8835; E70(x)
P130 (x,y) &#8835; E70(y)
P130(x,y,z) &#8835; [P130(x,y) &#8743; E55(z)]
    """

    URI = "http://erlangen-crm.org/current/P130_shows_features_of"
