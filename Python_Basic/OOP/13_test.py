import reflection_target_module

if hasattr(reflection_target_module,'obj'):
#     print('yes')
    a = getattr(reflection_target_module,'obj')
    print(a.name)
    """return: Simon"""

# print(reflection_target_module.__name__)