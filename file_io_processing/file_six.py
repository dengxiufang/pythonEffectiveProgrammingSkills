# -*- coding: utf-8 -*-

# 如何使用临时文件

# 实际案例

# 某项目中，我们从传感器采集数据，每收集
# 到 1G 数据后，做数据分析
# 最终只保存分析结果，这样很大的临时数据
# 如果常驻内存，将消耗大量内存资源，我们可以使用临时
# 文件存储这些临时数据（外部存储）
# 临时文件不用命名，且关闭后自动被删除

# 解决方案
# 使用标准库中 tempfile 下的 TemporaryFile,NamedTemporaryFile


from  tempfile import TemporaryFile,NamedTemporaryFile

f = TemporaryFile()

f.write('abcdef'*100000)

# 将指针指导文件首部
f.seek(0)

print(f.read(100))


ntf = NamedTemporaryFile()

# 不删除临时文件
ntf = NamedTemporaryFile(delete=False)


# 创建一个临时文件
# 关闭后删除
print(ntf.name)