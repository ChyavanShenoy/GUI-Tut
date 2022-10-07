import os
import matplotlib.pyplot as plt
from doctr.io import DocumentFile
from doctr.models import ocr_predictor
import json

os.environ['USE_TORCH'] = '1'

filePath = ""


def get_filePath(path):
    global filePath
    filePath = path
    extract_text()


def extract_text():
    global filePath

    # Load the model
    model = ocr_predictor('db_resnet50', 'crnn_vgg16_bn',
                          pretrained=True, detect_language=True)

    # Load the document
    doc = DocumentFile.from_images(filePath)

    # Predict the document
    result = model(doc)

    # Store the result in a JSON file
    xml_output = result.export_as_xml()
    print(xml_output)
    for output in xml_output:
        xml_bytes_string = output[0]
        xml_element = output[1]
        xml_string = xml_bytes_string.decode("utf-8")
        with open('output.xml', 'w') as f:
            f.write(xml_string)
        # with open('data.xml', 'w') as f:
        #     f.write(xml_element)
        print(xml_element)

    # with open('data.xml', 'w') as f:
    #     json.dump(json_data,
    #               f, ensure_ascii=False, indent=4)


get_filePath('./images/gst-bill.jpg')
