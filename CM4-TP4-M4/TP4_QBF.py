def positions(s, p):
    # pré : prise d'une chaîne de caractères et d'un motif à identifier. Marche pour tout.
    # post : renvoyer la position du motif dans la chaîne de caractères.
    l = []
    p = p.lower()
    s = s.lower()
    for posp in range(len(p)-1):
        if s[0] == '?':
            ident = True
            for poss in range(1, len(s)):
                if s[poss] == '?':
                    indent = True
                elif p[posp + poss] != s[poss]:
                    ident = False
                    break
            if ident:
                l.append(posp)
        else:
            if p[posp] == s[0]:
                ident = True
                for poss in range(1, len(s)):
                    if s[poss] == '?':
                        indent = True
                    elif p[posp + poss] != s[poss]:
                        ident = False
                        break
                if ident:
                    l.append(posp)
    return l

print(positions("ab","CDEF"))
print(positions("?B","CAbDEF"))
print(positions("A?","CABDEACF"))
print(positions("aa","CAAABDEAAF"))
print(positions("??","CAAAB"))