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
    result = [str(i) for i in dynetz(**dic)]
    return result
    


# Induction Machine circle diagram
def induction_motor_circle_handler(args):
    arr = args[0].split(",")
    open_circuit_test_data = {"V0":float(arr[0]), "I0":float(arr[1]), "W0":float(arr[2])}

    arr2 = args[1].split(",")
    blocked_rotor_test_data = {"Vsc":float(arr2[0]), "Isc":float(arr2[1]), "Wsc":float(arr2[2])}

    visu.InductionMotorCircle(
        no_load_data=open_circuit_test_data,
        blocked_rotor_data=blocked_rotor_test_data,
        output_power=float(args[2]),
        torque_ration=float(args[3]),
        frequency=args[4],
        poles=int(args[5])
    )

    return "Induction Motor Circle Diagram Plotted"
    



if __name__ == "__main__":
    args_phasor = ["68,0", "72,120", "53,-120"]
    handle_phasor_plot(args_phasor)

    args_dynetz = ["3+2j,5+8j,3j", "#"]
    print(dynetz_handler(args_dynetz))


