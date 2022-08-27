import utils.header as c_global_vars
import utils.class_sharpness as c_sharp

pytesseract = c_global_vars.pytesseract
cv2 = c_global_vars.cv2
Output = c_global_vars.Output
PIL = c_global_vars.PIL
re = c_global_vars.re
pathlib = c_global_vars.pathlib

class OpenCV:
    
    def __init__(self):
        pass
    
    pytesseract.pytesseract.tesseract_cmd = c_global_vars.global_vars().tesseractPath

    def get_text_img(self, img_input, output_path):
        
        if img_input is None:
            return
        
        filename = pathlib.Path(img_input).stem
        
        img = cv2.imread(img_input)
        
        array = pytesseract.image_to_data(img, output_type=Output.DICT)
        
        text_box = len(array['text'])
        
        #print(data['text'])
        
        for index in range(text_box):
            
            if int(array['conf'][index]) > 60:
                (x, y, w, h) = (array['left'][index], array['top'][index], array['width'][index], array['height'][index])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        cv2.imwrite(output_path + r'/' + filename + '-openCV.png', img)