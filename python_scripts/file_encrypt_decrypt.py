# PGP encryption and decryption using gnuPG v1.4
import logging
import gnupg
import os 

logging.basicConfig(level=logging.INFO)
gpg=gnupg.GPG(gpgbinary='C:\Program Files (x86)\GNU\GnuPG\gpg.exe') #initializing gnuPG object
logging.info("GNU PG object initialized successfully")

recipient_email="sushank.saini@abc.com"
passphrase="passphrase"
encrypted_file_path="E:\BMO-SE-Work\python_scripts\encrypted_file.gpg"
decrypted_file_path="E:\BMO-SE-Work\python_scripts\decrypted_file.txt"

def main_function(file_path):
    if file_path is None or file_path=="": #check if file path is null or empty
        logging.error("File Path Is Empty. Please Provide a Valid File Path.")
    logging.info("File Path OK")
    key_generation_status=generate_keypair()
    if(key_generation_status is True):
        logging.info("Encrypting the File.")
        encryption_status=encrypt_file(file_path)
        if encryption_status is True:
            logging.info("File Encrypted Sucessfully.")
            logging.info("Decrypting the File.")
            decryption_status=decrypt_file(encrypted_file_path)
            if decryption_status is True:
                logging.info("File Decrypted Successfully")
            else:
                logging.info("File could not be Decrypted.")
        else:
            logging.info("File could not be Encrypted.")
    else:
        logging.info("There was an error generating the key pair for PGP encryption and decryption.")
    #upload_file_to_db()
    
def generate_keypair():
    logging.info("Generating key pair.")
    try:
        logging.info("Initializing Input Data for Key Generation.")
        input_data=gpg.gen_key_input(name_email=recipient_email,passphrase=passphrase)
        gpg.gen_key(input_data)
        logging.info("Key Pair Generated sucessfully.")
        return True
    except Exception as error:
        logging.info(error)
        return False

def encrypt_file(file):
    logging.info("Encrypting file: " +file)
    logging.info("Absolute Path of the file: "+ os.path.abspath(file))
    try:
        logging.info("Reading original file.")
        with open(file, "rb") as f:
            status=gpg.encrypt_file(f,recipients=recipient_email,output=encrypted_file_path)
        if status.ok is True:
            return True
        else:
            return False
    except FileNotFoundError as error:
        logging.error(error)
        return False
    except Exception as error:
        logging.error(error)
        return False
    
def decrypt_file(file):
    logging.info("Decrypting file: " +file)
    logging.info("Absolute Path of the file: "+ os.path.abspath(file))
    try:
        logging.info("Reading encrypted file.")
        with open(file,"rb") as f:
            status=gpg.decrypt_file(f,passphrase=passphrase,output=decrypted_file_path)
        if status.ok is True:
            return True
        else:
            return False  
    except FileNotFoundError as error:
        logging.error(error)
        return False
    except Exception as error:
        logging.error(error)
        return False
        
if __name__=="__main__":
    main_function("E:\BMO-SE-Work\python_scripts\original_file.txt")