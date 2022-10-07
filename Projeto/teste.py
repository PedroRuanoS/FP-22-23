
def limpa_text(jose):
    return ' '.join(jose.split())


cu = '''           Computers are incredibly \n\tfast, \n\t\taccurate
 \n\t\t\tand stupid. \n Human beings  \f            are incredibly slow 
inaccurate, and\v           brilliant. \n Together they are         powerful 
beyond imagination.         '''

joana = ' Fundamentos\n\tda Programacao\n'

print(limpa_text(cu))

a = ['o', 'jose', 'mal']

a.insert(2, 'cheira')

#print(a)

a = ['cu','assado','com','mel']

for i in a:
    i.split()
    i.append(' ')
    print(i)



