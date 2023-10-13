import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def uploadFile(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from, "rb")
        dbx.files_upload(f.read(),file_to)
def main():
    access_token="sl.Bn0oe7DAbj1sdZtkaQ13WoXns6BXUmF0VC0-JoOSMGjid1q5S-cnnozdHIEteJ1TZWSgLfrurvsIDSIK3xQpLCHrxcsf0-anrQMENQaw4c8Dt4lkppMmNov-m2bUdfNsmnqgxR0JNAIuueXo6yU8s2w"
    tranfer_Data=TransferData(access_token)
    file_from=input("Enter the file path to tranfer: ")
    file_to = input("Enter the full path to recieve the data: ")
    tranfer_Data.uploadFile(file_from,file_to)
    print("File has been moved")
main()
