import xml.etree.ElementTree as etree
import argparse
import entar
import studio_cleaner.clean_studio_xml as csx
import xmlmerger as merger
import os, os.path
from distutils import dir_util

def parseargs():
    ''' Parse the command-line arguments '''
    parser = argparse.ArgumentParser(
        description='CLI to merge two Edx-Courses.')

    parser.add_argument('first',
                        metavar='FIRSTFILE',
                        help='tar.gz-File of the first Edx-Course')

    parser.add_argument('second',
                        metavar='SECONDFILE',
                        help='tar.gz-File of the secend Edx-Course')

    parser.add_argument('-i', '--insertafter',
                        metavar='DISPLAYNAME',
                        help='Insert chapters from the secondfile after'
                        + 'the chapter with the specified display_name')

    parser.add_argument('-o', '--output',
                        metavar='FILE',
                        default=None,
                        help='Name of the outputFile(default: New_course.xml)')

    parser.add_argument('-v', '--verbose',
                        action='store_const',
                        const=True, help='Name of the outputFile')

    return parser.parse_args()

def main():
    ''' main '''
    args = parseargs()
    merge_course(args.first, args.second, args.insertafter, args.output)

    #make sure both folder are empty
def merge_course(firstfile, secondfile, output=None, insertafter=None):
    
    first_temp_dir = './tmp/A'
    second_temp_dir = './tmp/B'
    
    #extract file a and b
    entar.extract_tar_arch(secondfile, second_temp_dir)
    entar.extract_tar_arch(firstfile, first_temp_dir)

    coursename_b = os.listdir(second_temp_dir)[0]
    coursename_a = os.listdir(first_temp_dir)[0]

    second_temp_dir = os.path.join(second_temp_dir, coursename_b)
    first_temp_dir = os.path.join(first_temp_dir, coursename_a)

    #run studio_clean_xml
    csx.clean(second_temp_dir)
    csx.clean(first_temp_dir)

    #delete empty folder
    entar.remove_empty_folder(second_temp_dir)
    entar.remove_empty_folder(first_temp_dir)

    second_xml = second_temp_dir + '/course.xml'
    first_xml = first_temp_dir + '/course.xml'
    
    cm = merger.XmlMerger(first_xml, second_xml)

    if insertafter is None:
        cm.append()
    else:
        cm.insert_at(insertafter)

    #Combine_A_B
    dir_util.copy_tree(second_temp_dir, first_temp_dir)

    #writes combined xml tree in first_temp_dir
    cm.write_xml()

    #Pack_A_B(first_temp_dir)
    if output is None:
        entar.make_tarfile('/media/joel/Transfer/OpenEdX/course_export/output.tar.gz', first_temp_dir)
    else:
        entar.make_tarfile(output, first_temp_dir)

    #clean

if __name__ == '__main__':
    main()
