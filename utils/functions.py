import os
import shutil
from io import StringIO
import xlrd
import rarfile
import zipfile
import pythoncom
from docx import Document
from win32com import client as wc
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

from utils.ocr import OCRClass


class Func():

    def __init__(self, read_db):
        self.read_db = read_db

    def toDOCX(self, filename):
        try:
            pythoncom.CoInitialize()
            word = wc.Dispatch('Word.Application')
            doc = word.Documents.Open(filename)
            doc.SaveAs(filename + 'x', 12)  # 12对应于下表中的pdf文件
            doc.Close()
            word.Quit()
            os.remove(filename)
            pythoncom.CoUninitialize()
        except Exception as e:
            pass
        finally:
            return filename + 'x'

    def read_word(self, filename):
        text = ''
        document = Document(filename)
        for paragraph in document.paragraphs:
            text += paragraph.text + ' '
        return text

    def read_excel(self, filename):
        text = ''
        book = xlrd.open_workbook(filename)
        names = book.sheet_names()
        for name in names:
            sheet = book.sheet_by_name(name)
            rows = sheet.nrows
            cols = sheet.ncols
            for r in range(rows):
                for c in range(cols):
                    text += str(sheet.cell_value(r, c)) + ' '
        return text

    def read_pdf(self, path, pages=None):
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)
        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)

        infile = open(path, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close()
        return text

    def read_img(self, path):
        _, API_Key, Secret_Key = self.read_db.get_baidu()
        self.ocr = OCRClass(API_Key, Secret_Key)
        text = self.ocr.run(path)
        return text

    def read_txt(self, path):
        with open(path, 'r', encoding='utf8') as f:
            text = f.read()
        return text

    def read(self, path):
        name, ext = os.path.splitext(path)
        if ext.lower() == '.doc':
            filename = self.toDOCX(path)
            text = self.read_word(filename)
            return text
        if ext.lower() == '.docx':
            text = self.read_word(path)
            return text
        if ext.lower() == '.xls' or ext.lower() == '.xlsx':
            text = self.read_excel(path)
            return text
        if ext.lower() == '.pdf':
            text = self.read_pdf(path)
            return text
        if ext.lower() == '.jpg' or ext.lower() == '.png' or ext.lower() == '.jpeg':
            _, API_Key, Secret_Key = self.read_db.get_baidu()
            self.ocr = OCRClass(API_Key, Secret_Key)
            text = self.ocr.run(path)
            return text
        if ext.lower() == '.txt' or ext.lower() == '.xml':
            text = self.read_txt(path)
            return text

    def un_zip(self, zip_file, to_folder):
        """  递归地提取格式为.zip的压缩包内的所有文件并在提取后将原文件删除
             @zip_file: .zip格式的压缩包文件
             @to_folder: 将文件提取到此处
        """
        try:
            # 解压
            if zip_file.endswith(".zip"):
                zf = zipfile.ZipFile(zip_file)
                zf.extractall(path=to_folder)
                zf.close()
                os.remove(zip_file)
            if zip_file.endswith(".rar"):
                zf = rarfile.RarFile(zip_file)
                zf.extractall(to_folder)
                zf.close()
                os.remove(zip_file)

            # 遍历 to_folder
            for root, dirs, files in os.walk(to_folder):
                for filename in files:
                    if filename.endswith(".zip") or filename.endswith(".rar"):
                        to_folder = os.path.join(root, filename[:-4])
                        zip_file = os.path.join(root, filename)
                        self.un_zip(zip_file, to_folder)
        except Exception as e:
            pass

    def listdir(self, basedir, list_name):  # 传入存储的list
        for file in os.listdir(basedir):
            file_path = os.path.join(basedir, file)
            if os.path.isdir(file_path):
                self.listdir(file_path, list_name)
            else:
                list_name.append(file_path)
        return list_name

    def del_dir(self, path):
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                self.del_dir(file_path)
            else:
                os.remove(file_path)
        os.rmdir(path)
