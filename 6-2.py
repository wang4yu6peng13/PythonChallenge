import zipfile, re
findnothing = re.compile(r"Next nothing is (\d+)").match
comments = []  # 收集注释信息的列表
z = zipfile.ZipFile("channel.zip", "r")  # 读取压缩包文件
seed = "90052"
while True:
    fname = seed + ".txt"
    comments.append(z.getinfo(fname).comment.decode())
    guts = z.read(fname).decode()
    m = findnothing(guts)
    if m:
        seed = m.group(1)
    else:
        break

res = "".join(comments)
print(res)  # 打印所有注释信息