# PGP encryption and decryption using gnuPG v1.4
import logging
import gnupg

logging.basicConfig(level=logging.INFO)
gpg=gnupg.GPG(gpgbinary='C:\Program Files (x86)\GNU\GnuPG\gpg.exe') #initializing gnuPG object
logging.info("GNU PG object initialized successfully")

def main_function(file):
    if file is None or file=="": #check if file name is null or empty
        logging.error("File name is empty. Please provide a valid file name.")
    logging.info("File Name OK")
    key_generation_status=generate_keypair()
    if(key_generation_status is True):
        logging.info("Encrypting the file.")
        #encryption_status=encrypt_file(file)
    else:
        logging.info("There was an error generating the key pair for PGP encryption and decryption.")
    #upload_file_to_sftp(file_name)
    #download_file_from_sftp(file_name)
    #decrypt_file(filename)
    #upload_file_to_db()
    
def generate_keypair():
    logging.info("Generating key pair.")
    try:
        logging.info("Initializing Input Data for Key Generation.")
        recipient_email="sushank.saini@abc.com"
        passphrase="passphrase"
        input_data=gpg.gen_key_input(name_email=recipient_email,passphrase=passphrase)
        key=gpg.gen_key(input_data)
        logging.info("Key Pair Generated sucessfully.")
        public_key=gpg.export_keys(key.fingerprint)
        logging.info("Public Key Generated Successfully")
        private_key=gpg.export_keys(key.fingerprint, True)
        logging.info("Private Key Generated Successfully")
        logging.info("Exporting Public Key into a file")
        with open("public_key.txt", "w") as file1:
            file1.write(public_key)
            file1.close()
        logging.info("Exporting Private Key into a file")
        with open("private_key.txt","w") as file2:
            file2.write(private_key)
            file2.close()
        return True
    except Exception as error:
        logging.info(error)
        return False

if __name__=="__main__":
    main_function("test.txt")