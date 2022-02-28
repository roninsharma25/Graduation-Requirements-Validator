import pandas as pd
import StringIO


def analyzeData(uploadedFile):
    file = StringIO(uploadedFile.getvalue().decode('utf-8')).read()
    fileData = pd.read_csv(file)