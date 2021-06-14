from pathlib import Path
import os
def ctnttf(df_path="Data"):

    """
    Start of:
    Setting up full path to directory with labelled images
    """

    # Full or absolute path to the folder with images
    # Find it with Py file getting-full-path.py
    # Pay attention! If you're using Windows, yours path might looks like:
    # r'C:\Users\my_name\Downloads\video-to-annotate'
    # or:
    # 'C:\\Users\\my_name\\Downloads\\video-to-annotate'
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    full_path_to_images = os.path.join(BASE_DIR,df_path)

    """
    End of:
    Setting up full path to directory with labelled images
    """


    """
    Start of:
    Getting list of full paths to labelled images
    """

    # Check point
    # Getting the current directory
    # print(os.getcwd())

    # Changing the current directory
    # to one with images
    os.chdir(full_path_to_images)

    # Check point
    # Getting the current directory
    # print(os.getcwd())

    # Defining list to write paths in
    p = []

    # Using os.walk for going through all directories
    # and files in them from the current directory
    # Fullstop in os.walk('.') means the current directory
    for current_dir, dirs, files in os.walk('.'):
        # Going through all files
        for f in files:
            # Checking if filename ends with '.jpeg'
            if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.png'):
                # Preparing path to save into train.txt file
                # Pay attention!
                # If you're using Windows, it might need to change
                # this: + '/' +
                # to this: + '\' +
                # or to this: + '\\' +
                path_to_save_into_txt_files = full_path_to_images + '/' + f

                # Appending the line into the list
                # We use here '\n' to move to the next line
                # when writing lines into txt files
                p.append(path_to_save_into_txt_files + '\n')


    # Slicing first 15% of elements from the list
    # to write into the test.txt file
    p_test = p[:int(len(p) * 0.15)]

    # Deleting from initial list first 15% of elements
    p = p[int(len(p) * 0.15):]

    """
    End of:
    Getting list of full paths to labelled images
    """


    """
    Start of:
    Creating train.txt and test.txt files
    """

    # Creating file train.txt and writing 85% of lines in it
    with open('train.txt', 'w') as train_txt:
        # Going through all elements of the list
        for e in p:
            # Writing current path at the end of the file
            train_txt.write(e)

    # Creating file test.txt and writing 15% of lines in it
    with open('test.txt', 'w') as test_txt:
        # Going through all elements of the list
        for e in p_test:
            # Writing current path at the end of the file
            test_txt.write(e)

    """
    End of:
    Creating train.txt and test.txt files
    """