import tarfile
import os
import errno

def extract_tar_arch(filename, dir):
    ''' extract the given filename (*.tar.gz) into the given directory '''
    try:
        print '%20s  %s' % (filename, tarfile.is_tarfile(filename))
        tarObj = tarfile.open(filename, 'r')
        
        for member_info in tarObj.getmembers():
            print member_info.name
            print '\tMode    :\t', oct(member_info.mode)
            print '\tType    :\t', member_info.type
            print '\tSize    :\t', member_info.size, 'bytes'
            print
        
    except IOError, err:
        print '%20s  %s' % (filename, err)

def pack_as_tar(dir):
     ''' creates a tar archive with from the given root-dir with the name of the root directory '''
    
def remove_empty_folder(dir):
    ''' to clean-up after the clean_studio_xml process remove all empty folder '''
    
    for root, dirs, files in os.walk(dir):
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except OSError as ex:
                if ex.errno == errno.ENOTEMPTY:
                    print 'folder not empty'
                    
    