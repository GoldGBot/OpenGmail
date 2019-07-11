#!/usr/bin/env python
# coding: utf-8
# JYT work
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
import email
from apiclient import errors
import pandas as pd
import re
import os
import webbrowser

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            
            
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    print(service)
    # Call the Gmail API  Get the labels from gmail account.
    
    response = service.users().labels().list(userId='me').execute()
    
    
    #--------------------------------------------------------------------------
    
    threads=service.users().threads().list(userId='me',labelIds='INBOX',q='CCCCCCC@outlook.com').execute().get('threads',[])
    for thread in threads:
        tdata=thread['snippet']
        print(tdata)
        
        
if __name__ == '__main__':
    main()


