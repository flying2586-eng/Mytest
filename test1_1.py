import diplib as dip
import math

# Load image and set pixel size
img = dip.ImageRead('N6uqw.jpg')
# dip.Show(img)
# dip.viewer.Show(img)
# dip.viewer.ShowModal(img)
# dip.Image.Show(img)
# dip.Image.ShowSlice(img)

# dip.viewer.Show(img)
# dip.viewer.Spin()
# dip.viewer.Draw()

img.Show('normal')