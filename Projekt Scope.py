import sys
import csv
import pandas
from os import system
import matplotlib.pyplot as plt


df = pandas.read_csv('data.csv', index_col='date') #Smider CSV-filen til pandas dataframe

def parse_csv(*option1): #Definerer Parse CSV-filen
    print(df) 

def data_entries(*option2): #Definerer dataindtastninger for hver kommune
    print(df['location'].value_counts())

def bar_plot(*option3): #Oprettelse af bar-plot
    #Konvetere latency fra string til float for at fjerne ms i data.csv og konventere den til sidst til float funktion 
    def setup_latency(lc):
        lc = ''.join(lc.split())
        lc = lc[:-2]
        return float (lc)

    data_frame = pandas.read_csv('data.csv') #Indlæser csv-filen
    data_frame ['date'] = pandas.to_datetime(data_frame['date']) #Kolonne for måneden
    data_frame['latency'] = data_frame ['latency'].map(setup_latency) #Giver en hver latency værdi ved at køre den igennem funktionen map

    frederiksberg = data_frame.query("location == 'Frederiksberg' ").groupby(data_frame['date'].dt.strftime('%B'))['latency'].mean() #Frederiksbergs data
    herning = data_frame.query("location == 'Herning' ").groupby(data_frame['date'].dt.strftime('%B'))['latency'].mean() #Hernings data

    ax = frederiksberg.plot(kind = 'bar')
    herning.plot(kind='bar', ax = ax, color ='red') #Herning = rød
    plt.show #Funktion til at vise diagrammet

def scatter_plot(*option4):#Oprettelse af scatter plot
    df[['location', 'download']].groupby('location', as_index=False).max().plot.scatter(x='location', y= 'download', alpha = 0.5) #
    plt.show()

print('This program illustrates TDCNETs data entries with data information on different region in Denmark with 2 different graphs. Please consider downloadning data.csv before starting this program'"\n"
"\n" 'Projekt Scope prototype') #Illustration af programmet og titel
print("\n" "\n" "Welcome to this program" "\n" "_-MENU-") #Første Linje: Velkomst, MenuBar
#Oprettelse af de forskelliger muligheder i en list literal function
menu_options= {
    1: 'Parse CSV-filen',
    2: 'Print hvor mange dataindtastninger der er for hver kommune',
    3: 'Opret et Bar Plot der viser den gennemsnitlige månedlige latency for Frederiksberg og Herning',
    4: 'Opret et Scatter Plot af de højeste downloadhastigheder for hver kommune',
    5: 'Tryk Q for at exit programmet'
}
#Definerer funktion og udskrivelse af layout. 
def print_menu():
    for key in menu_options.keys():
        print (key, ':', menu_options[key] )

def option1():
    print(parse_csv('You choosed option 1 \'Parse CSV-filen\'')) #tast 1 for at få parse csv
    
def option2():
    print(data_entries('You choosed option 2 \'Antal af dataindtastninger der er for hver kommune\'')) #tast 2 for at få den gennemsnitlige dataindtastninger for hver kommune

def option3():
    print(bar_plot('You choosed option 3 \'BarPlot for Frederiksberg og Herning\'')) #tast 3 for at få vist barplot

def option4():
    print(scatter_plot('You choosed option 4 \'ScatterPlot af de højeste downloadhastigheder for hver kommune\'')) #tast 4 for at få vist scatter plot

def option5(): #EXIT
    print()


if menu_options: #Decides the execution
    while(True): #(Loop Forever) Programmet fortsætter med at køre igen efter man har indtastet 1-4 eller Q/q for at lukke. 
        print_menu() #Viser de 5 forskellige muligheder
        try: #Executer vores kode hvis man indtaster mellem 1-4 el. Q/q
            option = int(input("\n"'Enter your choice of option: '))
        except: #Executer hvis try exception (Alt andet end tal) er forkert
            print('Incorrect input type. Please enter a number from MENU or Q to exit')
        
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            print('Thank you for your time. Goodbye.') #Indtast 5 for at lukke programmet
            exit()
        else:
            print('The option does not exist. Please enter the following options between 1 and 4 or Q to exit.') #Indtastning af andre symboler, tal eller tegn der ikke er gældende -  ville teksten printes. 


