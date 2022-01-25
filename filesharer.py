from filestack import Client


class FileSharer:

    def __init__(self, filepath, api_key='AEI2SO4bRkenQ9FYanPwMz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_fileline = client.upload(filepath=self.filepath)
        return new_fileline.url
