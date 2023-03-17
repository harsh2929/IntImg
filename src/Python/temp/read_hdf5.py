
import h5py
import numpy

def entry(nx, location):
    for item in nx[location].keys():
        print (item)
        #add files
nx = h5py.File(filename, "r")

entries = [entry for entry in nx['/'].keys()] 
print (entries)

three3d = numpy.asarray(nx.get(''))
wt = numpy.asarray(nx.get(''))

slices_tot = numpy.asarray(nx.get('/slices_tot'), dtype=int)[0]
import matplotlib.pyplot as plt
fig = plt.figure()

a=fig.plotting(1,1,1)
a.set_title('noise')
imgplot = plt.imshow(Weights3D[0].T)
plt.show()