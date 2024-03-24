from electricpy import phasors
from electricpy import visu
from electricpy import dynetz


def handle_phasor_plot(args):
    phasors_ = phasors.phasorlist(args)
    plt = visu.phasorplot(phasors_, legend = True, labels = args)
    plt.show()

def dynetz_handler(args):
    dic = {"delta" : args[0] if not "NA" else None,
           "wye" : args[1] if not "NA" else None}
    return dynetz(**dic)
