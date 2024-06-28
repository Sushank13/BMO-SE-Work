import logging
def main_function(file_name):
    if file_name is None or file_name=="": #check if file name is null or empty
        logging.error("File name is empty. Please provide a valid file name.")
    #encrypt_file(file_name)
    #push_file_to_sftp(file_name)
    #pull_file_from_sftp(file_name)
    #decrypt_file(filename)
    


main_function(None)