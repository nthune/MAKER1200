import matplotlib.pyplot as plt
import csv

def get_data_from_csv(inputFil):
    with open(inputFil, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        lapArray = []
        for i in range(len(data)):
            lapNumber = data[i][0]
            lapTime = int(data[i][1])
            lapArray.append(tuple((lapNumber, lapTime)))
        return lapArray


def selection_sort(array):
    array_sorted = []
    while array:
        max = array[0]
        for lap, time in array:
            if time > max[1]:
                max = (lap, time)

        array_sorted.append(max)
        array.remove(max)
    return array_sorted


def plot_array(array):
    x_val = [x[0] for x in array]
    y_val = [x[1] for x in array]
    plt.plot(x_val,y_val)
    plt.title('Plot over laptimes i race')
    plt.xlabel('Lap nummer')
    plt.ylabel('Laptime i sekunder')
    plt.show()


def main():
    tmpInput = input("\nOnsker du aa registrere nytt race manuelt? ja/nei\n(skriv nei for aa hente fra .csv fil)\n").lower()

    if tmpInput == "ja":
        lapsOverview = []
        antLaps = int(input("\nHvor mange laps vil du registrere?\n"))
        for i in range(antLaps):
            tmpString = "Lap " + str(i+1)
            tmpString2 = "Hva ble tiden paa " + tmpString + " i sekunder?\n"
            tidLap = int(input(tmpString2))
            lapsOverview.append(tuple((tmpString, tidLap)))
        plot_array(lapsOverview)
        sorted_array = selection_sort(lapsOverview)
        fastest_lap = sorted_array[-1]
        print("Din raskeste lap var " + fastest_lap[0] + " og tiden var " + str(fastest_lap[1]) + " sekunder")

    else:
        #laptimes = [("Lap 1", 128), ("Lap 2", 134), ("Lap 3", 129), ("Lap 4", 125), ("Lap 5", 136)]
        inputFil = input("\nHva er navn paa .csv fil? \n(Skriv eksempelvis: dataset.csv)\n")
        laptimes = get_data_from_csv(inputFil)
        plot_array(laptimes)
        sorted_array = selection_sort(laptimes)
        fastest_lap = sorted_array[-1]
        print("Din raskeste lap var " + fastest_lap[0] + " og tiden var " + str(fastest_lap[1]) + " sekunder")

main()
