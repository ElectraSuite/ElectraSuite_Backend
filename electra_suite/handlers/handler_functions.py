from electricpy import phasors
from electricpy import visu
from electricpy import dynetz

# Phasor Plot drawing
def handle_phasor_plot(args):
    args = [[float(j) for j in i.split(",")] for i in args]
    phasors_ = phasors.phasorlist(args)
    plt = visu.phasorplot(phasors_, legend = True, labels = args)
    plt.show()

# Delta-Wye converter
def dynetz_handler(args):
    # splitting each argument on basis of ",". "#" is ignored.
    args = [i.split(",") for i in args]
    for i in range(len(args)):
        if args[i][0] == "#":
            args[i] = None
        else:
            arr = args[i]
            args[i] = [complex(i) for i in arr]

    dic = {"delta" : args[0],
           "wye" : args[1],
           "round": 3}
    return str(dynetz(**dic))

if __name__ == "__main__":
    args_phasor = ["68,0", "72,120", "53,-120"]
    handle_phasor_plot(args_phasor)

    args_dynetz = ["3+2j,5+8j,3j", "#"]
    print(dynetz_handler(args_dynetz))

