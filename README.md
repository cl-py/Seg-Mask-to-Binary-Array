# Seg-Mask-to-Binary-Array
Creates a binary array .txt file from a segmentation mask. 
Intended primarily for use for CVAT, as binary array creation when exporting as Segmentation Mask 1.1 is not currently supported.

Can write arrays of multiple .png files from one directory. It is assumed that the segmentation mask is binary, i.e there are only 2 color values in the image. The background is assumed to be black (0, 0, 0), but values can be manually adjusted.
