# dataExtractionExcel
Extraction et traitement des données d'un fichier Excel avec Python - Pandas


Ce programme utilise Python version 3.12.0, les librairies Pandas et Openpyxl ainsi qu'un fichier Excel. Il nécessite donc l'installation de Python version 3.12.0, des librairies Pandas et Openpyxl pour fonctionner. 

Il effectue une extraction des données d'un fichier Excel. Ici, toutes les données sont extraites, mais il est possible de ne choisir que certaines données en ajoutant directement des conditions pour préciser notre choix de données à extraire.
 
Ensuite, ces données sont affichées à l'écran afin de visualiser l'ensemble du contenu du fichier Excel ici nommé "myData.xlsx". 

Puis, un tri conditionnel est appliqué sur les données extraites et le résultat de ce tri est affiché à l'écran. Ces données peuvent par la suite, être copiées dans un nouveau fichier par exemple. Un autre traitement peut aussi être réalisé sur celles-ci.

Enfin, un calcul est effectué sur le résultat des données sur lesquelles un tri conditionnel a été effectué précédemment.

Effectuer directement le tri lors de l'extraction des données serait un choix plus efficace sur un large volume de données, à condition de connaître l'utilisation souhaitée de celles-ci. Cette action est réalisable sur plusieurs fichiers et sur différents types de fichiers avec d'autres librairies Python notamment.  

La capture d'écran "resultDataExtractionExcel.png" montre le résultat d'exécution de ce programme :   
- Un affichage de toutes les données extraites du tableau Excel
- Un affichage des noms des éléments du système solaire et de la composition de leur atmosphère s'ils en ont une
- Un affichage d'un calcul sur les données précédentes : le pourcentage d'éléments du système solaire dont l'atmosphère contient de l'hydrogène parmi ceux qui possèdent une atmosphère


N.B. : L'astronomie n'est pas mon domaine d'expertise, et les découvertes scientifiques apportent régulièrement des précisions et corrections. Ainsi, les données du tableau Excel sont susceptibles de nécessiter des corrections et également des précisions. L'objectif est ici d'avoir un jeu de données utile au programme.   


Pour exécuter le programme, placer tous les fichiers dans un dossier et se placer dans celui-ci dans l'invite de commande, par exemple :
C:\Demo\Python\dataExtractionExcel

Puis entrer cette commande d'exécution :
python dataExtractionExcel.py
