# ChangeLogGeneratorPython
Generate change log by python script.  
The output format is very simple.  
It's just list commits between two tags.  
I will change format in next version.  
Next output format will support [AngularJS commit conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#heading=h.uyo6cb12dt6w).  

*How to use?*  
---
1. Move the python file to your release branch git base folder.(Contain your release version tag)
2. Open terminal panel,cd to the git base folder.
3. Input `$ python GenChangeLog.py`.
4. ChangeLog.md will generated beside the python file.
5. Chekc it!

*Why not use exist git log export tool?*  
---
Because I want a simplest tool to finished my job.  
I don't want to install too many plugins or modules. 
And too many command instruction will make this worse.  
Simple way is the best and python is the best tool to do this!  
If you don't like the output,you can modify by yourself.  
1. Python code modify very easy.
2. Cross platform.(Mac and Window)
