import utils.header as c_global_vars
import utils.class_sharpness as c_sharp

cv2 = c_global_vars.cv2
pytesseract = c_global_vars.pytesseract
PIL = c_global_vars.PIL
pathlib = c_global_vars.pathlib
DEBUG = c_global_vars.global_vars().DEBUG
re = c_global_vars.re

class TesseractOCR():
    
    def __init__(self):
        pass
    
    def pre_process_img(self, img_input, output_path):
        
        if img_input is None:
            
            if DEBUG:
                print("[ " +  img_input + " ] -> Not exist !" )
            return 
        
        filename = pathlib.Path(img_input).stem
    
        img = cv2.imread(img_input)
        # amplia a imagem da placa em 4
        
        scale_percent = 100 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        
        img = cv2.resize(img, dim, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)

        img = c_sharp.Sharpness().get_grayscale(img)

        img = c_sharp.Sharpness().thresholding(img)

        #img = c_sharp.Sharpness().GaussianBlur(img)

        #img = c_sharp.Sharpness().dilate(img)

        cnts = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
        if len(cnts) == 2 :
            
            cnts = cnts[0] 
            
        else : 
            
            cnts = cnts[1]
        
        cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])
        
        for c in cnts:
            
            x, y, w, h = cv2.boundingRect(c)
            img = cv2.rectangle(img,  (x, y), (x + w, y + h), (255, 255, 0), 1)
            
        out = output_path + r'/' + filename + "-ocr.png"
        
        cv2.imwrite( out, img )
        
        return out



    def img_to_text(self, img_input):

        pytesseract.pytesseract.tesseract_cmd = c_global_vars.global_vars().tesseractPath
    
        filename = pathlib.Path(img_input).stem
        
        out = pytesseract.image_to_string(PIL.Image.open(img_input), config=c_global_vars.global_vars().custom_config) 

        return out