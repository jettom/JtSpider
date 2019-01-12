#coding：utf-8import os,re
 #代码所在目录FILE_PATH = './'
 def analyze_code(codefilesource):
    '''    打开一个文件，统计其中的代码行数，包括空行和注释    返回含该文件总行数，注释行数，空行数的列表    :param codefilesource:    :return:    '''
    total_line = 0
    comment_line = 0
    blank_line = 0
    with open(codefilesource,encoding='gb18030',errors='ignore') as f:
        lines = f.readlines()
        total_line = len(lines)
        line_index = 0
        #遍历每一行
        while line_index < total_line:
            line = lines[line_index]
            #检查是否为注释
            if line.startswith("#"):
                comment_line += 1
            elif re.match("\s*'''",line) is not None:
                comment_line += 1
                while re.match(".*'''$",line) is None:
                    line = lines[line_index]
                    comment_line += 1
                    line_index += 1
            #检查是否为空行
            elif line =='\n':
                blank_line += 1
            line_index += 1
    print("在%s中:"%codefilesource)
    print("代码行数：",total_line)
    return [total_line,comment_line,blank_line]def list_all_files(rootdir):
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _filesdef run():
    _fs = list_all_files('./')
    total_lines = 0
    total_comment_lines = 0
    total_blank_lines = 0
    for i in _fs:
        if True:
            line = analyze_code(i)
            total_lines,total_comment_lines,total_blank_lines=total_lines+line[0],total_comment_lines+line[1],total_blank_lines+line[2]
    print("总代码行数:",total_lines)
     if __name__ == '__main__':
    run()
