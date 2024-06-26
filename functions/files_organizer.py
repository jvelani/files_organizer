import os
import sys
import shutil
import datetime
sys.dont_write_bytecode = True
from log.log_logging import report

def files_organizer(input_folder_path:str, output_folder_path:str, organize_method:str='month', replace:bool=True, delete:bool=True):
    num_files_input = files_counter(input_folder_path)
    num_files = 0
    for (dirpath, dirnames, filenames) in os.walk(input_folder_path):
        for file in filenames:
            file_full_path = f'{dirpath}/{file}'
            if os.path.isfile(file_full_path):
                output_path = get_output_path(organize_method, output_folder_path, file_full_path)
                if not replace:
                    num_files += 1
                    organizer_not_replace(output_path, file_full_path, file, delete)
                else:
                    num_files += 1
                    organizer_replace(output_path, file_full_path, delete)
                report(f'{file} copied to {output_path} - {num_files}', 'debug')
            else:
                report(f'The file {file_full_path} can not be find.', 'error')

    num_files_output = files_counter(output_folder_path)

    report(f'{num_files_input} files are copied from {output_folder_path} to {input_folder_path}', 'info')

    if num_files_input > num_files_output:
        report(f'There are more files in the input than in the output!', 'error')
    elif num_files_output > num_files_input:
        report(f'There are more files in the output than in the input!', 'warning')

def get_output_path(organize_method:str, output_folder_path, file_full_path):
    modified_time = str(datetime.datetime.fromtimestamp(os.path.getmtime(file_full_path)).date())
    year = modified_time[0:4] 
    month = modified_time[5:7]
    day = modified_time[8:10]

    if organize_method.lower() == 'day':
        output_path = f'{output_folder_path}/{year}/{month}/{day}'
    elif organize_method.lower() == 'month':
        output_path = f'{output_folder_path}/{year}/{month}'
    elif organize_method.lower() == 'year':
        output_path = f'{output_folder_path}/{year}'
    else:
        output_path =f'{output_folder_path}/{year}/{month}'
    return output_path

def organizer_not_replace(output_path, file_full_path, file, delete):
    actual_file_path = f'{output_path}/{file}'
    if not os.path.isfile(actual_file_path):
        if not os.path.isdir(output_path):
            os.makedirs(output_path)
        else:
            pass
        try:
            if delete:
                shutil.move(file_full_path, f'{output_path}/{file}')
            else:
                shutil.copy(file_full_path, f'{output_path}/{file}')
        except:
            report(f'The file {file_full_path} can not be find.', 'error')
    else:
        count = 1
        while True:
            base, extension = os.path.splitext(file)
            new_name = f'{output_path}/{base}_{count}{extension}'
            if not os.path.exists(new_name):
                try:
                    if delete:
                        shutil.move(file_full_path, new_name)
                    else:
                        shutil.copy(file_full_path, new_name)   
                except IOError as e:
                    report(f'The file {file_full_path} can not be find.', 'error')
                break
            count += 1

def organizer_replace(output_path, file_full_path, delete):
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
    else:
        pass
    try:
        if delete:
            shutil.move(file_full_path, output_path) 
        else:
            shutil.copy(file_full_path, output_path)     
    except IOError as e:
        report(f'The file {file_full_path} can not be find.', 'error')

def files_counter(input_path):
    count = 0
    for (dirpath, dirnames, filenames) in os.walk(input_path):
        count = count + len(filenames)
    return count