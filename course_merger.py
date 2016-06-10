import xml.etree.ElementTree as etree
import argparse
        
parser = argparse.ArgumentParser(description='CLI to merge two Edx-Courses.')
parser.add_argument('first', metavar='FIRSTFILE', type=argparse.FileType('r'), help='XML-File of the first Edx-Course')
parser.add_argument('second', metavar='SECONDFILE', type=argparse.FileType('r'), help='XML-File of the secend Edx-Course')
parser.add_argument('-i', '--insertafter', metavar='DISPLAYNAME', help='Insert chapters from the secondfile after the chapter with the specified display_name')
parser.add_argument('-o', '--output', metavar='FILE', default='New_course.xml', help='Name of the outputFile(default: New_course.xml)')
parser.add_argument('-v', '--verbose', action='store_const', const=True, help='Name of the outputFile')
args = parser.parse_args()

firstTree = etree.parse(args.first)
secondTree = etree.parse(args.second)
firstRoot = firstTree.getroot()
secondRoot = secondTree.getroot()

if args.insertafter is None:
    for child in secondRoot:
        firstRoot.append(child)

else:
    for child in firstRoot:
        if child.get('display_name') == args.insertafter:
            print child

#write three
firstTree.write(args.output)

## MAIN ##
#Extract_File_A
extract_tar_arch('2016_SS.tar.gz', './tmp')

#Extract_File_B

#Clean_A

#Clean_B

#Combine_A_B

#Pack_A_B
make_tarfile('2016_SS_clean.tar.gz', 'tmp/2016_SS')

