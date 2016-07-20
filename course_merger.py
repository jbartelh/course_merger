import xml.etree.ElementTree as etree
import argparse
import entar
import studio_cleaner.clean_studio_xml as csx
import xmlmerger as merger

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
    first_temp_dir = './tmp/A'
    second_temp_dir = './tmp/B'

    #make sure both folder are empty

    #extract file a and b
    entar.extract_tar_arch(args.first, first_temp_dir)
    entar.extract_tar_arch(args.second, second_temp_dir)

    #run studio_clean_xml
    csx.clean(first_temp_dir)
    csx.clean(second_temp_dir)

    #delete empty folder
    entar.remove_empty_folder(first_temp_dir)
    entar.remove_empty_folder(second_temp_dir)

    first_xml = first_temp_dir + '/course.xml'
    second_xml = second_temp_dir + '/course.xml'

    cm = merger.XmlMerger(first_xml, second_xml)

    if args.insertafter is None:
        print 'append file a'
        cm.append()
    else:
        print 'insert at given position'
        cm.insert_at(args.insertafter)

    #Combine_A_B

    #Pack_A_B
    #entar.make_tarfile('2016_SS_clean.tar.gz', 'tmp/2016_SS')

if __name__ == '__main__':
    main()
