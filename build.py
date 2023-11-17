import os

path = '.'

foldersStart = """<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Fragment>
    <StandardDirectory Id="ProgramFiles6432Folder">
      <Directory Id="INSTALLFOLDER" Name="!(bind.Property.Manufacturer) !(bind.Property.ProductName)" />
"""

foldersEnd = """    </StandardDirectory>
  </Fragment>
</Wix>
"""

def fileStart(x, file_path):
    return f"""<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Fragment>
    <ComponentGroup Id="{x}" Directory="INSTALLFOLDER\{file_path}">
      <Component>
"""

fileEnd = """      </Component>
    </ComponentGroup>
  </Fragment>
</Wix>"""

folderswxs = foldersStart
dirpaths = []
num = []

def traverse_dir(path, x = 1, folderswxs = folderswxs):
    for root, dirs, files in os.walk(path):
        for subdir in dirs:
            # Env
            fileMiddle = '' #用于直接插入
            # 文件部分
            subdir_path = os.path.join(root, subdir) # 相对路径
            dirpath = subdir_path[2:].replace('/', '\\') # 切割使其符合Wix标准
            filelist = [file for file in os.listdir(subdir_path) if not os.path.isdir(os.path.join(subdir_path, file))] # 子目录下文件
            for file in filelist:
                filepath = os.path.join(subdir_path, file)[2:].replace('/', '\\') # 切割使其符合Wix标准
                fileMiddle += f'        <File Source="{filepath}" />\n' #插入
            filewxs = open(f'{x}.wxs', 'w')
            filestr = fileStart(x, dirpath) + fileMiddle + fileEnd
            filewxs.write(filestr); filewxs.flush(); filewxs.close()
            # 文件夹部分
            dirpaths.append(subdir_path[2:].replace('/', '\\'))
            num.append(x)
        # print(folderswxs)
        x += 1

def delCommon(list: list):
    li = []
    for i in list:
        if i not in li:
            li.append(i)
    return li

if __name__:
    print(traverse_dir(path))
    num = delCommon(num)
    dirpaths = delCommon(dirpaths)
    print(num)