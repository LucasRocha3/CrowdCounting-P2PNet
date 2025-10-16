import os
import argparse

def create_list_file(data_root, dataset_part, output_file):
    images_path = os.path.join(data_root, dataset_part, 'images')
    gt_path = os.path.join(data_root, dataset_part, 'ground_truth')
    
    with open(output_file, 'w') as f:
        for img_name in os.listdir(images_path):
            if img_name.endswith('.jpg'):
                img_path = os.path.join(dataset_part, 'images', img_name)
                gt_name = 'GT_' + img_name.replace('.jpg', '.txt')
                gt_file_path = os.path.join(gt_path, gt_name)
                
                # Check if the corresponding ground truth file exists
                if os.path.exists(gt_file_path):
                    gt_list_path = os.path.join(dataset_part, 'ground_truth', gt_name)
                    f.write(f'{img_path} {gt_list_path}\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Create list files for ShanghaiTech dataset', add_help=False)
    parser.add_argument('--dataset', default='A', type=str, help='Part of the dataset to process (A or B)')
    args = parser.parse_args()

    if args.dataset == 'A':
        data_root = 'ShanghaiTech_Crowd_Counting_Dataset/part_A_final'
    elif args.dataset == 'B':
        data_root = 'ShanghaiTech_Crowd_Counting_Dataset/part_B_final'
    else:
        print('Invalid dataset part specified. Please use A or B.')
        exit()

    # Create train.list
    create_list_file(data_root, 'train_data', os.path.join(data_root, 'train.list'))
    
    # Create test.list
    create_list_file(data_root, 'test_data', os.path.join(data_root, 'test.list'))
