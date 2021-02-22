def output(tuples):
    print(len(tuples))
    for tuplez in tuples:
        tuplez = [str(len(tuplez))] + tuplez
        print (" ".join(map(str, tuplez)))

output([[1,4],[0,2,3]])