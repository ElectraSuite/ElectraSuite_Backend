from handlers.handler_functions import *

map_ = {
    "phasorplot": {
        "function": handle_phasor_plot,
        "description": "This function is designed to plot a phasor-diagram with angles in degrees for up to 12 phasor "
                       "sets (more may be used if additional colors are set). Phasors must be passed as a complex "
                       "number set, (e.g. [ m+ja, m+ja, m+ja, … , m+ja ] )"
    },
    "delta_wye_converter": {
        "function": dynetz_handler,
        "description": "This function is designed to act as the conversion utility to transform delta-connected impedance values to wye- connected and vice-versa."
    },
    
    "circle_diagram": {
        "function": induction_motor_circle_handler,
        "description": "This function is used to generate the induction motor circle diagram. It can also find torque line, desired output power-point, etc."
    }
}