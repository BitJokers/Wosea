import os
import sys
import uuid
import zlib

def pathmd5(text: str):
    # hashmd5 = hashlib.md5()
    # hashmd5.update(text[pathLen:].replace('/', '\\').encode('utf-8'))
    # return hashmd5.hexdigest() 
    numhash: str = str(zlib.adler32(text[pathLen:].replace('/', '\\').encode('utf-8')))
    numhash = numhash.replace('1','a')
    numhash = numhash.replace('2','b')
    numhash = numhash.replace('3','c')
    numhash = numhash.replace('4','d')
    numhash = numhash.replace('5','e')
    numhash = numhash.replace('6','f')
    numhash = numhash.replace('7','g')
    numhash = numhash.replace('8','h')
    numhash = numhash.replace('9','i')
    numhash = numhash.replace('0','j')
    return numhash

def pathguid(text: str):
    # hashmd5 = hashlib.md5()
    # hashmd5.update(text[pathLen:].replace('/', '\\').encode('utf-8'))
    # return hashmd5.hexdigest() 
    # return str(zlib.adler32(text[pathLen:].replace('/', '\\').encode('utf-8')))
    return str(uuid.uuid3(uuid.NAMESPACE_DNS, text))

pathLen = len(sys.argv[1]) + 1

foldersStart = """<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Fragment>
    <StandardDirectory Id="ProgramFiles6432Folder">
      <Directory Id="INSTALLFOLDER" Name="!(bind.Property.Manufacturer) !(bind.Property.ProductName)" />
"""

foldersEnd = """    </StandardDirectory>
  </Fragment>
</Wix>
"""

def fileStart(x, guid):
    return f"""<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Fragment>
    <ComponentGroup Id="{x}" Directory="{x}">
      <Component Guid="{guid}">
"""

fileEnd = """      </Component>
    </ComponentGroup>
  </Fragment>
</Wix>"""

packageStart = """<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Package Name="Wosea" Manufacturer="Jaffrez and Bliod" Version="1.0.0.1" UpgradeCode="b62078cb-8244-47c6-8e1b-c7131bdeace7">
    <MajorUpgrade DowngradeErrorMessage="!(loc.DowngradeError)" />

	  <MediaTemplate EmbedCab="yes"/>
	  
    <Feature Id="Main">
"""

packageEnd = """    </Feature>
  </Package>
</Wix>"""

foldersId = []

def alldir(path):
    packageStr = packageStart
    foldersStr = foldersStart
    for root, dirs, files in os.walk(path):
        folderswxs = open('folders.wxs', 'w')
        for dir in dirs:
            dirpath: str = os.path.join(root,dir) # 相对路径
            # 处理File.wxs
            fileStr: str = fileStart(pathmd5(dirpath), pathguid(dirpath))
            filemid = ''
            for file in [os.path.join(dirpath, file)[pathLen:].replace('/', '\\') for file in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, file))]: # 处理的文件夹下的所有文件
                filepath = os.path.join(file) # 文件相对路径
                filemid += f'        <File Source="{filepath}" /> \n'
            if filemid != '':
                filewxs = open(f'{pathmd5(dirpath)}.wxs', mode = 'w')
                fileStr += filemid + fileEnd
                filewxs.write(fileStr); filewxs.flush(); filewxs.close() # 写入
                foldersId.append(pathmd5(dirpath)) # 统计文件夹Id
            # 处理Folders.wxs
            folderpath = dirpath[pathLen:].replace('/', '\\')
            foldersStr += f'		  <Directory Id="{pathmd5(dirpath)}" Name="!(bind.Property.Manufacturer) !(bind.Property.ProductName)\{folderpath}" />\n'
    # 测试
    dirpath: str = os.path.join(path) # 相对路径
    # 处理File.wxs
    fileStr: str = fileStart(pathmd5(dirpath), pathguid(dirpath))
    filemid = ''
    for file in [os.path.join(dirpath, file)[pathLen:].replace('/', '\\') for file in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, file))]: # 处理的文件夹下的所有文件
        filepath = os.path.join(file) # 文件相对路径
        filemid += f'        <File Source="{filepath}" /> \n'
    if filemid != '':
        filewxs = open(f'{pathmd5(dirpath)}.wxs', mode = 'w')
        fileStr += filemid + fileEnd
        filewxs.write(fileStr); filewxs.flush(); filewxs.close() # 写入
        foldersId.append(pathmd5(dirpath)) # 统计文件夹Id
    # 处理Folders.wxs
    folderpath = dirpath[pathLen:].replace('/', '\\')
    foldersStr += f'		  <Directory Id="{pathmd5(dirpath)}" Name="!(bind.Property.Manufacturer) !(bind.Property.ProductName)\{folderpath}" />\n'
    # 测试


    foldersStr += foldersEnd
    folderswxs.write(foldersStr); folderswxs.flush(); folderswxs.close()
    # 处理 Package.wxs
    packagewxs = open('package.wxs', 'w')
    for dirhash in foldersId:
        packageStr += f'		<ComponentGroupRef Id="{dirhash}" />\n'
    packageStr += packageEnd
    packagewxs.write(packageStr); packagewxs.flush(); packagewxs.close()

if __name__:
    alldir(sys.argv[1])