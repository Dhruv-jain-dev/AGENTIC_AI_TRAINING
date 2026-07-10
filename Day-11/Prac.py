# print the count of vehicle, Fasttag, TollQueue constructors & show the count in a new csv file.
file=open(r'C:\Users\hp\OneDrive\Desktop\AGENTIC_AI_TRAINING\Day-10\.py','r')
data= file.readlines()
vehicle=0
toll=0
fasttag=0
file=open('cnt.csv','a')
for line in data:

    if( 'vehicle(' in line):
        vehicle+=1
    if('FastTag(' in line):
        fasttag+=1
    if('TollQueue(' in line):
        toll+=1
file.write(f'Vehicle,{vehicle}\n')
file.write(f'toll,{toll}\n')
file.write(f'tag,{fasttag}\n')