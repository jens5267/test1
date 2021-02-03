import matplotlib.pyplot as plt
import openpyxl





def get_distances():
    locations = {
        'F_LPA': 0,
        'F_G1': 1.802,
        'F_G2': 4.014,
        'F_MS1': 1.525,
        'F_MS2': 4.819,
        'F_LPB': 6.442,
    }
    return locations

def plot_forces():
    locations = get_distances()
    forces = {
        'F_G1': -738.74,
        'F_G2' : -832.1,
        'F_LPA' : 845.66,
        'F_LPB' : 725.19,
        'F_MS1' : -0.09,
        'F_MS2' : 0.09,
    }
    positions = [(value, forces[key]) for key, value in locations.items()]
    # plt.plot(positions)
    # beam = [positions[0][0], positions[-1][0]], [0, 0]
    # print(beam)
    plt.plot([positions[0][0], positions[-1][0]], [0, 0])

    for index, (distance, force) in enumerate(positions):
        # print(distance, force)
        plt.arrow(distance, 0, 0, force, fc="k", ec="k", head_width=0.1, head_length=50, label=f'Force {index}')


    plt.legend()
    plt.xlabel("Position [m]")
    plt.ylabel("Force [kN]")
    plt.title("Free Body Diagram")
    plt.show()

# plot_forces()
def read_excel(filename):
    wb_obj = openpyxl.load_workbook(filename, data_only=True)
    # sheet = wb_obj.active
    sheet = wb_obj['Section Moduli']

    for row in sheet:
        for cell in row:
            print(cell.value)

# read_excel('./../Rigging/Rigging Concept.xlsx')