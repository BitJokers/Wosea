# 这段代码由佛祖保佑可以运行

import os
dirs = ['.']

# Envs
# Folder
foldersStart = """<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Fragment>
    <StandardDirectory Id="ProgramFiles6432Folder">
      <Directory Id="INSTALLFOLDER" Name="!(bind.Property.Manufacturer) !(bind.Property.ProductName)" />
"""
foldersEnd = """    </StandardDirectory>
  </Fragment>
</Wix>
"""
# File
def fileStart(x, i):
    return f"""<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Fragment>
    <ComponentGroup Id="{x}" Directory="{i}">
      <Component>
"""
fileEnd = """      </Component>
    </ComponentGroup>
  </Fragment>
</Wix>"""

# Package
packageStart = """<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Package Name="Wosea" Manufacturer="Jaffrez and Bliod" Version="1.0.0.1" UpgradeCode="b62078cb-8244-47c6-8e1b-c7131bdeace7">
    <MajorUpgrade DowngradeErrorMessage="!(loc.DowngradeError)" />

	  <MediaTemplate EmbedCab="yes"/>
	  
    <Feature Id="Main">
"""
packageEnd = """    </Feature>
  </Package>
</Wix>"""

# Folder
folders = foldersStart
x = 1
def adddir(subdirs, dirs):
    dirs += subdirs
for dir in dirs:
    subdirs = [f'{dir}/{subdir}' for subdir in os.listdir(dir) if os.path.isdir(subdir)]
    for i in subdirs:
        temp = open(f'{x}.wxs', mode="w")
        filelist = [os.path.join(i, file) for file in os.listdir(i) if os.path.isdir(file) == False]
        i = i[2:].replace('/', '\\')
        files = fileStart(x, i)
        for file in filelist:
            z = file[2:].replace('/', '\\')
            files += f'        <File Source="{z}" />\n'
        files += fileEnd
        temp.write(files); temp.flush(); temp.close()
        folders += f'        <Directory Id="{i}" Name="!(bind.Property.Manufacturer) !(bind.Property.ProductName)\{i}" />\n'
        print(files)
        x += 1
    adddir(subdirs, dirs)
folders += foldersEnd
print(folders)