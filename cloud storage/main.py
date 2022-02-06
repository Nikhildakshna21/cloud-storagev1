import os
import dropbox

class TransferData(object):
    def __init__(self, access_token):
        self.accessToken=access_token

    def uploadFile(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.accessToken)
        
        dbx.files_upload(file_from,file_to)
    
