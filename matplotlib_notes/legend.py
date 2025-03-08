
'''
To make put the legend outside and below the figure, use the following code
'''

gain_weight = pd.read_csv(....)

fs = 15
fig_gain, ax_gain = plt.subplots(figsize = (12, 8))
ax_gain.plot(gain_weight['AGE_qrts'], gain_weight['gamma'], label = 'label 1')

ax_gain.set_ylabel('Gain', fontsize = fs)
ax_gain.set_xlabel('Age (qrts)', fontsize = fs)
ax_gain.tick_params(axis = 'x', labelsize = fs)
ax_gain.tick_params(axis = 'y', labelsize = fs)

# Shrink the height of chart so I can put legend at the bottom.
# Shrink current axis's height by 10% on the bottom
box = ax_gain.get_position()
ax_gain.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

# bbox_to_anchor = (xaxis, yaxis) determins the position of legend. 
# ncol: number of columns that the legend has. If there are three labels, then set ncol = 3
# frameon = True: Add border to legend box.
ax_gain.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), fancybox=True, shadow=False, ncol=3, fontsize = 15, frameon = True)

fig_gain.savefig(os.path.join(fig_dir, 'example_gain.png'))
plt.close(fig_gain)
