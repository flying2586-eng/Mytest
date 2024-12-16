import diplib as dip
import math

# Load image and set pixel size
# img = dip.ImageRead('N6uqw.jpg')
# dip.Show(img)
# dip.viewer.Show(img)
# dip.viewer.ShowModal(img)
# dip.Image.Show(img)
# dip.Image.ShowSlice(img)

# dip.viewer.Show(img)
# dip.viewer.Spin()
# dip.viewer.Draw()

# img.Show('normal')


#!/usr/bin/env python3

# Tests some functions for finding circles using the Hough transform

# Prepare image
a = dip.Image((512, 512))
a.Fill(0)
dip.DrawEllipsoid(a, (200, 200), (256, 256))
dip.DrawEllipsoid(a, (50, 50), (350, 350))

gv = dip.Gradient(a)
gm = dip.Norm(gv)
bin = dip.IsodataThreshold(gm)

# Find circles using low-level functions
h = dip.HoughTransformCircleCenters(bin, gv)
m = dip.FindHoughMaxima(h, 10)
d = dip.PointDistanceDistribution(bin, m)
r = d.MaximumLikelihood()
print(m, r)
print('--------------------')
# Find circles using integrated function
c = dip.FindHoughCircles(bin, gv, (), 10)
print(c)

# Show original and transform
dip.viewer.Show(bin, "Input")
dip.viewer.Show(h, "Hough transform")
dip.viewer.Spin()