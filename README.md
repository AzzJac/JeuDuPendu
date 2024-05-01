# Création d’un mini jeu
Règle du jeu :
Le joueur va pouvoir tuer des monstres de niveau 1 et des monstres de niveau 2 avant de mourir, en
ayant perdu tous ses points de vie (le joueur démarre avec 100 points de vie). Chaque monstre de
niveau 1 tué rapporte 1 point, chaque monstre de niveau 2 tué en rapporte 2.
Un monstre aléatoire arrive (de niveau 1 ou de niveau 2), le héros attaque le monstre ; si le monstre
a survécu il attaque à son tour le joueur et ceci jusqu'à ce que le joueur soit mort. On compte au fur
et à mesure le nombre de points rapporté pour chaque monstre tué.
Une attaque d’un joueur sur un monstre consiste à jeter un dé pour les deux protagonistes. Si le dé
du joueur est supérieur ou égal au dé du monstre, alors celui-ci est vaincu. Sinon, rien ne se passe et
c'est au tour du monstre d'attaquer.
L'attaque du monstre de niveau 1 sur le joueur est similaire, à la différence que le jet du monstre doit
être strictement supérieur au jet du joueur. Si le dé du monstre est strictement supérieur au dé du
joueur, alors celui-ci est reçoit les dégâts du monstre. Sinon, rien ne se passe et c'est au tour du
monstre d'attaquer.
Lorsque le joueur reçoit des dégâts, son bouclier se déclenche avec un nouveau jet de dé. Si ce
dernier est inférieur ou égal à 2, alors le joueur ne reçoit pas de dégâts. Dans le cas contraire, ses
points de vie sont diminués de 10 points de vie.
L'attaque du monstre niveau 2 est la même que celle du monstre de niveau 1, sauf qu'il enchaine
avec un sort magique. Un jet de dé est réalisé et si ce jet est égal à 6 alors le héros reçoit des
dommages équivalents aux dégâts du sort magique.
