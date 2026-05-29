times = ('corinthians', 'palmeiras', 'santos', 'gremio', 'cruzeiro', 'flamengo', 'vasco',
         'chapecoense', 'atletico', 'botafogo', 'atletico-PR', 'bahia', 'sao paulo', 'fluminense',
         'sport recife', 'ec vitoria', 'coritiba', 'avai','ponte preta', 'atletico goianiense')
print(f'lista de times do brasileirão: {times}')
print('---'*50)
print(f'os 5 primeiros times são: {times[0:5]} ')
print('---'*50)
print(f'os ultimos 4 times são: {times[-4:]} ')
print('---'*50)
print(f'times em ordem alfabetica:{sorted(times)}')
print('---'*50)
print(f'o chapeco esta na posiçao: {times.index("chapecoense")+1}ª')

