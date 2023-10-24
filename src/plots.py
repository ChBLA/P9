import file_util as fu
import plotting_util as pu
import os
from enum import Enum

def process_sizes(data):
    sizes = data["sizes"]
    path = data["path"]

    def get_current_size(i):
        return sizes[str(i)][version_indeces[i]]
    
    def advance(i):
        version_indeces[i] += 1

    new_sizes = []
    compulsory_sizes = []
    estimated_time = []
    version_indeces = {int(i) : 0 for i in sizes.keys()}
    for step in path:
        size = 0
        flag = False

        if version_indeces[step[0]] == 0:
            advance(step[0])
            size += get_current_size(step[0])
            flag = True 
        if version_indeces[step[1]] == 0:
            advance(step[1])
            size += get_current_size(step[1])
            flag = True  
        if flag:
            estimated_time.append(size)
            compulsory_sizes.append((compulsory_sizes[-1] + size) if len(compulsory_sizes) > 0 else size)

        size = compulsory_sizes[-1] - get_current_size(step[0]) - get_current_size(step[1])
        estimated_time.append(get_current_size(step[0])**2 + get_current_size(step[1])**2)
        advance(step[1])
        compulsory_sizes.append(size + get_current_size(step[1]))
        new_sizes.append(get_current_size(step[1]))

    return compulsory_sizes, estimated_time, new_sizes

def get_nested(ls):
    return [[v] for v in ls]

def plot(folder, plots, save_path = ""):
    files = fu.load_all_json(os.path.join("experiments", folder))
    data = {v : [] for v in list(Variables)}
    for file in files: 
        if True:
            s, estimated_time, new_sizes = process_sizes(file)
            data[Variables.ESTIMATED_TIME].append([sum(estimated_time)])
            data[Variables.SIZES].append(s)
            data[Variables.NEW_SIZES].append(new_sizes)
            data[Variables.STEPS].append(range(len(s)))
            data[Variables.CONTRACTION_STEPS].append(range(len(new_sizes)))
            q = file['circuit_settings']['qubits']
            data[Variables.NAMES].append(f"{file['circuit_settings']['algorithm']}:{q:03d}")
            data[Variables.QUBITS].append([q])
            data[Variables.MAX_SIZES].append([max(s)])
            data[Variables.CONTRACTION_TIME].append([file["contraction_time"]])

    if save_path != "":
        save_path = os.path.normpath(os.path.join(os.path.realpath(__file__), "..", "..", "experiments", save_path))

        if not os.path.exists(save_path):
            os.makedirs(save_path)

    for p in plots:
        full_path = ("" if save_path == "" else os.path.join(save_path, p[3].replace(" ", "_")))
        title = p[3] + " " + files[0]['circuit_settings']['algorithm']
        if p[0] == "line":
            pu.plot_line_series_2d(data[p[1]], data[p[2]], data[Variables.NAMES], 
                                   p[1].value, p[2].value, title=title, 
                                   save_path=full_path, legend=False)
        elif p[0] == "points":
            pu.plotPoints2d(data[p[1]], data[p[2]], p[1].value, p[2].value, 
                            series_labels=data[Variables.NAMES], title= title,
                            marker="o", save_path=full_path, legend=False)

class Variables(Enum):
    SIZES = "Nodes |N|"
    STEPS = "Path Steps s"
    CONTRACTION_STEPS = "Path Contraction Steps s_c"
    QUBITS = "Qubits n"
    MAX_SIZES = "Max Nodes N_max"
    NAMES = "Names"
    ALGORITHM = "Algorithm"
    CONTRACTION_TIME = "Contraction Time t_c"
    ESTIMATED_TIME = "Estimated Time t_e"
    NEW_SIZES = "Newest TDD Size N_new"


if __name__ == "__main__":
 
    plots = [("line", Variables.STEPS, Variables.SIZES, "Compulsory Sizes over Path"),
             ("points", Variables.QUBITS, Variables.MAX_SIZES, "Maximum Size by Qubits"),
             ("points", Variables.MAX_SIZES, Variables.CONTRACTION_TIME, "Time by Maximum Size"),
             ("points", Variables.ESTIMATED_TIME, Variables.CONTRACTION_TIME, "Time by Estimated Time"),
             ("points", Variables.QUBITS, Variables.ESTIMATED_TIME, "Estimated Time by Qubits"),
             ("line", Variables.CONTRACTION_STEPS, Variables.NEW_SIZES, "New Sizes over Path")]
    
    folders = ["first_experiment_2023-10-18", "first_experiment_2023-10-19_10-17", 
               "mapping_experiment_2023-10-19_16-48", "mapping_experiment_2023-10-19_17-08",
               "mapping_experiment_2023-10-19_17-24", "mapping_experiment_2023-10-19_17-27"]

    for i, folder in enumerate(folders):
        plot(folder, plots, os.path.join("plots", folder)) 
        print(f"Plotted: {int((i + 1) / len(folders) * 100)}%")