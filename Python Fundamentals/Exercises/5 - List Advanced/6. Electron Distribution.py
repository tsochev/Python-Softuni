num_of_electrons = int(input())


electron_shells = []
layer = 1
while num_of_electrons > 0:
    electron_layers = 2 * layer ** 2

    if num_of_electrons >= electron_layers:
        electron_shells.append(electron_layers)
    else:
        electron_shells.append(num_of_electrons)
    num_of_electrons -= electron_layers
    layer += 1
print(electron_shells)