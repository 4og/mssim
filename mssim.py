#!/usr/bin/python

import sys, os, numpy, scipy.misc
from scipy.ndimage import filters

class MSSIM:
    def gaussian(self, size, sigma):
        x = numpy.arange(0, size, 1, float)
        y = x[:,numpy.newaxis]
        xc = (size-1) / 2
        yc = (size-1) / 2

        gauss = numpy.exp(-((x-xc)**2 + (y-yc)**2) / (2*sigma**2))
        return gauss / gauss.sum()

    def compute(self, fn, fns, k=[0.01, 0.03]):
        c1 = (k[0]*255)**2
        c2 = (k[1]*255)**2
        win = self.gaussian(11, 1.5)

        im1 = scipy.misc.imread(fn, 1)
        mu1 = filters.correlate(im1, win)
        mu1_sq = mu1*mu1;
        s1sq =filters.correlate(im1*im1, win)-mu1_sq

        for f in fns:
            im2 = scipy.misc.imread(f, 1)
            if im1.shape != im2.shape:
                print("{}: Incorrect image. All images "
                      "should be of equal size".format(f))
                continue

            mu2 = filters.correlate(im2, win)
            mu2_sq = mu2*mu2;
            mu1_mu2 = mu1*mu2;

            s2sq = filters.correlate(im2*im2, win)-mu2_sq
            s12 = filters.correlate(im1*im2, win)-mu1_mu2

            ssims = ((2*mu1_mu2 + c1)*(2*s12 + c2))/ \
                    ((mu1_sq + mu2_sq + c1)*(s1sq + s2sq + c2))
            print("{:24} {:.4f}".format(os.path.basename(f), ssims.mean()))


if len(sys.argv) < 3:
    print("Usage: mssim.py reference-image other-images ...")
    exit()

MSSIM().compute(sys.argv[1], sys.argv[2:])

