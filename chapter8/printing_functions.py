def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current_design = unprinted_models.pop(0)
        print(f"Printing model: {current_design.title()}")
        completed_models.append(current_design)
        
def show_complete_models(completed_models):
    print("The following models has been printed")
    for model in completed_models:
        print(model)
        
        
unprinted_models = ['A', 'B', 'C', 'D', 'E', 'F']
completed_models = []  
print_models(unprinted_models[:], completed_models)
show_complete_models(completed_models)

print(unprinted_models)