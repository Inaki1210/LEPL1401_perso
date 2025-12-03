#tests de search.py

import search

def test_get_words():
    assert search.get_words( "Turmoil has engulfed the Galactic Republic." ) == ["turmoil", "has", "engulfed", "the", "galactic", "republic"]
    assert search.get_words("10000 durum je fait ce code seul.") !=["Je","l'ai","fait","seul"] #bon ok, j'ai un peu débogué avec ChatGPT (voir readme)

def test_readfile():
    assert search.readfile('testing.txt') != ["Coucou c'est moi.","It's me, Mario", "Hello, it's me"]
    assert search.readfile('testing1.txt') == [['Rammstein\n'], ['By Rammstein\n'], ['\n'], ['Deutschland 5:23\n'], ['Radio 4:37\n'], ['Zeig Dich 4:15\n'], ['AuslÃ¤nder 3:51\n'], ['Sex 3:56\n'], ['Puppe 4:33\n'], ['Was Ich Liebe 4:29\n'], ['Diamant 2:34\n'], ['Weit Weg 4:20\n'], ['Tattoo 4:11\n'], ['Hallomann 4:11\t']]

def test_create_index():
    assert search.create_index('testing') != {"J'aime" : [0,1,2],"faire":[0],"du" : [7], "yoyo" : [13]}
    assert search.create_index('testing1.txt') == {'by': [0], 'dich': [3], 'ich': [6], 'liebe': [6], 'weg': [8]}

def test_get_lines():
    assert search.get_lines(['jedi','tommy'],search.create_index('testing.txt')) == []
    assert search.get_lines(['jedi','tommy'],search.create_index('testing.txt')) != [289,2424,0]

test_readfile()
test_get_words()
test_create_index()
test_get_lines()