import xml.etree.ElementTree as etree
import os,os.path

class XmlMerger(object):
    ''' merges cleaned edx courses together'''

    def __init__(self, xml_file_a, xml_file_b):
        self.xml_file_a = xml_file_a
        self.xml_file_b = xml_file_b

        self.first_tree = etree.parse(self.xml_file_a)
        self.second_tree = etree.parse(self.xml_file_b)
        self.first_root = self.first_tree.getroot()
        self.second_root = self.second_tree.getroot()

    def __append_course_a(self):
        ''' Append course A with the content of course B
        returns the new xml-tree '''
        for child in self.second_root:
            self.__add_child_to_newroot(child)

    def __insert_course_at(self, insert_node):
        ''' inserts the content of course B
        at the given position in course A '''

        for child in self.first_root:
            if child.get('display_name') == insert_node:
                print child

    def __write_xml(self, xml_root, output_file=None):
        ''' write the new xml-Tree into the file
        xml_file_a will be used, if no output file is given '''
            
        xml_root.write(output_file)

    def append(self):
        ''' Append course A with the content of course B '''
        self.__append_course_a()
        os.unlink(self.xml_file_a)
        self.__write_xml(self.first_tree, self.xml_file_a)
        
    def insert_at(self, insert_pos):
        ''' Inserts course b at the given position in course a '''
        
    def __add_child_to_newroot(self, child_node):
        self.first_root.append(child_node)
