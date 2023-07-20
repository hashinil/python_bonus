import zipfile
import pathlib


def make_archive(filepaths, destdir):
    destdir = pathlib.Path(destdir, "compressed.zip")
    with zipfile.ZipFile(destdir, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["files/doc.txt", "files/report.txt"], destdir="files")
