# Diverse soluzioni per algoritmi per controllare se un dato anno è bisestile


ANNO = int(input("Inserire anno: "))


def lazy_evaluation(anno):
    bisestile = (anno % 400 == 0) or (anno % 100 == 0) and (anno % 4 == 0)
    return bisestile


def alg_1(anno):
    """if anno % 4 == 0:
        if anno % 100 == 0:
            if anno % 400 == 0:
                Bisestile = True
            else:
                Bisestile = False
        else:
            Bisestile = True
    else:
        Bisestile = False"""
    Bisestile = (anno % 4 == 0) and (anno % 100 == 0) or (anno % 400 == 0)
    return Bisestile


def alg_2(anno):
    """if anno % 100 == 0:
        if anno % 400 == 0:
            Bisestile = True
        else:
            Bisestile = False
    else:
        if anno % 4 == 0:
            Bisestile = True
        else:
            Bisestile = False"""
    Bisestile = (anno % 100 == 0) and (anno % 4 == 0) or (anno % 400 ==0)
    return Bisestile


def alg_3(anno):
    """if anno % 400 == 0:
        Bisestile = True
    elif anno % 100 == 0:
        Bisestile = False
    else:
        Bisestile = anno % 4 == 0"""
    Bisestile = (anno % 400 == 0) or (anno % 100 == 0) and (anno % 4 == 0)
    return Bisestile


def main():
    return


if __name__ == '__main__':
    main()



