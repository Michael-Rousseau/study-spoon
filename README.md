# Encodage de Huffman

Huffman-NSI est une bibliothèque python permettant l'encodage et le décodage de texte ASCII avec la méthode de Huffman. C'est un projet développé dans le cadre d'un DM de spé NSI.


## Build
Ce projet est configuré avec Spyder


## Usage

### Avec la ligne de commande
 > Pour encoder un fichier texte
```
(fichier a encoder à glisser dans __encode__.py)
Usage: python3 ./Huffman/__encode__.py

```

> Pour décoder un fichier texte
'''
glisser la table d'occurence dans __decode__.py ainsi que le fichier à décoder
Usage: python3 ./Huffman/__decode__.py
'''

### Avec le module python
Si vous voulez utilisez ceci directement dans votre code python,
vous pouvez utiliser le module Huffman-NSI:

```python
import pytest
import pykeepass

from HuffmanNSI.huffman import encoder, decoder

text = "Mon texte a coder, seulement en ascii!"

encoder(text, "data.pickle", "encoder.bin")
decoder("data.pickle", "encoder.bin")
# la fonction decoder enregistre le texte décodé dans le fichier
# Fichier_decode.txt
```
