import urllib.request
import re

contents = urllib.request.urlopen("https://www.cvk.gov.ua/pls/vp2019/wp335pt001f01=719.html").read().decode("windows-1251")
regex = re.compile(r"class=a1 href=\"(.*?)\"")
matches = regex.findall(contents)
print(len(matches))
vds = []
for str_match in matches:
    vds.append((re.search(r"(\d+)\.html", str_match).group(1), str_match))
    

i = 0
for vd in vds:
    print(i)
    with open(vd[0] + ".dat", "w") as file:
        contents = urllib.request.urlopen("https://www.cvk.gov.ua/pls/vp2019/" + vd[1]).read().decode("windows-1251")
        for a in contents.split("<tr")[2:]:
            file.write(",".join(re.findall("\d+", "\n".join(a.split("\n")[:-2]))))
            file.write("\n")
    i += 1

