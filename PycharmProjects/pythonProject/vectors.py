def calculate_velocity():
    displacement = int(input("Enter the value of displacement: "))
    time = int(input("Enter the value of time: "))
    velocity = (displacement/time)
    print("The value of velocity is", velocity,"m/s")

def calculate_pressure():
    force = int(input("Enter the value of force: "))
    area = int(input("Enter the value of area: "))
    pressure = (force/area)
    print("The value of pressure is", pressure,"N/m^2")

def calculate_density():
    mass = int(input("Enter the value of mass: "))
    volume = int(input("Enter the value of volume: "))
    density = (mass/volume)
    print("The value of density is", density,"N/m^3")

def calculate_impulse():
    force = int(input("Enter the value of force: "))
    time = int(input("Enter the value of time: "))
    impulse = (force*time)
    print("The value of impulse is", impulse,"N/m^2")

def calculate_energy():
    power = int(input("Enter the value of power: "))
    time = int(input("Enter the value of time: "))
    energy = power*time
    print("The value of energy is", energy,"joules")

hello = int(input("Type 1 to calculate velocity\nType 2 to calculate pressure\nType 3 to calculate density\nType 4 to calculate impulse\nType 5 to calculate energy\n"))
print(hello)


if hello == 1:
    calculate_velocity()
elif hello == 2:
    calculate_pressure()
elif hello == 3:
    calculate_density()
elif hello == 4:
    calculate_impulse()
elif hello == 5:
    calculate_energy()
else:
    print("Invalid input")