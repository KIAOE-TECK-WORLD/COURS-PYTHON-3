import math

Fruits = {
    'Orange': {
        'variete': 'Orange Bleue',
        'quantite': 1000,
        'provenance': 'Haiti'
    },
    'Banane': {
        'variete': 'Banane Plantin',
        'quantite': 5000,
        'provenance': 'Cote Ivoire'
    },
    'Raisins': {
        'variete': 'Raisin vert',
        'quantite': 200,
        'provenance': 'France'
    }
}


if __name__ == '__main__':
    surface = math.pi * math.pow(float(input('Entrez votre rayon: ')), 2)
