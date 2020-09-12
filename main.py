# -*- coding: utf-8 -*-
import vk_api
import time

from modules import XML as moduleXml

XML = moduleXml.XML("settings")
VK = vk_api.VkApi(token=XML.parsingFile("token"))

done = False

groupsId = []
groupsShortName = ""
for child in XML.parsingFile("groups", False):
    groupsShortName += child.text + ","

for group in VK.method("groups.getById", {"group_ids": groupsShortName}):
    groupsId.append(group["id"] * -1)

del groupsShortName

textPost = XML.parsingFile("textPost")
intervalPost = int(XML.parsingFile("interval"))

attachments = [attachment.text for attachment in XML.parsingFile("attachments", False)]
copyright = XML.parsingFile("copyright")
v = XML.parsingFile("v")

def publicPosts():
    for groupId in groupsId:
        for i in range(1, 5):
            result = VK.method("wall.post", {
                "owner_id": groupId,
                "message": textPost,
                "attachments": attachments,
                "copyright": copyright,
                "v": v
            })
            if result["post_id"]:
                print("Good post, id post - " + str(result["post_id"]))
            else:
                print("Error posting")

if __name__ == "__main__":
    done = True

while done:
    publicPosts()
    time.sleep(intervalPost)