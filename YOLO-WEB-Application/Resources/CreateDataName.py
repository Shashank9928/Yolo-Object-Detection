from pathlib import Path
import os
def cfdn(df_path="Data"):

    """
    End of:
    Setting up full path to directory with labelled images
    """
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    full_path_to_images = os.path.join(BASE_DIR,df_path)

    """
    Start of:
    Creating file classes.names
    """

    # Defining counter for classes
    c = 0

    # Creating file classes.names from existing one classes.txt
    # Pay attention! If you're using Windows, it might need to change
    # this: + '/' +
    # to this: + '\' +
    # or to this: + '\\' +
    with open(full_path_to_images + '/' + 'classes.names', 'w') as names, \
        open(full_path_to_images + '/' + 'classes.txt', 'r') as txt:

        # Going through all lines in txt file and writing them into names file
        for line in txt:
            names.write(line)  # Copying all info from file txt to names

            # Increasing counter
            c += 1

    """
    End of:
    Creating file classes.names
    """


    """
    Start of:
    Creating file labelled_data.data
    """

    # Creating file labelled_data.data
    # Pay attention! If you're using Windows, it might need to change
    # this: + '/' +
    # to this: + '\' +
    # or to this: + '\\' +
    with open(full_path_to_images + '/' + 'labelled_data.data', 'w') as data:
        # Writing needed 5 lines
        # Number of classes
        # By using '\n' we move to the next line
        data.write('classes = ' + str(c) + '\n')

        # Location of the train.txt file
        data.write('train = ' + full_path_to_images + '/' + 'train.txt' + '\n')

        # Location of the test.txt file
        data.write('valid = ' + full_path_to_images + '/' + 'test.txt' + '\n')

        # Location of the classes.names file
        data.write('names = ' + full_path_to_images + '/' + 'classes.names' + '\n')

        # Location where to save weights
        data.write('backup = backup')

    """
    End of:
    Creating file labelled_data.data
    """