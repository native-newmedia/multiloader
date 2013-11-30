# -*- coding: cp1252 -*-
# import multiloader
# by Sanjeev Kumar
# check for update : www.devilsan.com

__Version__ = 1.0
__Author__="Sanjeev Kumar"
mx = 10
#lang="eng"
print("----------------New Execution--------")
from xml.dom.minidom import parseString
import os,locale


try:
	import PeyeonScript as eyeon
except ImportError as err:
    print("To err is human")


lang = locale.getdefaultlocale()[0]

def multiload():
    fusion=eyeon.scriptapp("Fusion")
    comp=fusion.GetCurrentComp()
    str=comp.AskUser("Multi-Loader",{1:{1: "loaderNum", 2: "Slider","Name":"No. of Loaders","Min":1,"Max":mx,"Integer":True},
                                    2:{1: "Msg", 2:"Text","Name":wrn,"ReadOnly":True,"Default":msg,"Wrap":True,"Lines":3},
                                    3:{1: "dlgCheck", "Name": "Lock Composition",2: "Checkbox", "Default": 1},
                                    4:{1: "Msg2", 2:"Text","Name":nte,"ReadOnly":True,"Default":lok,"Wrap":True,"Lines":4}
                                    })
    print(str)
    if str is not None:
        if str['dlgCheck'] == 1:
            cmpLk=1
        else:
            cmpLk=0
        t=(int(str['loaderNum']))
        dialog={}

        for i in range(t):
            pat={1: 'Sequence{0}'.format(i), 2: 'FileBrowse','Save': True,'Default': ''}
            dialog.update({i:pat})

        seqLoader = comp.AskUser("Load Multiple Sequences",dialog)

        for i in range(t):
            if cmpLk==1:
                comp.Lock()
            if seqLoader['Sequence{0}'.format(i)]!='':
                loader = comp.Loader({'Clip' : seqLoader['Sequence{0}'.format(i)]})
            elif seqLoader['Sequence{0}'.format(i)]=='':
                print("You didn't selected anything for Sequence{0}".format(i))
            if cmpLk==1:
                comp.Unlock()
    else:
        print(usrcan)



langloc=os.getcwd()+"\Scripts\Comp\lang.xml"

try:
    file =open(langloc,'r')
    strErr="Found"
    print("in Try: "+strErr)
except IOError as err:
	strErr="{0}".format(err)
	print(strErr)

if strErr =="[Errno 2] No such file or directory: '\\Scripts\\Comp\\lang.xml'" or lang=="en_ca" or lang=="en_US" or lang=="en_in" or lang=="en_gb" or lang=="en_AU":
    wrn="Warning"
    msg="Select the number of sequence you would want to load, depending upon the number you will get next prompt with multiple loaders in one."
    lok="If the Composition is locked, Fusion suppress any dialog boxes which may appear, and additionally prevents any re-rendering in response to changes to the controls"
    wrn="Warning"
    nte="Note"
    usrcan="User Cancelled"
    print(strErr)
    print ("Hello")
    print(lang)
    multiload()
elif strErr=="Found":
    file =open(langloc,'r',encoding="utf-8")
    data=file.read()
    file.close()
    dom=parseString(data)
    if lang=="ru":
        print("Bingo!!!")
        lok=dom.getElementsByTagName('rus_lok')[0].attributes['name'].value
        msg=dom.getElementsByTagName('rus_msg')[0].attributes['name'].value
        wrn=dom.getElementsByTagName('rus_warn')[0].attributes['name'].value
        nte=dom.getElementsByTagName('rus_note')[0].attributes['name'].value
        usrcan=dom.getElementsByTagName('rus_usrCan')[0].attributes['name'].value
        multiload()
        print("Russian lang")
    elif lang=='fr_FR'or lang=='fr_CA' or lang=='fr_be'or lang=="fr_lu" or lang == "fr":
        print("in Fr Block "+strErr)
        lok=dom.getElementsByTagName('fr_lok')[0].attributes['name'].value
        msg=dom.getElementsByTagName('fr_msg')[0].attributes['name'].value
        wrn=dom.getElementsByTagName('fr_warn')[0].attributes['name'].value
        nte=dom.getElementsByTagName('fr_note')[0].attributes['name'].value
        usrcan=dom.getElementsByTagName('fr_usrCan')[0].attributes['name'].value
        multiload()
    elif lang=="es_ar" or lang=="es_ES" or lang=="es_mx":
        lok=dom.getElementsByTagName('es_lok')[0].attributes['name'].value
        msg=dom.getElementsByTagName('es_msg')[0].attributes['name'].value
        wrn=dom.getElementsByTagName('es_warn')[0].attributes['name'].value
        nte=dom.getElementsByTagName('es_note')[0].attributes['name'].value
        usrcan=dom.getElementsByTagName('es_usrCan')[0].attributes['name'].value
    elif lang=="ja_JP":#Japanese
        pass
    elif lang=="pl":#Polska
        pass
    elif lang=="zh_CN":#Chinese Simplified
        pass

##For Testing Lang Blocks #strErr=="Found":#

print("----------End Code Line-----------")
