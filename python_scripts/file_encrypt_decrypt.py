#symmetric encryption and decryption using PGP
import logging
def main_function(file_name, symmetric_key):
    if file_name is None or file_name=="": #check if file name is null or empty
        logging.error("File name is empty. Please provide a valid file name.")
    if symmetric_key is None or symmetric_key=="": #check if symmetric key is null or empty
        logging.error("Please provide a symmetric key to encrypt the file.")
    encryption_status=encrypt_file(file_name)
    #push_file_to_sftp(file_name)
    #pull_file_from_sftp(file_name)
    #decrypt_file(filename)
    
def encrypt_file(file_name):
        
    


main_function("test.txt")