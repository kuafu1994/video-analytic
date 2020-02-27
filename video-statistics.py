
import numpy as np
import os 
import argparse 

from tqdm import tqdm

from yolov3.utils.utils import load_classes

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--label_folder', required=True)
    parser.add_argument('--class_path', required=True)
    parser.add_argument('--clss', required=True)
    parser.add_argument('--output_file', required=True)
    args = parser.parse_args()
    
    labels_path = os.listdir(args.label_folder)
    
    # Load the classes
    classes = load_classes(args.class_path)
    
    clss = args.clss.strip().lower() 
    
    try:
        clss_ind = classes.index(clss)
    
    except ValueError:
        print('{} is not in predefined classes'.format(clss))
        exit(1)
    
    num_images = len(labels_path)
    object_nums = []
    
    for label_path in tqdm(labels_path):
        
        data = open(os.path.join(args.label_folder, label_path)).read() 
        
        lines = data.split('\n')
        
        num_object = 0
        for line in lines:
            line = line.strip() 
            
            if line == '':
                continue 
            
            clss_num = line.split(',')[-1] 
            clss_num = int(float(clss_num))
            
            if clss_ind == clss_num:
                num_object += 1
        
        object_nums.append(num_object)
    
    object_nums = np.array(object_nums)

    with open(args.output_file, 'w') as f:
        f.write('num,min,max,mean,var\n')
        f.write('{},{},{},{},{}'.format(num_images,
                                     object_nums.min(),
                                     object_nums.max(),
                                     object_nums.mean(),
                                     object_nums.var()))
    
    

   
            
            
            

    
    
        
    
    
    

