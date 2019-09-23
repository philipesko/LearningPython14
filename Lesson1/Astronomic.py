import ephem
from datetime import datetime

# mars = ephem.Mars('2000/01/01')
# cons = ephem.constellation(mars)
# print(cons)
#
# venera = ephem.Jupiter(datetime.now())
# const = ephem.constellation(venera)
# print(const)

attr_name = 'Mars'
planet = getattr(ephem, attr_name)(datetime.now())
cons = ephem.constellation(planet)
print(cons)
