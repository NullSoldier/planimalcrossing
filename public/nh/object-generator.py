

from os import walk, mkdir
from PIL import Image
from shutil import copyfile, rmtree

GENERATED_WARNING = "/** \n * This file was auto-generated with object-generator.py \n */\n\n"

def capitalizeName(name):
    if ("zother" in name):
        name = name[1:]
    names = name.split('-')
    result = ""
    for n in names:
        result += n.capitalize()
        result += " "
    return result.strip()

#
# Css Generation
#

css_file = open("css/objects.css", "a+")
css_file.truncate(0)
css_file.write(GENERATED_WARNING)

rmtree('img/flat-tiles')
mkdir('img/flat-tiles')

for (dirpath, dirnames, filenames) in walk("img/tiles"):
    css_file.write("/* {} */\n".format(dirpath))
    for file in filenames:
    	if file != ".DS_Store":
            copyfile(dirpath + '/' + file, "img/flat-tiles/" + file)
            name = file[:-4]
            css_file.write(".sprite-icon.{} {{ \n    background-image: url('/nh/img/flat-tiles/{}');\n}}\n ".format(name, file))
css_file.close()
print("Generated {}".format(css_file.name))

#
# JS Generation
#         

js_file = open("js/data/sprites.js", "a+")
js_file.truncate(0)
js_file.writelines([
GENERATED_WARNING,
"'use strict';\n\n",
"var data = {\n",
"    tiles: [\n"])

SIZE_LISTS = ["buildings", "structures"]
SIZE_LIST_RATIO = {"buildings":60, "structures":60}

def writeSizedObject(directory, file_path, building_name):
    with Image.open(file_path) as img:
        width, height = img.size
        width = (width / SIZE_LIST_RATIO[directory]) * 16
        height = (height / SIZE_LIST_RATIO[directory]) * 16
        js_file.write("        '{}': {{\n".format(building_name))
        js_file.write("            'sprite': '{}',\n".format(file_path))
        js_file.write("            'width': {},\n".format(width))
        js_file.write("            'height': {},\n".format(height))
        js_file.write("        },\n")


for (dirpath, dirnames, filenames) in walk("img/tiles"):
    directory = dirpath[dirpath.rindex('/') + 1:]
    if (directory != "tiles"):
        if (directory in SIZE_LISTS):
    	    js_file.write("    {}: {{\n".format(directory))
        else:
            js_file.write("    {}: [\n".format(directory))
    for file in filenames:
        if file != ".DS_Store":
            name = file[:-4]
            if (directory in SIZE_LISTS):
                writeSizedObject(directory, "{}/{}".format('img/flat-tiles', file), name)
            else:
                js_file.write("        '{}',\n".format(name))
    if (directory in SIZE_LISTS):
        js_file.write("    },\n")
    else:
        js_file.write("    ],\n")

js_file.writelines([
"};\n\n",
"// nodeJS would also like to use this file\n",
"if (typeof module !== 'undefined') {\n",
"    module.exports = data;\n",
"}\n\n"])

js_file.close()
print("Generated {}".format(js_file.name))



#
# JS Map files
#         

js_file = open("js/data/map-sprites.js", "a+")
js_file.truncate(0)
js_file.writelines([
GENERATED_WARNING,
"'use strict';\n\n",
"var maps = [\n"])

for (dirpath, dirnames, filenames) in walk("img/layouts/maps/"):
    for file in sorted(filenames):
        if file != ".DS_Store":
            js_file.write("        '{}',\n".format(file))

js_file.writelines([
"];\n\n",
"// nodeJS would also like to use this file\n",
"if (typeof module !== 'undefined') {\n",
"    module.exports = maps;\n",
"}\n\n"])

js_file.close()
print("Generated {}".format(js_file.name))


#
# Html Generation
# The generated file must be copy and pasted into index.html in the indicated section
#

html_file = open("objects.html", "a+")
html_file.truncate(0)
html_file.write("<!--  \n * START auto-generated section from objects.html \n  --> \n\n")

def writeObjectHtml(data, type, directory, name):
    if (directory == 'maptiles/'):
        pass
    else:
        html_file.write('                                    ')
        html_file.write('<li class="tools {}" data-{}="{}"><div class="link"><i class="sprite-icon {}"></i>{}</div></li>\n'
            .format(type, data, name, name, capitalizeName(name)))

for (dirpath, dirnames, filenames) in walk("img/tiles"):
    directory = dirpath[dirpath.rindex('/') + 1:]
    if (directory == "tiles"):
        continue
    html_file.writelines([
        '                            ',
        '<li class="divider"></li>\n',
        '                            ',
        '<li class="has-dropdown">\n',
        '                            ',
        '    <a href="#" class="show-for-xlarge-up" title="{}">{}</a>\n'.format(directory,capitalizeName(directory)),
        '                            ',
        '    <a href="#" class="hide-for-xlarge-up" title="{}">{}</a>\n'.format(directory,capitalizeName(directory)),
        '                            ',
        '    <ul class="dropdown">\n',
    ])

    subCats = { "flowers": "", "structures": "", "other" : ""}
    num = 0
    for file in sorted(filenames):
        if file != ".DS_Store":
            name = file[:-4]
            if(directory in subCats):
                old = subCats[directory]
                subCats[directory] = file[:file.find('-')]
                if (old != subCats[directory]):
                    if old != "":
                        # spacing so the dropdown list opens at the correct height
                        num += 26
                        html_file.write('                            </ul>\n')
                    html_file.writelines([
                    '                           ',
                    ' <li class="tools parent" data-type="{}"><div class="link"><i class="sprite-icon"></i>{}</div></li>\n'.format(subCats[directory],capitalizeName(subCats[directory])),
                    '                            ',
                    '    <ul class="submenu" style="top:{}px">\n'.format(num),
                    ])
            if (directory in subCats):
                html_file.write('                                    ')
                if (directory in SIZE_LISTS):
                    html_file.write('<li class="tools {}" data-id="{}"><div class="link"><i class="sprite-icon {}"></i>{}</div></li>\n'
                        .format("building", name, name, capitalizeName(name[name.find('-'):])))
                else:
                    html_file.write('<li class="tools {}" data-type="{}"><div class="link"><i class="sprite-icon {}"></i>{}</div></li>\n'
                        .format("brush", name, name, capitalizeName(name[name.find('-'):])))
            elif (directory in SIZE_LISTS):
                writeObjectHtml("id", "building", "", name)
            else:
                writeObjectHtml("type","brush", directory + "/", name)

    if(directory in subCats):
        html_file.write('                                </ul>\n')


    html_file.writelines([
        '                                </ul>\n',
        '                            </li>\n',
    ])
html_file.write("<!--  \n * STOP auto-generated section from objects.html \n  --> \n")
html_file.close()
print("Generated {}".format(html_file.name))



