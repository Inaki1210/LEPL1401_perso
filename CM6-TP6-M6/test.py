import assistant as assist

def tests():
    """
    Effectue des tests sur les fonctions du fichier assistant.py , importé comme assist

    Args:
        //
    
    Returns:
        Des messages d'erreurs en fonction des asserts qui sont trigger.
        Permet de trouver des bugs dans le code
    """
    assert assist.file("")
    assert assist.file("all-words.dat")
    assert assist.file("zezv.dat")

    assert assist.info()

    assert assist.words()

    assert assist.search("zezefze")

    assert assist.sum([23,25,465,235345])
    assert assist.sum(['ZEFZ','zfz',24,-325])

    assert assist.avg([144,2352,5,3])

    assert assist.exit()

    assert assist.help()

tests()