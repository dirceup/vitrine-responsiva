import os
import re

output_file_name = "../public/vitrine_responsiva-1.8.1.min.js"

# minimize CSS using YUI Compressor - stores at ./staging/
os.system("java -jar ../tools/yuicompressor-2.4.8.jar ./style.css -o ../public/style-min.css -v")

# minimize JS using Closure Compiler - stores at ./staging/
os.system("java -jar ../tools/closure-compiler-v20200719.jar --js ./lib/spin.min.js ./lib/json2.js ./vitrine_responsiva.js --js_output_file " + output_file_name)

# open css file
css_file = open("../public/style-min.css", "r")
css_content = css_file.read()
css_file.close()

# open frameads.html
frameads_file = open("../public/frameads.html", "r+")
frameads_content = frameads_file.read()

link_el = r"\<style\>(.*)<\/style\>"
style = "<style>" + css_content + "</style>"

regex = re.compile(link_el)

# replace
frameads_content = re.sub(regex, style, frameads_content)

# erase content
frameads_file.seek(0)
frameads_file.truncate()

# write replaced
frameads_file.write(frameads_content)
frameads_file.close()

# remove minified css
os.system("rm ../public/style-min.css")