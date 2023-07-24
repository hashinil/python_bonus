import zipfile


def extract_archive(filepaths, destdir):
    with zipfile.ZipFile(filepaths, 'r') as archive:
        archive.extractall(destdir)


if __name__ == "__main__":
    extract_archive('file_ex/compressed.zip',
                    "files/file_ex")
