import numpy as np
import matplotlib.pyplot as plt

# *******************************************************************************************************
# SIMULATION WITH NO EQUIPMENT ERROR
# *******************************************************************************************************

# List to store percent errors for different values of s
perror = {
    10: [],
    50: [],
    100: [],
    500: [],
    1000: [],
    5000: [], 
    10000:  []
}


# Sizes to run simulations for
sizes = [10, 50, 100, 500, 1000, 5000, 10000]

# Run simulations for each size s
for s in sizes:
    print(f"\nRunning simulations for s = {s}...")

    # Run the simulation 1000 times for each s
    for run in range(1000):  

        # Always simulate the presence of an eavesdropper
        t1 = "Y"
        print(f"Simulating test in presence of an eavesdropper... (Run {run + 1}/1000)")

        # Create the random bases and bits for A, B, and E based on the size of test bits desired
        Abasis = np.random.choice(['x', '+'], size=s)
        Abits = np.random.choice([0, 1], size=s)
        Ebasis = np.random.choice(['x', '+'], size=s)
        Bbasis = np.random.choice(['x', '+'], size=s)

        # Setting polarization of A
        Apolar = []
        for i, j in zip(Abasis, Abits):
            if i == 'x' and j == 0:
                Apolar.append(-45)
            elif i == 'x' and j == 1:
                Apolar.append(45)
            elif i == '+' and j == 0:
                Apolar.append(0)
            elif i == '+' and j == 1:
                Apolar.append(90)
        
        # Setting polarization of E receiving from A
        Epolar = []
        for i in Ebasis:
            if i == 'x':
                Epolar.append(45)
            elif i == '+':
                Epolar.append(0)

        # Setting polarization of B
        Bpolar = []
        for i in Bbasis:
            if i == 'x':
                Bpolar.append(45)
            elif i == '+':
                Bpolar.append(0)

        # Receiving bits A --> E
        AErec = []
        for i, j in zip(Apolar, Epolar):
            if i == -45 and j == 0:
                AErec.append(0)
            elif i == 0 and j == 0:
                AErec.append(0)
            elif i == 45 and j == 0: 
                AErec.append(1)
            elif i == 90 and j == 0:
                AErec.append(1)
            elif i == -45 and j == 45:
                AErec.append(0)
            elif i == 0 and j == 45:
                AErec.append(1)
            elif i == 45 and j == 45:
                AErec.append(1)
            elif i == 90 and j == 45:
                AErec.append(0)

        # Setting polarization of E sending to B
        Epolar2 = []
        for i, j in zip(Ebasis, AErec):
            if i == 'x' and j == 0:
                Epolar2.append(-45)
            elif i == 'x' and j == 1:
                Epolar2.append(45)
            elif i == '+' and j == 0:
                Epolar2.append(0)
            elif i == '+' and j == 1:
                Epolar2.append(90)

        # Receiving bits E --> B
        EBrec = []
        for i, j in zip(Epolar2, Bpolar):
            if i == -45 and j == 0:
                EBrec.append(0)
            elif i == 0 and j == 0:
                EBrec.append(0)
            elif i == 45 and j == 0: 
                EBrec.append(1)
            elif i == 90 and j == 0:
                EBrec.append(1)
            elif i == -45 and j == 45:
                EBrec.append(0)
            elif i == 0 and j == 45:
                EBrec.append(1)
            elif i == 45 and j == 45:
                EBrec.append(1)
            elif i == 90 and j == 45:
                EBrec.append(0)

        # Generate keys for A and B -- bases must match and bits must match
        Akey2 = []
        for i in range(len(Abasis)):
            if Abasis[i] == Bbasis[i]:  
                Akey2.append(Abits[i])

        Bkey2 = []
        for i in range(len(Abasis)):
            if Abasis[i] == Bbasis[i]:  
                Bkey2.append(EBrec[i])

        # Check to see how many bits match between A and B -- will be discrepancy due to Eve
        accuracy = []
        for i in range(len(Akey2)):
            if Akey2[i] == Bkey2[i]:
                accuracy.append(Akey2[i])
        
        # Calculate the percent error in the key due to Eve
        per = (len(Akey2) - len(accuracy))/len(Akey2)*100


        # Append the result for this simulation and size s
        perror[s].append(per)

sz = 1000

# Average error for each test bit size per 100 simulations
avgerror = {s: np.mean(perror[s]) for s in sizes}


# Standard deviation of each test bit size
std = {s: np.std(perror[s]) for s in sizes}


# Standard error of the mean for each test bit size
sem = {s: std[s]/np.sqrt(sz) for s in sizes}


# Standard error of the mean around 25%
std10 = np.sqrt(((avgerror[10] - 25)**2)/sz)
std50 = np.sqrt((avgerror[50] - 25)**2/sz)
std100 = np.sqrt((avgerror[100] - 25)**2/sz)
std500 = np.sqrt((avgerror[500] - 25)**2/sz)
std1000 = np.sqrt((avgerror[1000] - 25)**2/sz)
std5000 = np.sqrt((avgerror[5000] - 25)**2/sz)
std10000 = np.sqrt((avgerror[10000] - 25)**2/sz)


# *******************************************************************************************************
# SIMULATION WITH EQUIPMENT ERROR
# *******************************************************************************************************

# List to store percent errors for different values of s
perror1 = {
    10: [],
    50: [],
    100: [],
    500: [],
    1000: [],
    5000: [], 
    10000:  []
}

# Sizes to run simulations for
sizes1 = [10, 50, 100, 500, 1000, 5000, 10000]

# Run simulations for each size s
for s in sizes1:
    print(f"\nRunning simulations for s = {s}...")

    # Run the simulation 1000 times for each s
    for run in range(1000):  

        # Always simulate the presence of an eavesdropper
        t1 = "Y"
        print(f"Simulating test in presence of an eavesdropper... (Run {run + 1}/1000)")

        # Create the random bases and bits for A, B, and E based on the size of test bits desired
        Abasis = np.random.choice(['x', '+'], size=s)
        Abits = np.random.choice([0, 1], size=s)
        Ebasis = np.random.choice(['x', '+'], size=s)
        Bbasis = np.random.choice(['x', '+'], size=s)

        # Setting polarization of A
        Apolar = []
        for i, j in zip(Abasis, Abits):
            if i == 'x' and j == 0:
                Apolar.append(-45)
            elif i == 'x' and j == 1:
                Apolar.append(45)
            elif i == '+' and j == 0:
                Apolar.append(0)
            elif i == '+' and j == 1:
                Apolar.append(90)
        
        # Setting polarization of E receiving from A
        Epolar = []
        for i in Ebasis:
            if i == 'x':
                Epolar.append(45)
            elif i == '+':
                Epolar.append(0)

        # Setting polarization of B
        Bpolar = []
        for i in Bbasis:
            if i == 'x':
                Bpolar.append(45)
            elif i == '+':
                Bpolar.append(0)

        # Receiving bits A --> E
        AErec = []
        for i, j in zip(Apolar, Epolar):
            if i == -45 and j == 0:
                AErec.append(0)
            elif i == 0 and j == 0:
                AErec.append(0)
            elif i == 45 and j == 0: 
                AErec.append(1)
            elif i == 90 and j == 0:
                AErec.append(1)
            elif i == -45 and j == 45:
                AErec.append(0)
            elif i == 0 and j == 45:
                AErec.append(1)
            elif i == 45 and j == 45:
                AErec.append(1)
            elif i == 90 and j == 45:
                AErec.append(0)

        # Setting polarization of E sending to B
        Epolar2 = []
        for i, j in zip(Ebasis, AErec):
            if i == 'x' and j == 0:
                Epolar2.append(-45)
            elif i == 'x' and j == 1:
                Epolar2.append(45)
            elif i == '+' and j == 0:
                Epolar2.append(0)
            elif i == '+' and j == 1:
                Epolar2.append(90)

        # Receiving bits E --> B
        EBrec = []
        for i, j in zip(Epolar2, Bpolar):
            if i == -45 and j == 0:
                EBrec.append(0)
            elif i == 0 and j == 0:
                EBrec.append(0)
            elif i == 45 and j == 0: 
                EBrec.append(1)
            elif i == 90 and j == 0:
                EBrec.append(1)
            elif i == -45 and j == 45:
                EBrec.append(0)
            elif i == 0 and j == 45:
                EBrec.append(1)
            elif i == 45 and j == 45:
                EBrec.append(1)
            elif i == 90 and j == 45:
                EBrec.append(0)

        # Generate keys for A and B -- bases must match and bits must match
        Akey2 = []
        for i in range(len(Abasis)):
            if Abasis[i] == Bbasis[i]:  
                Akey2.append(Abits[i])

        Bkey2 = []
        for i in range(len(Abasis)):
            if Abasis[i] == Bbasis[i]:  
                Bkey2.append(EBrec[i])

        # Check to see how many bits match between A and B -- will be discrepancy due to Eve
        accuracy = []
        for i in range(len(Akey2)):
            if Akey2[i] == Bkey2[i]:
                accuracy.append(Akey2[i])
        
        # Calculate the percent error in the key due to Eve
        per = (len(Akey2) - len(accuracy))/len(Akey2)*100


        # Append the result for this simulation and size s
        perror1[s].append(per)

sz = 1000

# Average error for each test bit size per 1000 simulations
avgerror1 = {s: np.mean(perror1[s]) for s in sizes1}


# Standard deviation of each test bit size
std1 = {s: np.std(perror1[s]) for s in sizes1}


# Standard error of the mean for each test bit size
sem1 = {s: std1[s]/np.sqrt(sz) for s in sizes1}


# Standard error of the mean around 25%
std101 = np.sqrt(((avgerror1[10] - 25)**2)/sz)
std501 = np.sqrt((avgerror1[50] - 25)**2/sz)
std1001 = np.sqrt((avgerror1[100] - 25)**2/sz)
std5001 = np.sqrt((avgerror1[500] - 25)**2/sz)
std10001 = np.sqrt((avgerror1[1000] - 25)**2/sz)
std50001 = np.sqrt((avgerror1[5000] - 25)**2/sz)
std100001 = np.sqrt((avgerror1[10000] - 25)**2/sz)


# Plot of STDEV for each s
plt.figure(figsize=(12, 8))
plt.scatter(1, std[10], marker='o', facecolor='k')
plt.scatter(2, std[50], marker='o', facecolor='k')
plt.scatter(3, std[100], marker='o', facecolor='k')
plt.scatter(4, std[500], marker='o', facecolor='k')
plt.scatter(5, std[1000], marker='o', facecolor='k')
plt.scatter(6, std[5000], marker='o', facecolor='k')
plt.scatter(7, std[10000], marker='o', facecolor='k')
plt.scatter(1, std1[10], marker='s', edgecolor='r', facecolors='none')
plt.scatter(2, std1[50], marker='s', edgecolor='r', facecolors='none')
plt.scatter(3, std1[100], marker='s', edgecolor='r', facecolors='none')
plt.scatter(4, std1[500], marker='s', edgecolor='r', facecolors='none')
plt.scatter(5, std1[1000], marker='s', edgecolor='r', facecolors='none')
plt.scatter(6, std1[5000], marker='s', edgecolor='r', facecolors='none')
plt.scatter(7, std1[10000], marker='s', edgecolor='r', facecolors='none')
plt.title("Standard Deviation in Key Generation with Eavesdropper for Various Test Bits Sizes")
plt.xlabel("Size of Test Bit")
plt.ylabel("Percent Error (%)")
# plt.xscale('log')
# plt.yscale('log')
tickloc = [1,2,3,4,5,6,7]
ticklabels = ["10", "50", "100", "500", "1000", "5000", "10000"]
plt.xticks(tickloc, ticklabels)
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='k', markerfacecolor='k', markersize=10, label="Without Equipment Error"),  
    plt.Line2D([0], [0], marker='s', color='r', markerfacecolor='none', markersize=10, label="With Equipment Error") 
]
plt.legend(handles=legend_elements, title="Simulation Type")
plt.grid(True)
plt.show()


# Plot of SEM for each s
plt.figure(figsize=(12, 8))
plt.scatter(1, sem[10], marker='o', facecolor='k')
plt.scatter(2, sem[50], marker='o', facecolor='k')
plt.scatter(3, sem[100], marker='o', facecolor='k')
plt.scatter(4, sem[500], marker='o', facecolor='k')
plt.scatter(5, sem[1000], marker='o', facecolor='k')
plt.scatter(6, sem[5000], marker='o', facecolor='k')
plt.scatter(7, sem[10000], marker='o', facecolor='k')
plt.scatter(1, sem1[10], marker='s', edgecolor='r', facecolors='none')
plt.scatter(2, sem1[50], marker='s', edgecolor='r', facecolors='none')
plt.scatter(3, sem1[100], marker='s', edgecolor='r', facecolors='none')
plt.scatter(4, sem1[500], marker='s', edgecolor='r', facecolors='none')
plt.scatter(5, sem1[1000], marker='s', edgecolor='r', facecolors='none')
plt.scatter(6, sem1[5000], marker='s', edgecolor='r', facecolors='none')
plt.scatter(7, sem1[10000], marker='s', edgecolor='r', facecolors='none')
plt.title("Standard Error of Mean in Key Generation with Eavesdropper for Various Test Bits Sizes")
plt.xlabel("Size of Test Bit")
plt.ylabel("Percent Error (%)")
# plt.xscale('log')
# plt.yscale('log')
tickloc = [1,2,3,4,5,6,7]
ticklabels = ["10", "50", "100", "500", "1000", "5000", "10000"]
plt.xticks(tickloc, ticklabels)
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='k', markerfacecolor='k', markersize=10, label="Without Equipment Error"),  
    plt.Line2D([0], [0], marker='s', color='r', markerfacecolor='none', markersize=10, label="With Equipment Error") 
]
plt.legend(handles=legend_elements, title="Simulation Type")
plt.grid(True)
plt.show()

