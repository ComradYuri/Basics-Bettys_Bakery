import numpy as np

cupcakes = np.array([2, 0.75, 2, 1, 0.5])
print('cupcakes\n', cupcakes)

recipes = np.genfromtxt('recipes.csv', delimiter=',')

# columns: Cups of Flour, Cups of sugar, Eggs, Cups of milk, Cups of butter
# rows: Cupcakes, Pancake, Cookie, Bread
print('recipes\n', recipes)

eggs = recipes[:, 2]
print('eggs required per recipe\n', eggs)

print('recipes that require one egg\n', eggs == 1)

cookies = recipes[2, :]
print('requirements for cookie recipe\n', cookies)

double_batch = cupcakes * 2
print('double pancake batch requirements\n', double_batch)

grocery_list = cookies + double_batch
print('grocery list for cookie and two pancakes\n', grocery_list)
