#%%
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches

def extract_mat(mat):
	rects = []
	for m in mat['boxes'][0]:
		rect = np.zeros((4, 2))
		i = 0
		for i in range(0, 4):
			rect[i] =  m[0][0][i]
		rects.append (rect)
	return rects

#%%
# convert_to_rect(a)
def convert_to_rect(hand):
	row = np.min(hand[:,1])
	col = np.min(hand[:,0])
	h = np.max(hand[:,1]) - row
	w = np.max(hand[:,0]) - col
	return row, col, h, w

#%%
def draw_rects(mat):
	url = mat.replace('annotations', 'images').replace('.mat', '.jpg')
	rects = extract_mat(scipy.io.loadmat(mat))

	img=mpimg.imread(url)
	fig,ax = plt.subplots(1)
	plt.imshow(img)
	for rect in rects:
		row, col, h, w = convert_to_rect(rect)
		rect = patches.Rectangle((row, col),h,w,linewidth=1,edgecolor='r',facecolor='none')
		ax.add_patch(rect)
	plt.show()

#%%

g = open('/Users/rizkyario/Downloads/darknet-hand/data/hand_dataset/training_mat_all.txt')
# g = open('/Users/rizkyario/Downloads/darknet-hand/data/hand_dataset/training_mat.txt')
data = g.readlines()
g.close()

for n, line in enumerate(data, 0):
	mat = '/Users/rizkyario/Downloads/darknet-hand/data/hand_dataset/training_dataset/training_data/annotations/' + data[n].replace('\n','')
	print data[n]
	rects = extract_mat(scipy.io.loadmat(mat))
	with open('/Users/rizkyario/Downloads/darknet-hand/data/hand_dataset/training_dataset/training_data/labels/' + data[n].replace('\n','').replace('.mat','.txt'), 'w+') as f:
		for rect in rects:
			row, col, h, w = convert_to_rect(rect)
			f.write('0 '+str(col/505)+' '+str(row/507)+' '+str(w/505)+' '+str(h/575)+'\n')
	# draw_rects(mat)