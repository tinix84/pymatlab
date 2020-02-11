#Start-Process powershell -Verb runAs
$matlabroot = "C:\Program Files\MATLAB\R2019a"
cd $matlabroot
cd "./extern/engines/python"
python ./setup.py install