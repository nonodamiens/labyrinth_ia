# coding: utf-8

"""
Les différentes classes du jeu
"""

class Joueur:
    """
    Le sprite contrôlé par le joueur
    
    Le sprite à besoin :
    - d'un graphisme
    - d'un emplacement (coordonnées)
    """

class lab:
    """
    Le plan du labyrinthe

    objectif :
    -> Création du schéma du labyrinthe en aléatoire mais reconductible (choix du random seed ?)
    -> Pour démarrer on fera juste des case couloir et des cases mur avec une case d'entrée et une case de sortie
    -> liste de nombres
    """

class NomDeMaClasse:
    """Docstring de ma classe"""
    
    attribut_de_classe = 'valeur'

    def __init__(self, arg1, arg2): # Méthode constructeur
        """Docstring de notre constructeur"""
        self.attribut1 = arg1
        self.attribut2 = arg2
        self.attribut3 = 'valeur'

        self._attribut_caché # Attribut interdit d'accés externe (convention)

        NomDeMaClasse.attribut_de_classe = 'valeur' # exemple compteur.objet_crees += 1

    def methode1(self, arg): # Une méthode
        """Docstring de la methode1"""
        self.attribut1 = arg
        self.attribut2 = 'valeur'

    def methode_de_classe(cls):
        """Docstring de la methode de classe"""
        cls.attribut_de_classe = 'valeur'

    attribut_de_classe2 = classmethod(methode_de_classe)

    def methode_static():
        """Docstring de la methode statique"""
        attribut = 'valeur'
    
    attribut_de_classe3 = staticmethod(methode_static)

    def _methode_caché(self):
        """Docstring de la methode cachée (non accessible à l'extérieur de la classe par convention)"""
        return 'valeur'

    def _get_attribut_caché(self):
        """Méthode cachée qui sera appelée quand on souhaitera accéder en lecture à l'attribut _attribut_caché"""
        return self._attribut_caché

    def _set_attribut_caché(self, valeur):
        """Méthode appelée quand on souhaite modifier l'attribut caché"""
        self._attribut_caché = valeur

    # On va dire à Python que notre attribut pointe vers une propriété
    # On peut rajouter 2 methodes : suppression et aide
    attribut_non_caché = property(_get_attribut_caché, _set_attribut_caché)