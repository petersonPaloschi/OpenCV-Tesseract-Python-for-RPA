import utils.class_Tesseract as c_TesseractOCR
import utils.class_openCV as c_OpenCV

import sys
from typing import List, Dict
from PIL import Image
import glob
from os import system
import subprocess

def main() -> None:
    
    args: Dict[str, str] = read_args()

    path = args['dir_input']
    output = args['dir_output']

    for filename in glob.glob(path + '/*.png'):
        
        out_img = c_TesseractOCR.TesseractOCR().pre_process_img(filename, output)

        #c_OpenCV.OpenCV().get_text_img(out_img, output)
        
        out = c_TesseractOCR.TesseractOCR().img_to_text(out_img)
        print(filename, " -> ", out)
        
def read_args() -> Dict[str, str]:
    
    if len(sys.argv) != 3:
        print("[+] Usar -> python -m main '[dir input]' '[dir output]'")
        exit()
    
    return {
        
        "dir_input": sys.argv[1],
        "dir_output": sys.argv[2]
        
    }
    
if __name__ == "__main__":

    system('cls')
    main()
    
    #Run in cmd
    # $ python -m main 'C:\Users\workstation\Desktop\src\img' 'C:\Users\workstation\Desktop\src\img\output'