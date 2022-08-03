import os
import imageio

pics = []
my_pics = os.listdir('pics')
for i in range(len(my_pics)):
    pic = imageio.imread('pics/' + my_pics[i])
    pics.append(pic)
imageio.mimsave('flower.gif', pics)