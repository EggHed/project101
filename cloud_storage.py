import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BKk_4AKlvK42j48n1IYMAfUecRFy03EX5RDfxZufT9rt7_KyrlPVReCOSQwfx9ZVZbTitjE78FdrE_LYV0i2R3WEMrRn3xRPXEy8WkWhbmIbYbDB67pQ9PhN8oxYRltl2_hEUvE'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")

    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()