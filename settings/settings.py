

# TEMP_DIR = '/tmp/'
DOC_TEMP_DIR = './'# cambiar directorio temporal
IMG_TEMP_DIR = './'# cambiar directorio temporal

'''
LOG Section
'''
LOGGER_NAME = 'SmartDocumentParser'
LOG_FILE = "/home/dmb/SmartDocumentParser.log"


# Diccionario que relaciona el content type con la lib de procesamiento
DOCUMENTS_TYPES_PARSER= {
                  'pdf': 'PdfParser',
                  'doc':  'DocParser'
                  }

# diccionario que relaciona el tipo de documento con los metodos lectores y escritores
READER_WRITER_DICT= {
                    'pdf': {'reader': "PdfFileReader", 'writer': "PdfFileWriter"}
                     }


#tipo pdf
src_url="https://www.mapa.gob.es/es/ganaderia/temas/produccion-y-mercados-ganaderos/20181107informedeusodeanimalesen2017_tcm30-485284.pdf"


#tipo doc
doc_url="http://www.iibce.edu.uy/ETICA/Formulario%20para%20Protocolo%20de%20experimentacion%20-%20CEUA.doc"
