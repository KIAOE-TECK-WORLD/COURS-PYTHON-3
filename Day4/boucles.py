# Boucles
# Les boucles ( for, while )
#
# Syntaxe for:
#   for variable_subtitution in varible_itarable
#   - On pas besoin d'incrément manuel pour passer à l'itération suivante
#   - il est plus simple d'utiliser la boucle
#   - en terme de complexité algorithmique face au while le for est mieux
#
# Syntaxe while:
#   while (condition):
#       -> incrémentation manuelle
#       -> stopper la boucle
#
# La fonction native range permet d'avoir un intervalle
# Exemple: range(10) => 0 à 9 <=> 0 à n-1
# Exemple: range(2, 10) => 2 à 9 <=> 2 à n-1
#   - range(start, final)
#   - range(start=0, final=n)


if __name__ == "__main__":

    for i in range(10): # première instruction
        # deuxième instruction
        print(f'Variable de subtitution={i}')

    print('\n')

    for i in range(2, 10):
        print(f'Variable de subtitution={i}')

    print('\n')

    i = 0 # le start 0 ( premère instruction )
    # deuxième instruction
    while i < 10:
        # troisième instruction
        print(f'Variable de subtitution={i}')
        # quatrième instruction
        i = i + 1

    print('\n')

    i = 2 # le start 2
    while i < 10:
        print(f'Variable de subtitution={i}')
        i = i + 1
