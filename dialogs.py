#1/usr/bin/pyton
#-*- coding: utf-8 -*-
a = input("Cien, liet.,lūdzu, ievadi skaitli")
#3. python'ā visi input rezultāti ir ar str datu tipu
# tāpēc ievadītā lieluma datu tips vēlāk ir jāpārveido
a = int(a)
# python valoda balstās uz C valodas -> print strādā līdzōgi printf
# https://www.cplusplus.com/referemce/cstdio/printf/
print("Liet.,Tu esi ievadījis skaitli: %d"%(a))
aa = a*a
print("Tavs skaitlis kvadrātā ir: %d"%(aa))

