# import printing_functions as pf
from printing_functions import show_complete_models as scm
from printing_functions import print_models as pm
# from printing_functions import *

unprinted_models = ['A', 'B', 'C', 'D', 'E', 'F']
completed_models = []  
pm(unprinted_models[:], completed_models)
scm(completed_models)

print(unprinted_models)