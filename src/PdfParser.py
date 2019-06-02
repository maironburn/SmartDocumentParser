# -*- coding: utf-8 -*-

import pytesseract
import os
import re
import nltk
from src.DocumentBase import DocumentBase
from PIL import Image
from settings.settings import IMG_TEMP_DIR
from pdf2image import convert_from_path


class PdfParser(DocumentBase):

    _imgBlobs = []
    _extracted_text = []

    def __init__(self, url=None):
        # inicializacion clase base
        DocumentBase.__init__(self, url)
        self.logger.info("Clase base inicializada (DocumentBase)")

        self.split_pdf_to_img()

        self.extract_text_from_images()
        self.logger.info("Extraido el texto de la coleccion de imagenes")
        self.get_words_frecuencies()

    def do_proccess(self):

        self.split_pdf_to_img()
        self.logger.info("Documento %s convertido a imagenes" % (self._filename,))
        self.extract_text_from_images()
        self.logger.info( "Texto extraido de %s" % (self._filename,))

    def split_pdf_to_img(self):

        try:
            pages = convert_from_path(self._file_full_path)
            print "converted"
            image_counter = 1
            self.logger.info("Fichero pdf %s dividido en %d paginas" % (self._filename, len(pages)))
            for page in pages:
                filename = "%s%s%s%s" % (self._filename, "_page_", str(image_counter), ".jpg")
                page.save(filename, 'JPEG')
                self.logger.info("pagina %s convertida a jpg ----> %s" % (image_counter, filename))
                self._imgBlobs.append(filename)
                image_counter += 1

        except Exception as ex:
            self.logger.error("Excepcion en %s -> %e" % ("split_pdf_to_img", format(ex)))
            raise ex

    def extract_text_from_images(self):

        outfile = "out_text.txt"
        try:

            with open(outfile, "a") as f:

                for i in self._imgBlobs:
                    text = pytesseract.image_to_string(Image.open('%s%s' % (IMG_TEMP_DIR, i)), lang='spa').encode('utf8').strip()
                    cleaned = filter(lambda x: not re.match(r'^\s*$', x), text).replace('\n', ' ').replace('\r', '')
                    self.logger.info("Extraido texto de %s%s " % (IMG_TEMP_DIR, i))
                    # eliminamos ficheros de img temps
                    os.remove('%s%s' % (IMG_TEMP_DIR, i))
                    self.logger.info("Eliminado fichero de imagen temporal %s%s " % (IMG_TEMP_DIR, i))
                    self._extracted_text.append(cleaned)
                    f.write(cleaned)

        except Exception as ex:
            self.logger.error("Excepcion en meth %s -> %e" % ("extract_text_from_images", format(ex)))
            raise ex

    def get_extracted_text(self):
        return " ".join(self._extracted_text)

    def get_words_frecuencies(self):

        freq = nltk.FreqDist(self._extracted_text)

        for key, val in freq.items():
            print (str(key) + ':' + str(val))

if __name__ == "__main__":
    print 'Testing DocumentBase'
    PdfParser()