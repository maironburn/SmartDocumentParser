# -*- coding: utf-8 -*-

from utils.Aux_Meth import getLibForProcessing,getContentType
from settings.settings import src_url

print "defaulf url: %s" % (src_url,)
extension =getContentType(src_url)[1:]
print "extension : %s" % (extension,)


try:
    getLibForProcessing(extension)
except Exception as e:
    print "Extension no reconocida"


#print "content_type : %s, extension : %s " % (content_type,extension)

