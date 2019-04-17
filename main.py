#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# =============================================================================
# =============================================================================
# # Import
# =============================================================================
# =============================================================================


# import random pas utile ET SURTOUT fait tout buguer buildozer :'(

import numpy as np  # Pour sqrt et son module random intégré !

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import RiseInTransition, FadeTransition,\
    FallOutTransition, WipeTransition
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# En gros pour le Pong (attention aux dépendances):
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty,\
    NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock

# Pour les Lapinous (attention aux dépendances):
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


# =============================================================================
# =============================================================================
# # On définit chaque écran de l'application
# =============================================================================
# =============================================================================


class MenuPrincipal(Screen):

    def quitter_app(self):
        App.get_running_app().stop()
        Window.close()


class Credits(Screen):
    pass


# =============================================================================
# Monty Hall
# =============================================================================


class MenuSelectionMH(Screen):
    pass


class portes3(Screen):

    text = StringProperty('Une porte cache une voiture, les 2 autres une chèvre. Choisissez une porte!')
#images quand les boutons seront desactivés
    i1 = StringProperty('opendoorgoat.png')
    i2 = StringProperty('opendoorgoat.png')
    i3 = StringProperty('opendoorgoat.png')
#active ou désactive les boutons associés aux portes
    p1 = BooleanProperty(False)
    p2 = BooleanProperty(False)
    p3 = BooleanProperty(False)
#opacité de chaque boutons associés aux portes
    o1 = NumericProperty(0.5)
    o2 = NumericProperty(0.5)
    o3 = NumericProperty(0.5)
#permet de savoir si le click est le premier ou le second effectué
    secondclick = BooleanProperty(False)

    def press1(self, **kwargs):  #désactive un bouton cachant une chèvre au hasard en choisissant la premiere porte
        self.text = 'Une porte cachant une chèvre a été ouverte, voulez-vous choisir une autre porte?'
        self.secondclick = True
        self.o1 = 1
        self.porteVoiture = np.random.randint(1, 4) # 1 inclu, 4 exclu
        self.porteSupp = 1
        while self.porteSupp==self.porteVoiture or self.porteSupp==1:
            self.porteSupp = np.random.randint(1, 4) # 1 inclu, 4 exclu
        if self.porteSupp == 2:
            self.p2 = True
        else:
            self.p3 = True

    def press2(self, **kwargs):
        self.text = 'Une porte cachant une chèvre a été ouverte, voulez-vous choisir une autre porte?'
        self.secondclick = True
        self.o2 = 1
        self.porteVoiture = np.random.randint(1, 4) # 1 inclu, 4 exclu
        self.porteSupp = 2
        while self.porteSupp==self.porteVoiture or self.porteSupp==2:
            self.porteSupp = np.random.randint(1, 4) # 1 inclu, 4 exclu
        if self.porteSupp == 1:
            self.p1 = True
        else:
            self.p3 = True

    def press3(self, **kwargs):
        self.text = 'Une porte cachant une chèvre a été ouverte, voulez-vous choisir une autre porte?'
        self.secondclick = True
        self.o3 = 1
        self.porteVoiture = np.random.randint(1, 4) # 1 inclu, 4 exclu
        self.porteSupp = 3
        while self.porteSupp == self.porteVoiture or self.porteSupp == 3:
            self.porteSupp = np.random.randint(1, 4) # 1 inclu, 4 exclu
        if self.porteSupp == 1:
            self.p1 = True
        else:
            self.p2 = True

    def secondpress1(self, **kwargs):  #désactive tous les boutons, affiche gagné ou perdu, et place une image avec une voiture derriere la porte gagnante
        self.o1 = 1
        self.o2 = .3
        self.o3 = .3
        if self.porteVoiture == 1:
            self.i1 = 'doorcar.png'
        if self.porteVoiture == 2:
            self.i2 = 'doorcar.png'
        if self.porteVoiture == 3:
            self.i3 = 'doorcar.png'
        if self.porteVoiture == 1:
            self.text = 'Gagné!'
        else:
            self.text = 'Perdu...'
        self.p1 = True
        self.p2 = True
        self.p3 = True

    def secondpress2(self, **kwargs):
        self.o1 = .3
        self.o2 = 1
        self.o3 = .3
        if self.porteVoiture == 1:
            self.i1 = 'doorcar.png'
        if self.porteVoiture == 2:
            self.i2 = 'doorcar.png'
        if self.porteVoiture == 3:
            self.i3 = 'doorcar.png'
        if self.porteVoiture == 2:
            self.text = 'Gagné!'
        else:
            self.text = 'Perdu...'
        self.p1 = True
        self.p2 = True
        self.p3 = True

    def secondpress3(self, **kwargs):
        self.o1 = .3
        self.o2 = .3
        self.o3 = 1
        if self.porteVoiture == 1:
            self.i1 = 'doorcar.png'
        if self.porteVoiture == 2:
            self.i2 = 'doorcar.png'
        if self.porteVoiture == 3:
            self.i3 = 'doorcar.png'
        if self.porteVoiture == 3:
            self.text = 'Gagné!'
        else:
            self.text = 'Perdu...'
        self.p1 = True
        self.p2 = True
        self.p3 = True

    def pressback(self, **kwargs):  #réinitialise toutes les variables
        self.text = 'Une porte cache une voiture, les 2 autres une chèvre. Choisissez une porte!'

        self.i1 = 'opendoorgoat.png'
        self.i2 = 'opendoorgoat.png'
        self.i3 = 'opendoorgoat.png'

        self.p1 = False
        self.p2 = False
        self.p3 = False

        self.o1 = 0.5
        self.o2 = 0.5
        self.o3 = 0.5

        self.secondclick = False

# Fonctions utiles pour SimulMH


def is_number(s):  # évalue la valeur rentré par l'utilisateur
    try:
        eval(s)
        return True
    except:
        return False


def ecart(n, p):
    return np.sqrt(p*(1-p)/n) *2.58 # intervalle de confiance à 99%


class SimulMH(Screen):
    #défini le nombre de victoires en changeant de portes, initialisé à 0, et le transforme en string
    porte = 0
    textporte = StringProperty(str(porte))
#permet de récupérer la value du slider
    s1 = ObjectProperty()
#réponse affiché
    textlancer = StringProperty('Validé!')
    porteanswer = StringProperty('')
#permet de désactiver certaines boutons et textinput
    probatext = BooleanProperty(False)
    disporte = BooleanProperty(False)

    def press(self, **kwargs):  #vérifie la réponse statistiquement
        self.userporte = self.ids.userporte.text

        if is_number(self.userporte):

            for i in range(0, int(self.ids.s1.value)):
                self.portes = ("Voiture", "Chèvre", "Chèvre")
                self.porte_choisie = self.portes[np.random.randint(0, 3)]  # 3 exclu
                self.porte_restante = 'Chèvre' if self.porte_choisie == "Voiture" else "Voiture"
                if self.porte_restante == 'Voiture':
                    self.porte+=1
            self.probatext = True
            if eval(self.userporte) - ecart(int(self.ids.s1.value), eval(self.userporte)) < self.porte /int(self.ids.s1.value)< eval(self.userporte) + ecart(int(self.ids.s1.value), eval(self.userporte)):
                self.porteanswer = 'La réponse est validée car elle est suffisement proche du résultat de la simulation sur ' + str(self.ids.s1.value) +  ' parties ! Bravo !'
                popup1 = Popup(title=';)', content=Image(source='Meme_Probability.jpg'), size_hint=(0.7, 0.7), size=self.size, auto_dismiss=True)
                popup1.open()
                popup2 = Popup(title='Bravo ! ! Voici une petite explication pour que ça soit un peu plus clair pour toi !', content=Image(source='MH_Arbre.png'), size_hint=(0.7, 0.7), size=self.size, auto_dismiss=True)
                popup2.open()
            else:
                self.porteanswer = 'La réponse est refusée car elle est trop éloignée du résultat de la simulation sur ' + str(self.ids.s1.value) +  ' parties ...'
            self.textporte = str(self.porte)
            self.disporte = True

    def pressback(self, **kwargs):  #réinitialise toutes les variables
        self.porte = 0
        self.textporte = str(self.porte)
        self.probatext = False
        self.porteanswer = ''

        self.disporte = False


class AideMH(Screen):
    pass


# =============================================================================
# 3Dés
# =============================================================================


class MenuSelection3des(Screen):
    pass


class Aide3Des(Screen):
    pass


class Lancer3DesTuto(Screen):

    image1 = StringProperty('dice.png')
    image2 = StringProperty('dice.png')
    image3 = StringProperty('dice.png')

    texte_paire_tuto = StringProperty('0')
    texte_brelan_tuto = StringProperty('0')
    texte_suite_tuto = StringProperty('0')

    paire = 0
    brelan = 0
    suite = 0

    str_nombre_lancers = StringProperty('0')
    nombre_lancers = 0

    def pressLancer(self, **kwargs):
        self.de1 = np.random.randint(1, 7)  # 1 inclu, 7 exclu
        self.de2 = np.random.randint(1, 7)  # 1 inclu, 7 exclu
        self.de3 = np.random.randint(1, 7)  # 1 inclu, 7 exclu
        if self.de1 == 1:
            self.image1 = 'de1.png'  #associe à chaque valeur de dé, l'image qui correspond
        if self.de1 == 2:
            self.image1 = 'de2.png'
        if self.de1 == 3:
            self.image1 = 'de3.png'
        if self.de1 == 4:
            self.image1 = 'de4.png'
        if self.de1 == 5:
            self.image1 = 'de5.png'
        if self.de1 == 6:
            self.image1 = 'de6.png'

        if self.de2 == 1:
            self.image2 = 'de1.png'
        if self.de2 == 2:
            self.image2 = 'de2.png'
        if self.de2 == 3:
            self.image2 = 'de3.png'
        if self.de2 == 4:
            self.image2 = 'de4.png'
        if self.de2 == 5:
            self.image2 = 'de5.png'
        if self.de2 == 6:
            self.image2 = 'de6.png'

        if self.de3 == 1:
            self.image3 = 'de1.png'
        if self.de3 == 2:
            self.image3 = 'de2.png'
        if self.de3 == 3:
            self.image3 = 'de3.png'
        if self.de3 == 4:
            self.image3 = 'de4.png'
        if self.de3 == 5:
            self.image3 = 'de5.png'
        if self.de3 == 6:
            self.image3 = 'de6.png'
#vérifie si les dés forment une paire, brelan... et les compte
        l = [self.de1, self.de2, self.de3]
        l.sort()
        if l[0] == l[1] == l[2]:
            self.brelan += 1
        elif l[0] == l[1] or l[0] == l[2] or l[1] == l[2]:
            self.paire += 1
        if l[1] == l[2]-1 and l[0] == l[1]-1:
            self.suite += 1
        self.texte_paire_tuto = str(self.paire)
        self.texte_brelan_tuto = str(self.brelan)
        self.texte_suite_tuto = str(self.suite)
        self.nombre_lancers += 1
        self.str_nombre_lancers = str(self.nombre_lancers)

    def retour(self):
        self.paire = 0  # On réinitialise les valeurs
        self.brelan = 0
        self.suite = 0
        self.nombre_lancers = 0

        self.texte_paire_tuto = str(self.paire)
        self.texte_brelan_tuto = str(self.brelan)
        self.texte_suite_tuto = str(self.suite)
        self.str_nombre_lancers = str(self.nombre_lancers)

        self.image1 = 'dice.png'
        self.image2 = 'dice.png'
        self.image3 = 'dice.png'


class Simul3D(Screen):
    paire = 0
    brelan = 0
    suite = 0
    textpaire = StringProperty(str(paire))
    textbrelan = StringProperty(str(brelan))
    textsuite = StringProperty(str(suite))

    textlancer = StringProperty('Validé!')
    paireanswer = StringProperty('')
    brelananswer = StringProperty('')
    suiteanswer = StringProperty('')

    disable = BooleanProperty(False)

    def press(self, **kwargs):
        self.userpaire = self.ids.userpaire.text
        self.userbrelan = self.ids.userbrelan.text
        self.usersuite = self.ids.usersuite.text
        if is_number(self.userpaire) and is_number(self.userbrelan) and is_number(self.usersuite):

            for i in range(0, 10000):
                de1 = np.random.randint(1, 7) # 1 inclu, 7 exclu
                de2 = np.random.randint(1, 7) # 1 inclu, 7 exclu
                de3 = np.random.randint(1, 7) # 1 inclu, 7 exclu
                l = [de1, de2, de3]
                l.sort()
                if l[0]==l[1]==l[2]:  #comptabilise les paires, brelans...
                    self.brelan+=1
                elif l[0]==l[1] or l[0]==l[2] or l[1]==l[2]:
                    self.paire+=1
                if l[1]==l[2]-1 and l[0]==l[1]-1:
                    self.suite+=1
                self.textpaire = str(self.paire)
                self.textbrelan = str(self.brelan)
                self.textsuite = str(self.suite)
#vérifie statistiquement en calculant un intervalle de confiance
            if float(eval(self.userpaire)) - ecart(10000, float(eval(self.userpaire))) < self.paire /10000< float(eval(self.userpaire)) + ecart(10000, float(eval(self.userpaire))):
                self.paireanswer = 'La réponse est validée car elle est suffisement proche du résultat de la simulation'
            else:
                self.paireanswer = 'La réponse est refusée car elle est trop éloignée du résultat de la simulation'
            if float(eval(self.userbrelan)) - ecart(10000, float(eval(self.userbrelan))) < self.brelan /10000< float(eval(self.userbrelan)) + ecart(10000, float(eval(self.userbrelan))):
                self.brelananswer = 'La réponse est validée car elle est suffisement proche du résultat de la simulation'
            else:
                self.brelananswer = 'La réponse est refusée car elle est trop éloignée du résultat de la simulation'
            if float(eval(self.usersuite)) - ecart(10000, float(eval(self.usersuite))) < self.suite /10000< float(eval(self.usersuite)) + ecart(10000, float(eval(self.usersuite))):
                self.suiteanswer = 'La réponse est validée car elle est suffisement proche du résultat de la simulation'
            else:
                self.suiteanswer = 'La réponse est refusée car elle est trop éloignée du résultat de la simulation'
            self.disable = True

    def pressback(self, **kwargs):  #réinitialise les valeurs
        self.paire = 0
        self.brelan = 0
        self.suite = 0
        self.textpaire = str(self.paire)
        self.textbrelan = str(self.brelan)
        self.textsuite = str(self.suite)

        self.paireanswer = ''
        self.brelananswer = ''
        self.suiteanswer = ''

        self.disable = False


# =============================================================================
# 4Dés
# =============================================================================


class MenuSelection4des(Screen):
    pass


class Aide4Des(Screen):
    pass


class Lancer4DesTuto(Screen):
    image1 = StringProperty('dice.png')
    image2 = StringProperty('dice.png')
    image3 = StringProperty('dice.png')
    image4 = StringProperty('dice.png')

    texte_paire_tuto = StringProperty('0')
    texte_brelan_tuto = StringProperty('0')
    texte_suite_tuto = StringProperty('0')
    texte_paire2_tuto = StringProperty('0')
    texte_carre_tuto = StringProperty('0')

    paire = 0
    brelan = 0
    suite = 0
    carre = 0
    paire2 = 0

    str_nombre_lancers = StringProperty('0')
    nombre_lancers = 0

    def pressLancer(self, **kwargs):
        self.de1 = np.random.randint(1, 7) # 1 inclu, 7 exclu
        self.de2 = np.random.randint(1, 7) # 1 inclu, 7 exclu
        self.de3 = np.random.randint(1, 7) # 1 inclu, 7 exclu
        self.de4 = np.random.randint(1, 7) # 1 inclu, 7 exclu

        if self.de1 == 1:  #associe à chaque dé l'mage qui correspond
            self.image1 = 'de1.png'
        if self.de1 == 2:
            self.image1 = 'de2.png'
        if self.de1 == 3:
            self.image1 = 'de3.png'
        if self.de1 == 4:
            self.image1 = 'de4.png'
        if self.de1 == 5:
            self.image1 = 'de5.png'
        if self.de1 == 6:
            self.image1 = 'de6.png'

        if self.de2 == 1:
            self.image2 = 'de1.png'
        if self.de2 == 2:
            self.image2 = 'de2.png'
        if self.de2 == 3:
            self.image2 = 'de3.png'
        if self.de2 == 4:
            self.image2 = 'de4.png'
        if self.de2 == 5:
            self.image2 = 'de5.png'
        if self.de2 == 6:
            self.image2 = 'de6.png'

        if self.de3 == 1:
            self.image3 = 'de1.png'
        if self.de3 == 2:
            self.image3 = 'de2.png'
        if self.de3 == 3:
            self.image3 = 'de3.png'
        if self.de3 == 4:
            self.image3 = 'de4.png'
        if self.de3 == 5:
            self.image3 = 'de5.png'
        if self.de3 == 6:
            self.image3 = 'de6.png'

        if self.de4 == 1:
            self.image4 = 'de1.png'
        if self.de4 == 2:
            self.image4 = 'de2.png'
        if self.de4 == 3:
            self.image4 = 'de3.png'
        if self.de4 == 4:
            self.image4 = 'de4.png'
        if self.de4 == 5:
            self.image4 = 'de5.png'
        if self.de4 == 6:
            self.image4 = 'de6.png'

        l = [self.de1, self.de2, self.de3, self.de4]  #vérifie la présence de paire, suites...
        l.sort()
        if l[0]==l[1]==l[2]==l[3]:
            self.carre+=1
        elif l[0]==l[1]==l[2] or l[1]==l[2]==l[3] or l[0]==l[1]==l[3] or l[0]==l[2]==l[3]:
            self.brelan+=1
        elif l[0]==l[1]and l[2]==l[3]:
            self.paire2+=1
        elif l[0]==l[1] or l[1]==l[2] or l[2]==l[3]:
            self.paire+=1
        if l[3] - 3 == l[2] - 2 == l[1] - 1 == l[0]:
            self.suite+=1
        self.texte_paire_tuto = str(self.paire)
        self.texte_brelan_tuto = str(self.brelan)
        self.texte_suite_tuto = str(self.suite)
        self.texte_carre_tuto = str(self.carre)
        self.texte_paire2_tuto = str(self.paire2)
        self.nombre_lancers += 1
        self.str_nombre_lancers = str(self.nombre_lancers)

    def retour(self):  #réinitialise les valeurs
        self.paire = 0
        self.brelan = 0
        self.suite = 0
        self.carre = 0
        self.paire2 = 0
        self.nombre_lancers = 0

        self.texte_paire_tuto = str(self.paire)
        self.texte_brelan_tuto = str(self.brelan)
        self.texte_suite_tuto = str(self.suite)
        self.texte_carre_tuto = str(self.carre)
        self.texte_paire2_tuto = str(self.paire2)
        self.str_nombre_lancers = str(self.nombre_lancers)

        self.image1 = 'dice.png'
        self.image2 = 'dice.png'
        self.image3 = 'dice.png'
        self.image4 = 'dice.png'


class Simul4D(Screen):
    paire = 0
    brelan = 0
    suite = 0
    carre = 0
    paire2 = 0

    textpaire = StringProperty(str(paire))
    textbrelan = StringProperty(str(brelan))
    textsuite = StringProperty(str(suite))
    textcarre = StringProperty(str(carre))
    textpaire2 = StringProperty(str(paire2))

    textlancer = StringProperty('Validé!')
    paireanswer = StringProperty('')
    brelananswer = StringProperty('')
    suiteanswer = StringProperty('')
    carreanswer = StringProperty('')
    paire2answer = StringProperty('')

    disable = BooleanProperty(False)

    def press(self, **kwargs):  #meme chose que pour 3 dés mais en ajoutant un dé, ainsi que carré et double paire
        self.userpaire = self.ids.userpaire.text
        self.userbrelan = self.ids.userbrelan.text
        self.usersuite = self.ids.usersuite.text
        self.usercarre = self.ids.usercarre.text
        self.userpaire2 = self.ids.userpaire2.text
        if is_number(self.userpaire) and is_number(self.userbrelan) and is_number(self.usersuite) and is_number(self.usercarre) and is_number(self.userpaire2):

            for i in range(0, 10000):
                de1 = np.random.randint(1, 7) # 1 inclu, 7 exclu
                de2 = np.random.randint(1, 7) # 1 inclu, 7 exclu
                de3 = np.random.randint(1, 7) # 1 inclu, 7 exclu
                de4 = np.random.randint(1, 7) # 1 inclu, 7 exclu
                l = [de1, de2, de3, de4]
                l.sort()
                if l[0]==l[1]==l[2]==l[3]:
                    self.carre+=1
                elif l[0]==l[1]==l[2] or l[1]==l[2]==l[3] or l[0]==l[1]==l[3] or l[0]==l[2]==l[3]:
                    self.brelan+=1
                elif l[0]==l[1]and l[2]==l[3]:
                    self.paire2+=1
                elif l[0]==l[1] or l[1]==l[2] or l[2]==l[3]:
                    self.paire+=1
                if l[3] - 3 == l[2] - 2 == l[1] - 1 == l[0]:
                    self.suite+=1
                self.textpaire = str(self.paire)
                self.textbrelan = str(self.brelan)
                self.textsuite = str(self.suite)
                self.textcarre = str(self.carre)
                self.textpaire2 = str(self.paire2)

            if float(eval(self.userpaire)) - ecart(10000, float(eval(self.userpaire))) < self.paire /10000< float(eval(self.userpaire)) + ecart(10000, float(eval(self.userpaire))):
                self.paireanswer = 'La réponse est validée car elle est suffisement proche du résultat de la simulation'
            else:
                self.paireanswer = 'La réponse est refusée car elle est trop éloignée du résultat de la simulation'
            if float(eval(self.userbrelan)) - ecart(10000, float(eval(self.userbrelan))) < self.brelan /10000< float(eval(self.userbrelan)) + ecart(10000, float(eval(self.userbrelan))):
                self.brelananswer = 'La réponse est validée car elle est suffisement proche du résultat de la simulation'
            else:
                self.brelananswer = 'La réponse est refusée car elle est trop éloignée du résultat de la simulation'
            if float(eval(self.usersuite)) - ecart(10000, float(eval(self.usersuite))) < self.suite /10000< float(eval(self.usersuite)) + ecart(10000, float(eval(self.usersuite))):
                self.suiteanswer = 'La réponse est validée car elle est suffisement proche du résultat de la simulation'
            else:
                self.suiteanswer = 'La réponse est refusée car elle est trop éloignée du résultat de la simulation'
            if float(eval(self.usercarre)) - ecart(10000, float(eval(self.usercarre))) < self.carre /10000< float(eval(self.usercarre)) + ecart(10000, float(eval(self.usercarre))):
                self.carreanswer = 'La réponse est validée car elle est suffisement proche du résultat de la simulation'
            else:
                self.carreanswer = 'La réponse est refusée car elle est trop éloignée du résultat de la simulation'
            if float(eval(self.userpaire2)) - ecart(10000, float(eval(self.userpaire2))) < self.paire2 /10000< float(eval(self.userpaire2)) + ecart(10000, float(eval(self.userpaire2))):
                self.paire2answer = 'La réponse est validée car elle est suffisement proche du résultat de la simulation'
            else:
                self.paire2answer = 'La réponse est refusée car elle est trop éloignée du résultat de la simulation'
            self.disable = True

    def pressback(self, **kwargs):  #réinitialise les variables
        self.paire = 0
        self.brelan = 0
        self.suite = 0
        self.carre = 0
        self.paire2 = 0

        self.textpaire = str(self.paire)
        self.textbrelan = str(self.brelan)
        self.textsuite = str(self.suite)
        self.textcarre = str(self.carre)
        self.textpaire2 = str(self.paire2)

        self.paireanswer = ''
        self.brelananswer = ''
        self.suiteanswer = ''
        self.carreanswer = ''
        self.paire2answer = ''

        self.disable = False


# =============================================================================
# Calculatrice
# =============================================================================


class CalcGridLayout(GridLayout):

    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


# =============================================================================
# =============================================================================
# # Jeux
# =============================================================================
# =============================================================================


# =============================================================================
# Pong
# =============================================================================


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(PongGame, self).__init__(*args, **kwargs)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def serve_ball(self, vel=(10, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

    # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

    # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(10, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-10, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class Screen1(Screen):
    pass


class Pong(Screen):
    pass


class Screen1Bis(Screen):
    pass


class Screen1BisBis(Screen):
    pass


# =============================================================================
# Lapinous
# =============================================================================


# On declare deux ecrans 'Menu' et 'Game'
class MenuScreen(Screen):

    def build(self):
        self.name='Menu_Lapins'#On donne un nom a l'ecran C'EST LE NOM QU'ON APPELLE DANS LE .KV
        #Une image de fond:
        self.add_widget(Image(source='land.png',allow_stretch=True,keep_ratio=False))
        #On definie un layout pour cet ecran:
        Menu_Layout = BoxLayout(padding=100,spacing=10,orientation='vertical')
        #On cree un bouton pour lancer le jeu:
        self.Bouton_Jeu=Button(text='Lapiiiiiiiins ! !')
        self.Bouton_Jeu.font_size=Window.size[0]*0.05
        self.Bouton_Jeu.background_color=[0,0,0,0.2]
        self.Bouton_Jeu.bind(on_press=self.Vers_Game)
        #On ajoute le bouton dans l'affichage:
        Menu_Layout.add_widget(self.Bouton_Jeu)
        #On cree un bouton qui nrentre au menu principal:
        self.Bouton_Rien=Button(text='Retour')
        self.Bouton_Rien.font_size=Window.size[0]*0.05
        self.Bouton_Rien.background_color=[0,0,0,0.2]
        self.Bouton_Rien.bind(on_press=self.Vers_Menu_Principal)
        #On ajoute le bouton dans l'affichage:
        Menu_Layout.add_widget(self.Bouton_Rien)
        #On ajoute ce layout dans l'ecran:
        self.add_widget(Menu_Layout)

    def Vers_Game(self,instance):#Fonction de transition vers 'Game'
        Game=GameScreen()
        Game.build()#On construit l'ecran 'Game'
        sm.add_widget(Game)#On ajoute l'ecran dans le screen manager
        sm.current='Game'#On definit 'Menu' comme ecran courant

    def Vers_Menu_Principal(self,instance):
        sm.current = 'EE'
        sm.transition.direction = 'right'


class GameScreen(Screen):

    def build(self):
        self.name='Game'#On donne un nom a l'ecran
        Game_Layout=Jeu()#Creation du jeu
        Game_Layout.debut()#Initialisation du jeu
        self.add_widget(Game_Layout)#On l'ajoute dans l'ecran
        Menu_Layout = FloatLayout()
        #On cree un bouton pour quitter le jeu:
        self.Bouton_Rien=Button(text='Retour', font_size=0.25*self.height, text_size = self.size, halign = 'center', valign = 'middle', size_hint=(0.1, 0.1), pos_hint={'x':0, 'y':.5})
        self.Bouton_Rien.background_color=[0,0,0,0.2]
        self.Bouton_Rien.bind(on_press=self.Vers_Menu_Lapins)
        #On ajoute le bouton dans l'affichage:
        Menu_Layout.add_widget(self.Bouton_Rien)
        #On ajoute ce layout dans l'ecran:
        self.add_widget(Menu_Layout)

    def Vers_Menu_Lapins(self,instance):
        sm.current = 'Menu_Lapins'
        sm.transition.direction = 'right'


class Lapin(Widget):

    def __init__(self,canvas):
        self.dy=-15
        self.canvas=canvas
        #Taille et position aleatoire:
        self.size=(Window.size[0]*0.05,Window.size[1]*0.1)
        self.x = np.random.randint(0,int(Window.size[0]-self.size[0]))
        self.y=Window.size[1]-100
        #Ajout de l'image du lapin:
        with self.canvas:
            self.dessin = Rectangle(source='lapin.png',size=self.size, pos=self.pos)
        #Detection des mouvements:
        self.bind(pos=self.update_canvas)

    def update_canvas(self, *args):#Mise a jour des positions de l'image:
        self.dessin.pos = self.pos

    def move(self):
        #On recalcule les positions:
        self.y=self.y+self.dy
        #On teste la fin de la chute:
        if self.y<=0-self.size[1]:
            #Repositionnement aleatoire en haut:
            self.y=Window.size[1]
            self.x=np.random.randint(0,int(Window.size[0]-self.size[0]))

    def prise(self):#Changement d'image pour le succes:
        self.dy=0#On stoppe la chute
        #Position au dessus du panier pour stopper la collision:
        self.y=Window.size[1]*0.2
        self.dessin.source='YES.png'#Nouvelle image
        #On lance le nouveau lapin dans 0.5 seconde:
        Clock.schedule_once(self.prise_fin, 0.5)

    def prise_fin(self,dt):#Retour a l'image de lapin et en haut:
        self.y=0-self.size[1]#On le place en dessous pour qu'il remonte
        self.dessin.source='lapin.png'   #On change l'image
        self.dy=-15    #On relance la chute


class Panier(Widget):

    def __init__(self, canvas):
        self.canvas=canvas
        #Taille et position:
        self.size = (Window.size[0]*0.1,Window.size[1]*0.1)
        self.pos = (0,Window.size[1]*0.02)
        #Ajout de l'image (add_wiget fonctionne aussi):
        with self.canvas:
            self.dessin = Rectangle(source='panier.png',size=self.size, pos=self.pos)
        #On associe le mouvement du panier et son image:
        self.bind(pos=self.update_canvas)

    def update_canvas(self, *args):#Mise a jour des positions de l'image:
        self.dessin.pos = self.pos

class Jeu(FloatLayout):

    def debut(self):
        #On recupere la taille de l'ecran:
        self.size=Window.size
        #On charge les sons :
        self.son_yes = SoundLoader.load('YES.ogg')
        #Une image de fond:
        self.add_widget(Image(source='fond1.jpg',allow_stretch=True,keep_ratio=False))

        #Un label pour le score:
        self.score=0#Creation de la variable score
        self.label=Label(text='Score : '+str(self.score),markup=True)
        #Taille de la police en fonction de l'ecran:
        self.label.font_size=self.size[0]*0.05
        #Le label ne doit pas ecraser tout l'ecran:
        self.label.size_hint=(None,None)
        #Position du label vers le centre de l'ecran:
        self.label.pos=(Window.size[0]*0.47,Window.size[1]*0.45)
        self.label.color=[0,0,0,1]
        #On ajoute le label dans l'ecran du jeu:
        self.add_widget(self.label)

        #Creation du panier:
        self.panier=Panier(self.canvas)
        #Creation des lapins:
        self.lapins=[]
        for i in range(0,5):#On ajoute les lapins
            self.lapins.append(Lapin(self.canvas))

        #Creation des chiffres pour de depart:
        self.compteur_anim=3
        self.chiffre=Image(source='3.png',allow_stretch=True,keep_ratio=False)
        self.chiffre.size_hint=(0,0)
        self.chiffre.pos=self.center
        self.add_widget(self.chiffre)
        #Lancement de l'animation start:
        self.animation_start()

        #Depart de l'horloge du jeu:
        Clock.schedule_interval(self.update_chute, 4.0/100.0)

    def update_chute(self,dt):#Chute des lapins et tests de collisions
        for lapin in self.lapins:
            lapin.move()
            if lapin.collide_widget(self.panier):
                    lapin.prise()#Animation de la capture
                    self.score+=1
                    self.label.text='Score : '+str(self.score)
                    self.son_yes.play()

    def on_touch_move(self,touch):#Deplacement du panier
        if touch.y<self.size[1]/3:
            self.panier.center_x=touch.x

    def animation_start(self):#Depart de l'animation start
        #On compose l'animation avec deux anim successives:
        anim = Animation(pos=(0,0),size=self.size,t='in_quad',duration=0.8)
        anim += Animation(pos=self.center,size=(0,0),duration=0.8)
        #On prevoie de lancer le prochain chiffre a la fin de l'animation:
        anim.bind(on_complete=self.animation_next)
        #Depart de l'animation:
        anim.start(self.chiffre)

    def animation_next(self,animation,widget):#Animation suivante:
        self.compteur_anim-=1
        if self.compteur_anim==0:
            self.remove_widget(self.chiffre)
        else:
            self.chiffre.source=str(self.compteur_anim)+'.png'
            self.animation_start()


# =============================================================================
# Puissance 4
# =============================================================================



# =============================================================================
# 2048
# =============================================================================


# =============================================================================
# Easter Egg
# =============================================================================


class EasterEgg(Screen):
    pass


# =============================================================================
# Calcul Mental
# =============================================================================


class Calcul_Mental(Screen):

    def build(self):
        self.name='Calcul'#On donne un nom a l'ecran C'EST LE NOM QU'ON APPELLE DANS LE .KV
        Calcul = Ecran_du_Jeu()# Typographie très importante !!! ne pas simplifier !!!
        Calcul.build()#Initialisation du Calcul
        self.add_widget(Calcul)#On l'ajoute dans l'ecran


class Ecran_du_Jeu(BoxLayout):

    def build(self):
        a=60
        self.nombre1 = np.random.randint(15,100)
        self.nombre2 = np.random.randint(15,100)
        self.orientation='vertical'
        self.spacing=20
        self.haut()
        self.chiffres()

        Layout3=GridLayout(cols=3,size_hint_y=0.15,spacing=10)
        self.BoutonRetour = Button(text = 'Retour', font_size = 0.3*self.height, text_size = self.size, halign = 'center', valign = 'middle', size_hint=(0.1, 0.1), pos_hint={'right': 0.1})
        self.BoutonRetour.bind(on_press = self.restart)
        self.BoutonRetour.bind(on_press = self.Vers_Menu_Principal)
        Layout3.add_widget(self.BoutonRetour)

        self.BoutonValider = Button(text = 'Valider', font_size = a,size_hint=(0.5,0.15),pos_hint={'right': 0.75},background_color=[0,1,0,1])
        self.BoutonValider.bind(on_press = self.valider)
        Layout3.add_widget(self.BoutonValider)

        self.add_widget(Layout3)

    def Vers_Menu_Principal(self,instance):
        sm.current = '1'
        sm.transition.direction = 'right'

    def haut(self):
        self.score=0
        Layout1=GridLayout(cols=3,size_hint_y=0.2,padding=20)
        scoretext='Score : ' + str(self.score)
        self.scorelabel=Label(text=scoretext,font_size=60, color=[1,0,0,1])
        calcul=str(self.nombre1) + " X " + str(self.nombre2)
        self.calcul=Label(text=calcul,font_size=60, color=[1,0,0,1])
        Layout1.add_widget(self.calcul)
        self.reponse=''
        self.champreponse = TextInput(text=self.reponse,font_size=80)
        Layout1.add_widget(self.champreponse)
        Layout1.add_widget(self.scorelabel)
        self.add_widget(Layout1)

    def chiffres(self):
        a=60
        Layout2=GridLayout(cols=3,size_hint_y=0.5,spacing=10)
        self.Bouton7=Button(text='7', font_size=a)
        self.Bouton7.bind(on_press=self.nombre)
        Layout2.add_widget(self.Bouton7)
        self.Bouton8=Button(text='8', font_size=a)
        self.Bouton8.bind(on_press=self.nombre)
        Layout2.add_widget(self.Bouton8)
        self.Bouton9=Button(text='9', font_size=a)
        self.Bouton9.bind(on_press=self.nombre)
        Layout2.add_widget(self.Bouton9)
        self.Bouton4=Button(text='4', font_size=a)
        self.Bouton4.bind(on_press=self.nombre)
        Layout2.add_widget(self.Bouton4)
        self.Bouton5=Button(text='5', font_size=a)
        self.Bouton5.bind(on_press=self.nombre)
        Layout2.add_widget(self.Bouton5)
        self.Bouton6=Button(text='6', font_size=a)
        self.Bouton6.bind(on_press=self.nombre)
        Layout2.add_widget(self.Bouton6)
        self.Bouton1=Button(text='1', font_size=a)
        self.Bouton1.bind(on_press=self.nombre)
        Layout2.add_widget(self.Bouton1)
        self.Bouton2=Button(text='2', font_size=a)
        self.Bouton2.bind(on_press=self.nombre)
        Layout2.add_widget(self.Bouton2)
        self.Bouton3=Button(text='3', font_size=a)
        self.Bouton3.bind(on_press=self.nombre)
        Layout2.add_widget(self.Bouton3)
        self.BoutonSupress=Button(text='Effacer', background_color=[1,0,0,1], font_size=a)
        self.BoutonSupress.bind(on_press=self.supress)
        Layout2.add_widget(self.BoutonSupress)
        self.Bouton0=Button(text='0', font_size=a)
        self.Bouton0.bind(on_press=self.nombre)
        Layout2.add_widget(self.Bouton0)
        self.BoutonRestart=Button(text='Restart', font_size=a, background_color=[1,0,0,1])
        self.BoutonRestart.bind(on_press=self.restart)
        Layout2.add_widget(self.BoutonRestart)
        self.add_widget(Layout2)

    def restart(self,instance):
        self.score=0
        self.scorelabel.text='Score : ' + str(self.score)
        self.reponse=''
        self.champreponse.text=''

    def nombre(self,instance):
        self.reponse+=instance.text
        self.champreponse.text=self.reponse

    def supress(self,instance):
        self.reponse=''
        self.champreponse.text=''

    def next(self):
        self.nombre1 = np.random.randint(15,100)
        self.nombre2 = np.random.randint(15,100)
        self.champreponse.text=''
        self.calcul.text = str(self.nombre1) + ' X ' + str(self.nombre2)

    def valider(self,instance):
        reponse=self.champreponse.text
        self.reponse=''
        if reponse==str(self.nombre1*self.nombre2):
            self.score=self.score+1
            self.score_restant = 5 - self.score
            content = Label(text='Bien joué, encore ' + str(self.score_restant) + '\n calculs', text_size = self.size, halign = 'center', valign = 'middle')
            popup = Popup(title='+ 1 point !',content=content, size_hint=(0.6,0.6), auto_dismiss=True)
            popup.open()
            self.scorelabel.text='Score : ' + str(self.score)
            self.next()
            if self.score == 5:
                self.Vers_Avion()
        else:
            self.score_restant = 5 - self.score
            contentnon = Label(text='Raté, il te reste ' + str(self.score_restant) + ' calculs\n si tu veux mériter les \n Easter Eggs ...', font_size=0.05*self.height, text_size = self.size, halign = 'center', valign = 'middle')
            popupnon = Popup(title='+ 0 point !',content=contentnon, size_hint=(0.6, 0.6), size=self.size, auto_dismiss=True)
            contentnon.bind(on_press=popupnon.dismiss)
            popupnon.open()
            self.next()

    def Vers_Avion(self): # ET ON REMET LE SCORE À 0
        self.score=0
        self.scorelabel.text='Score : ' + str(self.score)
        self.reponse=''
        self.champreponse.text=''
        sm.current = 'Avion'
        sm.transition.direction = 'left'


# =============================================================================
# Avion
# =============================================================================


class Avion(Screen):

    def press(self):
        self.avion = self.ids.avion.text
        if is_number(self.avion):
            if eval(self.avion) == 0.5:
                self.Vers_EE()

    def Vers_EE(self):
        sm.current = 'EE'
        sm.transition.direction = 'left'


# =============================================================================
# =============================================================================
# # On crée l'application
# =============================================================================
# =============================================================================


sm = ScreenManager()

"""On crée le sm dans tout le code pour que les classes
en bénéficient toutes, pas de jalouse """


class AndroidApp(App):

    def build(self):
        """En important un .kv, il faut definir les écrans du sm dans le build
        pour que le programme le lise après avoir lu le .kv"""
        """moins compliqué de créer le sm dans le .py plutôt que dans le .kv"""
#        sm.current = '1'
# Si on veut changer la transition: très compliqué pour pas grand chose
# sm = ScreenManager(transition=WipeTransition())
        # On ajoute chaque écran dans le (BD)SM
        sm.add_widget(MenuPrincipal(name='1'))
        sm.add_widget(MenuSelectionMH(name='2'))
        sm.add_widget(MenuSelection3des(name='3'))
        sm.add_widget(MenuSelection4des(name='4'))
        sm.add_widget(Lancer3DesTuto(name='5'))
        sm.add_widget(Lancer4DesTuto(name='6'))
        sm.add_widget(portes3(name='7'))
        sm.add_widget(AideMH(name='8'))
        sm.add_widget(Aide3Des(name='9'))
        sm.add_widget(Aide4Des(name='10'))
        sm.add_widget(Simul4D(name='11'))
        sm.add_widget(Simul3D(name='12'))
        sm.add_widget(SimulMH(name='13'))
        sm.add_widget(Credits(name='14'))

# Easter Egg

        sm.add_widget(EasterEgg(name='EE'))
        sm.add_widget(Avion(name='Avion'))

# Pong créé en kv

        sm.add_widget(Pong(name='Pong'))

# Lapins créé en py

        Menu_Lapins = MenuScreen()  # Creation de l'ecran 'Menu_Lapins' DOIT ETRE LE MEME NOM QUE L'ÉCRAN
        Menu_Lapins.build()  # Construction de l'ecran 'Menu_Lapins'
        sm.add_widget(Menu_Lapins)# Le nom de l'écran est Menu_Lapins, def dans la class

# Puissance 4


# 2048


# Calcul Mental

        Calcul=Calcul_Mental()
        Calcul.build()
        sm.add_widget(Calcul)

        return sm


# =============================================================================
# =============================================================================
# # On lance l'application ! !
# =============================================================================
# =============================================================================


if __name__ == '__main__':
    AndroidApp().run()
