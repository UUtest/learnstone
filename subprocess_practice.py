import subprocess
'''
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#子进程还需输入，可以通过communitcate()方法输入
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
'''

child1 = subprocess.Popen(["ls", "-1"], stdout = subprocess.PIPE)
child2 = subprocess.Popen(["wc"], stdin = child1.stdout, stdout = subprocess.PIPE)
out = child2.communicate()
print(out)

child = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
child.communicate()
