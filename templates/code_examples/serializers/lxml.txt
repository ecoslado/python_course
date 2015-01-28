__author__ = 'Enrique Coslado'

from lxml import etree
from c15.e0_logger import logger

class XMLTranslator(object):
    """
    XML Translator transform a news
    xml in another format taking only
    title and text.
    """

    def __init__(self, xml_string="", xml_file_path=""):
        """
        Initializes object with xml_string if it exists
        or with xml_file_path content.

        :param xml_string: a string with xml data
        :param xml_file_path: a path to a file with xml data
        :return: self
        """

        self._xml_string = ""
        self._xml_tree = None
        self._translated_xml_tree = None
        self._translated_dict = dict(root = dict())

        if xml_file_path:
            self.set_xml_from_path(xml_file_path)

        if xml_string:
            self.set_xml_from_string(xml_string)


    def set_xml_from_string(self, xml_string):
        """
        Set xml_string from another string

        :param xml_string: string
        :return: self
        """
        try:
            self._xml_string = xml_string
            self._xml_tree = etree.fromstring(self._xml_string)

        except Exception as e:
            logger.error("Error importing xml from string. %s" % repr(e))


    def set_xml_from_path(self, xml_file_path):
        """
        Set xml_string from the content of a file

        :param xml_file_path: string with filepath
        :return: self
        """
        try:
            file = open(xml_file_path)
            xml_string = file.read()
            self._xml_string = xml_string
            self._xml_tree = etree.fromstring(self._xml_string)

        except Exception as e:
            logger.error("Error importing xml from file. %s" % repr(e))

    def _from_origin_to_dict(self):
        """
        Auxiliary function to translate xml from source to
        a dictionary
        :return: self
        """
        try:
            for elem in self._xml_tree.getchildren():
                if elem.tag == "info":
                    for subelem in elem.xpath("//Metadata/General/Metas/Titulo"):
                        self._translated_dict["root"]["title"] = subelem.text
            return self

        except Exception as e:
            logger.error("XML Parse Error. %s" % repr(e))

    def _from_dict_to_destination(self):
        """
        Auxiliary function to translate dictionary to xml
        object destination
        :return: self
        """
        self._translated_xml_tree = etree.Element("root")
        for key, value in self._translated_dict["root"].items():
            etree.SubElement(self._translated_xml_tree, key).text = value


    def get_translated_xml_string(self):
        """
        Getter xml translated string
        :return: string
        """
        return etree.tostring(self._translated_xml_tree)

    def translate_xml(self):
        """
        Translate xml object from origin format to
        destination
        :return: self
        """
        self._from_origin_to_dict()
        self._from_dict_to_destination()
        return self

