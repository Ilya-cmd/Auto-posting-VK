import xml.etree.ElementTree as xml
import time

class XML:

    fileName = False

    def __init__(self, fileName):
        self.fileName = fileName + ".xml"
        self.openFile()

    def openFile(self):
        try:
            file = open(self.fileName, "r")
        except FileNotFoundError:
            self.createFile()

    def createFile(self):
        rootXML = xml.Element("settings")

        token = xml.Element("token")
        token.text = "token"
        rootXML.append(token)

        textPost = xml.Element("textPost")
        textPost.text = "Text post"
        rootXML.append(textPost)

        interval = xml.Element("interval")
        interval.text = "120"
        rootXML.append(interval)

        post = xml.Element("post")
        rootXML.append(post)

        attachments = xml.SubElement(post, "attachments")
        attachment: xml.SubElement

        attachment = xml.SubElement(attachments, "attachment")
        attachment.text = "attachment"

        copyright = xml.SubElement(post, "copyright")
        copyright.text = "copyright"

        v = xml.SubElement(post, "v")
        v.text = "5.122"

        groups = xml.Element("groups")
        rootXML.append(groups)

        group = xml.SubElement(groups, "group")
        group.text = "short name group"

        file = open(self.fileName, "w")
        file.write(xml.tostring(rootXML, encoding="utf-8", method="xml").decode(encoding="utf-8"))
        file.close()

    def editFile(self, element, attribute):
        tree = xml.ElementTree(file=self.fileName)
        rootXML = tree.getroot()
        for elem in rootXML.iter(element):
            elem.text = str(attribute)

        tree = xml.ElementTree(rootXML)
        tree.write(self.fileName)

    def parsingFile(self, elements, text = True):
        tree = xml.ElementTree(file=self.fileName)
        rootXML = tree.getroot()
        for element in rootXML.iter(elements):
            if (text):
                return element.text
            return element