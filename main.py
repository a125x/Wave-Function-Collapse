from typing import List
import random

#notation:
#
#              0001
#             |‾‾‾|
#         1000|   |0010
#             |___|
#              0100
#
def basic_tiles() ->List[List[str]]:
    return [['|‾‾‾|\n|   |\n|___|', '0000'],
            ['|‾‾‾|\n    |\n|___|', '1000'],
            ['|‾‾‾|\n|    \n|___|', '0010'],
            ['|‾ ‾|\n|   |\n|___|', '0001'],
            ['|‾‾‾|\n|   |\n|_ _|', '0100'],
            ['|‾‾‾|\n     \n|___|', '1010'],
            ['|‾ ‾|\n|   |\n|_ _|', '0101'],
            ['|‾ ‾|\n    |\n|_ _|', '1101'],
            ['|‾ ‾|\n|    \n|_ _|', '0111'],
            ['|‾‾‾|\n     \n|_ _|', '1110'],
            ['|‾ ‾|\n     \n|___|', '1011'],
            ['|‾ ‾|\n     \n|_ _|', '1111']]

def start_tiles() -> List[List[str]]:
    return [['']]

def print_tiles(tiles: List[List[str]]) -> None:
    for i in tiles():
        print(i[0])

#works only for amount >= 0
#generate some amount of tiles by repeating the process
#of creating wave function and collapsing it
def generate_tiles(
        amount: int, 
        collapse: List[List[str]], 
        wave: List[List[str]], 
        basic_tiles: List[List[str]],
        current_tiles: List[List[str]]
        ) -> List[List[str]]:
    if amount == 0:
        return current_tiles
    elif amount > 0:
        #print(amount)
        current_tiles = collapse(wave(basic_tiles,
                                      current_tiles))
        return generate_tiles(amount - 1, 
                              collapse, 
                              wave, 
                              basic_tiles, 
                              current_tiles)
    #raising exception. Yes, i don't know how.
    else:
        10/0

def collapse_wave_function(
        variants_of_tiles: List[List[str]]
        ) -> List[List[str]]:
    #should return one single choosen (randomly?) variant
    def choosen_variant():
        return [variants_of_tiles()[random.randint(0, len(variants_of_tiles()) - 1)]] 
    return choosen_variant

def wave_function(
        basic_tiles: List[List[str]],
        current_tiles: List[List[str]]
        ) -> List[List[str]]:
    #for now return input, should return variants
    #print_tiles(basic_tiles)
    return basic_tiles

def main() -> None:
    print_tiles(
            generate_tiles(10, 
                           collapse_wave_function,
                           wave_function, 
                           basic_tiles, 
                           start_tiles)
          )

if __name__ == '__main__':
    main()
