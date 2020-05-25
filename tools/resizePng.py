# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
import PIL
from PIL import Image

baseheight = 256
  
# Function to rename multiple files 
def main(): 
    arr = os.listdir(".")
    print(arr)
    for infile in arr: 
        try:
	    print(infile)
            img = Image.open(infile)
            hpercent = (baseheight / float(img.size[1]))
            wsize = int((float(img.size[0]) * float(hpercent)))
            img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
            img.save(infile, "PNG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()
