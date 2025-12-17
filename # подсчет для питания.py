nachalo = input('+ - для начала: ')
f = False
if nachalo == '+':
   f = True
# подсчет для питания
while f == True:
   ves = float(input('Напиши свой вес: '))
   procent_jira = int(input('Напиши свой процент жира: ')) * 0.01
   cuh_ves = ves * (1 - procent_jira)
   kall = ves * 30 * (1 - procent_jira)
   print(kall)
   a1 = input('Продолжим?+ или -: ')
   if a1 == '-':
      print('Конец')
      break
   elif a1 == '+':
      cell = input('Ваша цель? 1масса, 2поддержка, 3сушка: ')
      if cell == '1' or cell == 'масса':
         n1 = int(input('Cколько попыток повышения веса?(если в течении недели вес не повысился - + 1 к попытке): '))
         kall = kall + 100 * (n1 - 1)
         belok = 1.5 * cuh_ves
         belok_kall = belok * 4
         jir = 1 * cuh_ves
         jir_kall = jir * 9
         ugli = (kall - (jir_kall + belok_kall)) / 4
         print('калорий -', kall)
         print('белка -', belok)
         print('жира -', jir)
         print('углевода -', ugli)
         a2 = input('Продолжим? + или -: ') 
         if a2 == '-':
               print('Конец')
               break
      elif cell == '3' or cell == 'сушка':
         n1 = int(input('Cколько попыток понижения веса?(если в течении недели вес не понизился - + 1 к попытке): '))
         kall = kall - 100 * (n1 - 1)
         belok = 2.2 * cuh_ves
         belok_kall = belok * 4
         jir = 0.9 * cuh_ves
         jir_kall = jir * 9
         ugli = (kall - (jir_kall + belok_kall)) / 4
         print('калорий -', kall)
         print('белка -', belok)
         print('жира -', jir)
         print('углевода -', ugli)
         a2 = input('Продолжим? + или -: ') 
         if a2 == '-':
               print('Конец')
               break
      elif cell == '2' or cell == 'поддержка':
         belok = 1.2 * cuh_ves
         belok_kall = belok * 4
         jir = 1 * cuh_ves
         jir_kall = jir * 9
         ugli = (kall - (jir_kall + belok_kall)) / 4
         print('калорий -', kall)
         print('белка -', belok)
         print('жира -', jir)
         print('углевода -', ugli)
         a2 = input('Продолжим? + или -: ') 
         if a2 == '-':
               print('Конец')
               break
      else:
          print('повтори запрос')
          a2 = input('Продолжим? + или -: ') 
          if a2 == '-':
               print('Конец')
               break
   else:
       print('повторите запрос')
else:
   print('Приходи позже')



