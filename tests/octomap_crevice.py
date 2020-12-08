#!/usr/bin/python

import numpy as np
import octomap
from termcolor import colored
from mayavi import mlab


def main():
    print(colored('Visualizing crevice data using OctoMap', 'green'))

    files = [b'./crevice_data/crevasse_octomap_0.025.bin',
             b'./crevice_data/crevasse_octomap_0.05.bin',
             b'./crevice_data/crevasse_octomap_0.1.bin']


    # initialize the tree for the crevice ot file
    for f in files:
        tree = octomap.OcTree(0.025) # the resolution given here does not matter
        if (tree.readBinary(f)):
            print(colored('Binary successfully imported', 'cyan'))

        # make sure the resolution is correct
        res = tree.getResolution()
        print(colored('Resolution for the octree is: %f' % res, 'cyan'))

        # extract the occupied and free subsets
        occupied, free = tree.extractPointCloud()

        # print some stats
        print(colored('Number of occupied points: %d' % np.shape(occupied)[0], 'cyan'))
        print(colored('Number of free points: %d' % np.shape(free)[0], 'cyan'))

        # plot the occupied subset at the min leaf level
        mlab.figure()
        mlab.points3d(occupied[:, 0], occupied[:, 1], occupied[:, 2],
                            mode="cube",
                            color=(1, 0, 0),
                            scale_factor=res)

    mlab.show()


if __name__ == "__main__":
    main()
