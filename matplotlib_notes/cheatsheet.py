from matplotlib import pyplot as plt



'''
=========================
Save multiple graphs
=========================
code:

    plt.clf()

clt() will initialize plt. Add this line after savefig(),
so that you don't need to comment all other plt codes

example:

    plt.plot(x_axis, coin_price, c = 'red')
    plt.plot(x_axis, gecko_price, c = 'blue')
    plt.savefig('coin_vs_gecko.png')
    # Initialize matplotlib after plotting.
    # Avoid overlapping
    plt.clf()




###------Subplots------###


# figsize change the size of each subplot
fig, axs = plt.subplots(4,5, figsize = (50,30))         # 4*5 = 20 graphs in one .png
plt.subplots_adjust(wspace = 0.1, hspace = 0.1)

film_names = [i[0] for i in box_list]
box_list = [i[1] for i in box_list]

pic_index = 0
for sub_pic in axs.flatten():
    x = coor_list[pic_index][0]
    y = coor_list[pic_index][1]
    sub_pic.plot([i for i in range(time_period)], box_list[pic_index])
    #sub_pic.title.set_text(film_names[pic_index])
    sub_pic.set_title(film_names[pic_index], font = 'SimHei')       # claim fonts if Chinese letter.
    pic_index += 1

plt.savefig(f'figures/{pic_name}.png')
plt.clf()





'''




