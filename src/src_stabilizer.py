"""
Source file for Section 1 - ImageJ Stabilizer
Last edited on Dec.19 2022
Copyright Yian Wang (canying0913@gmail.com) - 2022
"""
import imagej
import numpy as np
import tifffile
import os
from time import time
import matplotlib.pyplot as plt


def ps1(text: str):
    print(f"  *  [S1 - ImageJ stabilizer]: {text}")


def s1(work_dir: dir, app_path, fpath_in, fpath_out=None, argv=None):  # -> tuple[np.ndarray, str]:
    ij = imagej.init(app_path, mode="headless")
    ps1(f"ImageJ version {ij.getVersion()}")
    # dataset = ij.io().open(fpath_in)
    # imp = ij.py.to_imageplus(dataset)
    imp = ij.IJ.openImage(fpath_in)

    if fpath_out is None:
        fpath_out = fpath_in[fpath_in.rfind(r"\\") + 1: fpath_in.rfind(".tif")] + "_stabilized.tif"
        fpath_out = os.path.join(work_dir, fpath_out)
    else:
        fpath_out = os.path.join(work_dir, fpath_out)
    ps1(f"Using output name: {fpath_out}")

    Transformation = "Translation" if argv.ij_trans == 0 else "Affine"
    MAX_Pyramid_level = argv.ij_maxpl
    update_coefficient = argv.ij_upco
    MAX_iteration = argv.ij_maxiter
    error_tolerance = argv.ij_errtol
    ps1("Using following parameters:")
    ps1(f"\t\tTransformation: {Transformation};")
    ps1(f"\t\tMAX_Pyramid_level: {MAX_Pyramid_level};")
    ps1(f"\t\tupdate_coefficient: {update_coefficient};")
    ps1(f"\t\tMAX_iteration: {MAX_iteration};")
    ps1(f"\t\terror_tolerance: {error_tolerance};")

    ps1("Starting stabilizer in headless mode...")
    st = time()
    ij.IJ.run(imp, "Image Stabilizer Headless",
              "transformation=" + Transformation + " maximum_pyramid_levels=" + str(MAX_Pyramid_level) +
              " template_update_coefficient=" + str(update_coefficient) + " maximum_iterations=" + str(MAX_iteration) +
              " error_tolerance=" + str(error_tolerance))
    ps1(f"Task finishes. Total of {int((time() - st) // 60)} m {int((time() - st) % 60)} s.")
    ij.IJ.saveAs(imp, "Tiff", fpath_out)
    imp.close()
    return tifffile.imread(fpath_out), fpath_out


def examine_stabilizer(image_i: np.ndarray, image_o: np.ndarray, idx: int):
    """
    QC function to visualize the stabilizer result within Jupyter Notebook

    Parameters:
        image_i: 3D image prior to stabilizer
        image_o: 3D image after stabilizer
        idx: index to access
    """
    assert image_i.shape == image_o.shape and 0 <= idx < image_i.shape[0]
    plt.figure(figsize=(16, 6))
    plt.title("Visualization of Dense Segmentation")
    plt.subplot(1, 2, 1)
    plt.imshow(image_i[idx, ...], cmap='gray')
    plt.title("Before")
    plt.subplot(1, 2, 2)
    plt.imshow(image_o[idx, ...], cmap='gray')
    plt.title("After")


def print_param(ij_params, f):
    Transformation = "Translation" if ij_params[0] == 0 else "Affine"
    MAX_Pyramid_level = ij_params[1]
    update_coefficient = ij_params[2]
    MAX_iteration = ij_params[3]
    error_tolerance = ij_params[4]
    f("Using following parameters:")
    f(f"Transformation: {Transformation};")
    f(f"MAX_Pyramid_level: {MAX_Pyramid_level};")
    f(f"update_coefficient: {update_coefficient};")
    f(f"MAX_iteration: {MAX_iteration};")
    f(f"error_tolerance: {error_tolerance};")
    del Transformation, MAX_Pyramid_level, update_coefficient, MAX_iteration, error_tolerance


def run_stabilizer(ij, imp, ij_params, f):
    Transformation = "Translation" if ij_params[0] == 0 else "Affine"
    MAX_Pyramid_level = ij_params[1]
    update_coefficient = ij_params[2]
    MAX_iteration = ij_params[3]
    error_tolerance = ij_params[4]
    st = time()
    ij.IJ.run(imp, "Image Stabilizer Headless",
                   "transformation=" + Transformation + " maximum_pyramid_levels=" + str(MAX_Pyramid_level) +
                   " template_update_coefficient=" + str(update_coefficient) + " maximum_iterations=" +
                   str(MAX_iteration) + " error_tolerance=" + str(error_tolerance))
    f(f"Task finishes. Total of {(time() - st) // 60}m {int((time() - st) % 60)}s.")
