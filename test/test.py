import pydicom
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

dicom_path = Path(__file__).with_name("T2W-MRI.dcm")
ds = pydicom.dcmread(str(dicom_path))

pixel_array = ds.pixel_array
if getattr(pixel_array, "ndim", 0) >= 3:
    pixel_array = pixel_array[0]

plt.imshow(pixel_array, cmap="gray")

backend = matplotlib.get_backend().lower()
is_non_interactive = any(name in backend for name in ("agg", "pdf", "ps", "svg", "cairo", "template"))
if is_non_interactive:
    output_path = Path(__file__).with_name("dicom_preview.png")
    plt.axis("off")
    plt.savefig(output_path, dpi=200, bbox_inches="tight", pad_inches=0)
    print(f"Saved preview image to: {output_path}")
else:
    plt.show()
