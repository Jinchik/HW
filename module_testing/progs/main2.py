
from sys import path

path.append('../packages')

from module_testing.packages.extra.good.best import sigma, sigma as sig
from module_testing.packages.extra.good.best.tau import FunT

print(sigma.FunS())
print(FunT())

from module_testing.packages.extra.good import alpha as alp

print(sig.FunS())
print(alp.FunA())


from sys import path

path.append('/module_testing/packages\\Extrapack ZIP file.zip')

import sys

for p in sys.path:
    print(p)


