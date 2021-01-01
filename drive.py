#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


if __name__ == "__main__":
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)
    for f in drive.ListFile({"q": "'root' in parents and trashed=false"}).GetList():
        print(f"title: {f['title']}, id: {f['id']}")
