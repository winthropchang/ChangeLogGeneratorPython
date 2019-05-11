# -*- coding=utf-8 -*-
import subprocess

GIT_GET_VERSION = ["git","tag","--sort","*authordate"]
GET_TAG_COMMIT_INFO = ["git", "log", "--no-merges", "--date=short", "--pretty=format:- %ad (%an) %s"]

def getAllTags():
    process = subprocess.Popen(GIT_GET_VERSION, stdout=subprocess.PIPE)
    out, err = process.communicate()
    if err:
        print(err)
        return None
    out = [tag for tag in out.split("\n") if len(tag) > 0]
    return out

def getPeriodLogs(startTag, endTag):
    cmd = GET_TAG_COMMIT_INFO[:]
    if startTag and endTag:
        cmd.append(startTag + ".." + endTag)
    else:
        if startTag:
            cmd.append(startTag)
        if endTag:
            cmd.append(endTag)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out, err = process.communicate()
    if err:
        print(err)
        return None
    return out

def createChangeLogFile(tags):
    if tags == None:
        return False
    file = open("CHANGELOG.md","w")
    startTag = None
    content = []
    for tag in tags:
        detail = []
        detail.append("      \n")
        detail.append("*" + tag + "*  \n---  \n")
        logs = getPeriodLogs(startTag, tag)
        if logs == None:
            print("get period log fail!(Start tag:" + startTag + ", end tag:" + tag)
            return False
        detail.append(logs+"  \n")
        detail.append("  \n")
        content.append("".join(detail))
        startTag = tag
    file.write("".join(list(reversed(content))))
    file.close()
    return True

if __name__ == "__main__":
    if createChangeLogFile(getAllTags()):
        print("Create ChangeLog file success!")
    else:
        print("Create ChangeLog file fail!")