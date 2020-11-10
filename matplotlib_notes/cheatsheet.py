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

'''
