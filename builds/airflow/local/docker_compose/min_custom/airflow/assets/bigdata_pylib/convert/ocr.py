

from PIL import Image
from pytesseract import Output
import pytesseract
import numpy as np
import cv2

from workflow_lib import get_files_from_path

__all__ = ['image_dir_to_text']

def image_dir_to_text(path, res='low', debug=False):
    """meant to be run within a single DAG task
    
    Takes in a path and gives a hash of the files and associated text found with them
    Input: string path
    Output: dict
    """
    results = {}
    target_extensions = ['jpg', 'jpeg']

    # get full files paths
    file_list = get_files_from_path(path, target_extensions)

    for i, file_path in enumerate(file_list):
        text = ''
        if debug: print(f"\n{i}) {file_path}")
        if res.lower() == 'high':
            text = extract_characters_from_highres_image(file_path, debug)
        else:
            text = extract_characters_from_lowres_image(file_path, debug)

        results.update({file_path: text})
    return results

def clean_noise(img, debug=False):
    """
    input: np.array: an image array
    output: str
    """
    if debug: print(f'trying to cut noise for "{type(img)}" (expecting <class "numpy.ndarray">)')
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    img = cv2.GaussianBlur(img, (1, 1), 0)
    return pytesseract.image_to_string(img)

def extract_characters_from_lowres_image(file_path, debug=False):
    """
    Simple text extract.  Meant for low size and resolution
    """
    if debug: print(f"::extract_characters_from_lowres_image({file_path}):")
    img = np.array(Image.open(file_path))
    
    text = pytesseract.image_to_string(img)
    print(f"\ttext({type(text)}): '{text}'")

    text = text.replace('\n\x0c','')

    if debug:
        print(f"{text=}")

    if text.strip() == "":
        text = clean_noise(img, debug)

    return text

def extract_characters_from_highres_image(file_path, debug=False):
    """
    This feature is meant to work on a lot of high res images in a pipeline.
    """
    text = ''
    try:
        img = cv2.imread(file_path)
        results = pytesseract.image_to_data(img, output_type=Output.DICT)

        text = ' '.join(results["text"]).strip()
        if debug:
            print(f"{text=}")

        if text == "":
            #if debug: print('!!!WARNING!!! NO TEXT FOUND, MOVING ON...')
            text = clean_noise(img, debug)
            text = text.replace('\n\x0c','')
            if debug: print(f"\tnew text: {text}")

    except Exception as e:
        print(f'err: {e}')
    finally:
        return text
    

def apply_text_rect(results, image, debug=False):
    """
    From the highres function, we can use additional features to create
    boxes around the text that was found.
    From these results one can additionally save and/or show the images
    via additional functions 'save_as' and 'display_image'
    """
    for i in range(0, len(results["text"])):
        x = results["left"][i]
        y = results["top"][i]

        w = results["width"][i]
        h = results["height"][i]

        text = results["text"][i]
        conf = int(results["conf"][i])

        if conf > 70:
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, text, (x, y - 10), 

    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)
    return cv2

def display_image(cv2, image):
    """
    WARNING: DO NOT USE in airflow as this will attempt to display an image within the airflow container
    Might be usefull for testing and debugging else where
    """
    cv2.imshow(image)

def save_as(file_path, image, cv2, debug=False):
    """simple save-as feature that just adds a '1' before the '.ext' of the filename"""
    try:
        ext = '.' + file_path.split('.')[-1]
        save_as_file_path = file_path.replace(ext, '1'+ext)
        if debug:
            print('')
            print(f"{save_as_file_path=}")
        cv2.imwrite(save_as_file_path, image)
        cv2.waitKey(0)
        return True
    except:
        return False







def extract_characters_from_highres_image_old(file_path, debug=False):

    if debug:
        print(f"#file_path: {file_path}")

    image = cv2.imread(file_path)

    if debug: 
        print('')
        print(' - results:')
    results = pytesseract.image_to_data(image, output_type=Output.DICT)
    for k, v in results.items():
        if debug: 
            print(f"\t>> {k}: {v}")

    text_concat = ''.join(results["text"]).strip()
    if debug: 
        print('')
        print(f"\n{text_concat=}")

    if text_concat == "":
        #raise AirflowFailException("No 'text' elements found !!!")
        print('NO TEXT FOUND, MOVING ON...')
        clean_noise(results)

    print(f"--cut noise text: {text}")
    return text

    
    for i in range(0, len(results["text"])):
        x = results["left"][i]
        y = results["top"][i]

        w = results["width"][i]
        h = results["height"][i]

        text = results["text"][i]
        conf = int(results["conf"][i])

        if conf > 70:
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, text, (x, y - 10), 

    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)
    # commented out as we do not want to actually try show the images within a DAG log 
    #cv2.imshow(image)

    try:

        ext = '.' + file_path.split('.')[-1]
        save_as_file_path = file_path.replace(ext, '1'+ext)
        print('')
        print(f"{save_as_file_path=}")
        cv2.imwrite(save_as_file_path, image)
        cv2.waitKey(0)
    except:
        pass