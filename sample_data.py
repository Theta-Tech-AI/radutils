import logging
import os
import nibabel as nib
from nilearn.datasets import fetch_atlas_harvard_oxford, load_mni152_template

logging.basicConfig(level=logging.DEBUG)

logging.info('📂 Setting up output directory...')
output_directory = 'sample_nifti_data'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    logging.info(f'📁 Created output directory: {output_directory}.')
else:
    logging.info(f'📁 Output directory already exists: {output_directory}.')
logging.debug(f'📂 {output_directory = }')

logging.info('⬇️ Downloading MNI152 template as sample MRI data...')
sample_mri_image = load_mni152_template()
logging.debug(f'📊 {sample_mri_image = }')

logging.info('💾 Saving sample MRI data...')
sample_mri_image_path = os.path.join(output_directory, 'sample_mri.nii.gz')
nib.save(sample_mri_image, sample_mri_image_path)
logging.info(f'✅ Saved sample MRI data to {sample_mri_image_path}.')
logging.debug(f'📊 {sample_mri_image_path = }')

logging.info('⬇️ Downloading Harvard-Oxford cortical atlas as sample segmentation data...')
atlas_dataset = fetch_atlas_harvard_oxford('cort-maxprob-thr0-1mm')
logging.debug(f'📊 {atlas_dataset = }')

logging.info('💾 Saving sample segmentation data...')
sample_segmentation_image = atlas_dataset.maps  # This is already a Nifti1Image object
logging.debug(f'📊 {type(sample_segmentation_image) = }')
sample_segmentation_image_path = os.path.join(output_directory, 'sample_segmentation.nii.gz')
nib.save(sample_segmentation_image, sample_segmentation_image_path)
logging.info(f'✅ Saved sample segmentation data to {sample_segmentation_image_path}.')
logging.debug(f'📊 {sample_segmentation_image_path = }')

logging.info('✅ Sample data download and save completed.')
