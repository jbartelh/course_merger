import tarfile
import os
import errno

def extract_tar_arch(input_filename, destination_dir):
    ''' extract the given filename (*.tar.gz) into the given directory '''
    with tarfile.open(input_filename, 'r') as tar:
        tar.extractall(destination_dir)

def make_tarfile(output_filename, source_dir):
    ''' creates a tar archive with from the given
    root-dir with the name of the root directory '''
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

def remove_empty_folder(directory):
    ''' to clean-up after the clean_studio_xml
    process. Removes all empty folder '''

    for root, dirs, files in os.walk(directory):
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except OSError as ex:
                if ex.errno == errno.ENOTEMPTY:
                    print 'folder not empty'

