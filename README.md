# drive-query
Access files in Google Drive

## setup
The necessary Python environment is specified by a
[Conda](https://docs.conda.io/en/latest/) environment file.

You can create the environment with:
``` bash
oliver@canopus:~/repos/drive-query$ conda env create --file environment.yml
```

and then activate it with:
``` bash
oliver@canopus:~/repos/drive-query$ conda activate drive
```

## authorization
The script queries the Google Drive web API and requires OAuth2.0 for
authentication. Follow these (updated) steps from
[PyDrive](https://googleworkspace.github.io/PyDrive/docs/build/html/quickstart.html#authentication)
to create a file with authentication information:

1. Go to [APIs
   Console](https://console.developers.google.com/iam-admin/projects) and make
   your own project.
2. From 'Enable APIs and Services', search for 'Google Drive API', select the
   entry, and click 'Enable'.
3. Select 'Credentials' from the left menu, click 'Create Credentials', select
   'OAuth client ID'.
4. Now, the product name and consent screen need to be set -> click 'Configure
   consent screen' and follow the instructions. Once finished:
    1. Select 'Application type' to be *Web application*.
    2. Enter an appropriate name.
    3. Input *http://localhost:8080* for 'Authorized JavaScript origins'.
    4. Input *http://localhost:8080/* for 'Authorized redirect URIs'.
    5. Click 'Create'.
5. Click 'Download JSON' on the right side of Client ID to download
   **client_secret_<really long ID>.json**.

The downloaded file has all authentication information of your application.
**Rename the file to "client_secrets.json" and place it in your working directory.**

Add yourself to 'Test users' if necessary in the 'OAuth consent screen' page if
necessary.


## usage
Do something like this:
``` bash
(drive) oliver@canopus:~/repos/drive-query$ ./drive.py
```
