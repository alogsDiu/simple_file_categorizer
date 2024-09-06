import os
from datetime import datetime


# TO GET THE FILE EXTENTION FROM PATH STRING (with a dot)
def find_extention(path_string):
    if '.' in path_string:
        ext_reverse=''

        #READING FROM THE BACK TILL DOT
        for char in path_string[::-1]:
            ext_reverse+=char
            if char == '.':
                
                # SHOULD I CONSIDER '.' AS A VALID EXTENTION? I DONT KNOW SO BY DEFAULT I DO CONSIDER IT AS A VALID EXTENTION 
                # if len(ext_reverse)==1:
                #     return ''
                
                break        

        return ext_reverse[::-1]
    
    return ''

# THE SOLUTION
def categorize_files_by_type(folder_path, file_size=None, modified_date=None): 
    if not os.path.exists(folder_path):
        raise ValueError("This dir does not exist please provide another!")
    
    if not os.path.isdir(folder_path):
        raise ValueError("This is not a directory!")

    result = {}

    dirs = [folder_path]

    while True:    

        temp_dirs = []
        
        for dir in dirs:
            dirs_inside = os.listdir(dir)

            for dir_inside in dirs_inside:
                temp_dirs.append(dir+'/'+dir_inside)

        if len(temp_dirs)==0:
            break
        else:
            dirs = []

            for temp_dir in temp_dirs:
                if os.path.isdir(temp_dir):
                    dirs.append(temp_dir)
                else:
                   if file_size != None:
                       if file_size > os.path.getsize(temp_dir):
                           continue
                   if modified_date != None:
                        if modified_date > os.path.getmtime(temp_dir):
                            continue

                   ext=find_extention(temp_dir)
                   
                   # STORE IF FILE ELSE GO DEEPER 
                   if ext in result:
                      result[ext].append(temp_dir)
                   else:
                      result[ext] = [temp_dir] 

    return result

# NEVER MIND PLEASE THIS PART IS ONLY FOR EASE OF CHECKING SO YOU DONT HAVE TO WRITE IT DOWN WHEN YOU WANT TO USE FILTERS
more_than_this_file_size = None
later_than_this_modified_date = None
#####################################

# UNCOMMENT BELOW TO USE FILTERS 
# more_than_this_file_size = 0 #  FILE SIZE IN BYTES
# later_than_this_modified_date = datetime(2023, 5, 4, 20, 5).timestamp() #PLEASE WRITE A VALID ONE dtime(year, month, day, hour, minute)

# WRITE THE DIR NAME HERE
dir_name = "3p"

try :
    result = categorize_files_by_type(dir_name, more_than_this_file_size, later_than_this_modified_date)
    print(result)
except ValueError as e:
    print(e)

## TESTS ## 

# def test_find_extention():
#     assert find_extention('dhjasfjhsa.png') == '.png', 'should be ".png" '
#     assert find_extention('dasds.dasdsadas.withDot') == '.withDot', 'should be ".withDot" '
#     assert find_extention('emptyextention') == '', 'should be "" (empty) '
#     assert find_extention('with_extention_but_null.') == '.', 'should be "." '

# import pytest

# def test_categorize_files_by_type():
    
#     with pytest.raises(ValueError,match='This dir does not exist please provide another!'):
#         categorize_files_by_type('4p')
#     with pytest.raises(ValueError,match='This is not a directory!'):
#         categorize_files_by_type('README.txt')
    
#     # IDEALY I AM SUPPOSED TO CREATE TEST DIRS BUT ...

#     assert categorize_files_by_type('1p') == {
#         '.chromedriver': ['1p/2ch/LICENSE.chromedriver'], 
#         '.pdf': ['1p/2ch/»πßΓ«⌐.pdf'], 
#         '.txt': ['1p/1ch/child.txt'], 
#         '.png': ['1p/1ch/%/Screenshot 2024-07-19.152529.png', '1p/1ch/%/--/p. - Copy.png', '1p/1ch/%/--/p..png'], 
#         '.docx': ['1p/3ch/_/__/New Microsoft Word Document.docx'], 
#         '.accdb': ['1p/3ch/_/__/New Microsoft Access Database.accdb']
#     }, '1p is not being looked correctly!'

#     assert categorize_files_by_type('2p') == {}, '2p is not being looked correctly !'

#     assert categorize_files_by_type('3p') == {'': ['3p/bmp']}, '3p is not being looked correctly !'
