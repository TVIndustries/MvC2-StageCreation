import os
import sys
import shutil


def strip_end(p_text, p_suffix):
    if p_suffix and p_text.endswith(p_suffix):
        return p_text[:-len(p_suffix)]
    return p_text


class ExitError(Exception):
    pass


def exitScript(str):
    print('\n\n')
    prefixStr = ('\n\n ' + '*' * 99) + '\n   ERROR: \n      '
    suffixStr = ('\n\n ' + '*' * 99)
    raise ExitError(prefixStr + str + suffixStr)


texture_mode = 'pvr'
texture_mode_dict = {
    'zbin': 'Textures\\',
    'pvr': 'Textures\\PVRs\\',
}
texture_ext_dict = {
    'pvr': ('.pvr', '.c'),
    'zbin': ('.zbin', '.bin'),
}
texture_mode_dir = texture_mode_dict[texture_mode]
nl = '\n'
s = '    '
spD = s + '#data '
inDir = ''
try:
    inDir = sys.argv[1] + '\\'
    mode = sys.argv[2]
except IndexError:
    exit_str = f"Usage: {sys.argv[0]} <directory> <model_000>"
    exit_str += "\nExample:\n > python .\\MyProject myModel_000.bin"
    raise SystemExit(exit_str)

models_dir = inDir + 'Models\\'
texture_dir = inDir + texture_mode_dir

# Gather Textures
textureList = []
for f_name in os.listdir(texture_dir):
    if f_name.endswith(texture_ext_dict[texture_mode]):
        textureList.append(f_name)
print('\n'.join(textureList), '\n')

textureLocStart = 0
fext = ''
if mode == 'stage':
    textureLocStart = 0x0CC00000
    fext = open(texture_dir + "STG02TEX.BIN", "wb")
elif mode == 'dmtex':
    textureLocStart = 0x0CC00000
    fext = open(texture_dir + "DMXXTEX.BIN", "wb")
elif mode == 'selstg':

    fext = open(texture_dir + "SELSTG.BIN", "wb")

else:
    exitScript('Mode is not \'stage\' or \'selstg\'')
curTexLocBeg = textureLocStart
if texture_mode == 'zbin':
    for curTexture in textureList:
        nameSplit = strip_end(curTexture, '.zbin').split('-')
        texID = nameSplit[0].split('_')[1]
        colFmt = nameSplit[1].split('_')[1]
        texType = nameSplit[2].split('_')[1]
        texWidth = nameSplit[3].split('_')[1]
        texHeight = nameSplit[4].split('_')[1]
        texInfo = (texWidth, texHeight, colFmt, texType)
        width = int(texWidth, 16)
        height = int(texHeight, 16)
        texDataSize = (width * height) << 1
        curTexLocEnd = curTexLocBeg + texDataSize
        texLine = spD + (' '.join(texInfo)) + ' 0x0000 0x%08X 0x00000000 ; %s, Ends @ 0x%08X' \
                  % (curTexLocBeg, texID, curTexLocEnd)
        curTexLocBeg = curTexLocEnd
        print(texLine)

    fext = open(texture_dir + "STG02TEX.BIN", "wb")
    for f in textureList:
        fo = open(os.path.join(texture_dir, f), "rb")
        shutil.copyfileobj(fo, fext)
        fo.close()

elif texture_mode == 'pvr':
    try:
        if mode == 'stage':
            for curTexture in textureList:
                inFile = open(os.path.join(texture_dir, curTexture), "rb")
                pvr_t = int.from_bytes(inFile.read(4), 'big')
                # print('0x%08X' % pvr_t)
                # exit()
                if pvr_t != 0x50565254:
                    inFile.seek(0x14, 0)
                nameSplit = strip_end(curTexture, '.pvr').split('-')
                texID = nameSplit[0].split('_')[1]
                texDataSize = int.from_bytes(inFile.read(4), 'little') - 8
                curTexLocEnd = curTexLocBeg + texDataSize
                colFmt = int.from_bytes(inFile.read(1), 'little')
                texType = int.from_bytes(inFile.read(1), 'little')
                inFile.seek(0x2, 1)
                texHeight = int.from_bytes(inFile.read(2), 'little')
                texWidth = int.from_bytes(inFile.read(2), 'little')
                texInfo = (texWidth, texHeight, colFmt)
                texLine = spD + '0x%04X 0x%04X 0x%02X 0x%02X 0x0000 0x%08X 0x00000000 ; %s, Ends @ 0x%08X, Size: 0x%08X' \
                          % (texHeight, texWidth, colFmt, texType, curTexLocBeg, texID, curTexLocEnd, texDataSize)
                print(texLine)
                curTexLocBeg = curTexLocEnd
                if curTexLocBeg > 0x0CD98000:
                    exitScript(" Data passing 0x0CD98000 memory space.")
                fext.write(inFile.read(texDataSize))
                inFile.close()
            if curTexLocBeg < 0x0CD14000:
                textureSpace = curTexLocBeg - textureLocStart
                if textureSpace <= 0x98000:
                    print('    ; This stage could fit on STG0B, total space used: 0x%05X' % textureSpace)
                else:
                    print('    ; NOT suitable for STG0B, total space used: 0x%05X should be <= 0x98000' % textureSpace)
                remainingSpace = 0x0CD98000 - 0x0CC00000 - textureSpace
                print('    ; Remaining space is 0x%08X' % remainingSpace)
                effeff = 0xFF
                diff = 0x0CD04000 - curTexLocBeg
                for i in range(0, diff):
                    fext.write(effeff.to_bytes(1, 'little'))
        elif mode == 'dmtex':
            for curTexture in textureList:
                inFile = open(os.path.join(texture_dir, curTexture), "rb")
                pvr_t = int.from_bytes(inFile.read(4), 'big')
                # print('0x%08X' % pvr_t)
                # exit()
                if pvr_t != 0x50565254:
                    inFile.seek(0x14, 0)
                nameSplit = strip_end(curTexture, '.pvr').split('-')
                texID = nameSplit[0].split('_')[1]
                texDataSize = int.from_bytes(inFile.read(4), 'little') - 8
                curTexLocEnd = curTexLocBeg + texDataSize
                colFmt = int.from_bytes(inFile.read(1), 'little')
                texType = int.from_bytes(inFile.read(1), 'little')
                inFile.seek(0x2, 1)
                texHeight = int.from_bytes(inFile.read(2), 'little')
                texWidth = int.from_bytes(inFile.read(2), 'little')
                texInfo = (texWidth, texHeight, colFmt)
                texLine = spD + '0x%04X 0x%04X 0x%02X 0x%02X 0x0000 0x%08X 0x00000000 ; %s, Ends @ 0x%08X, Size: 0x%08X' \
                          % (texHeight, texWidth, colFmt, texType, curTexLocBeg, texID, curTexLocEnd, texDataSize)
                print(texLine)
                curTexLocBeg = curTexLocEnd
                # if curTexLocBeg > 0x0CD98000:
                #     exitScript(" Data passing 0x0CD98000 memory space.")
                fext.write(inFile.read(texDataSize))
                inFile.close()
            # if curTexLocBeg < 0x0CD14000:
            #     effeff = 0xFF
            #     diff = 0x0CD04000 - curTexLocBeg
            #     for i in range(0, diff):
            #         fext.write(effeff.to_bytes(1, 'little'))
        elif mode == 'selstg':
            for curTexture in textureList:
                inFile = open(os.path.join(texture_dir, curTexture), "rb")
                pvr_t = int.from_bytes(inFile.read(4), 'big')
                # print('0x%08X' % pvr_t)
                # exit()
                if pvr_t != 0x50565254:
                    inFile.seek(0x14, 0)
                nameSplit = strip_end(curTexture, '.pvr').split('-')
                texID = nameSplit[0].split('_')[1]
                texDataSize = int.from_bytes(inFile.read(4), 'little') - 8
                curTexLocEnd = curTexLocBeg + texDataSize
                colFmt = int.from_bytes(inFile.read(1), 'little')
                texType = int.from_bytes(inFile.read(1), 'little')
                inFile.seek(0x2, 1)
                texHeight = int.from_bytes(inFile.read(2), 'little')
                texWidth = int.from_bytes(inFile.read(2), 'little')
                texInfo = (texWidth, texHeight, colFmt)
                texLine = spD + '0x%04X 0x%04X 0x%02X 0x%02X 0x0000 0x%08X 0x00000000 ; %s, Ends @ 0x%08X, Size: 0x%08X' \
                          % (texHeight, texWidth, colFmt, texType, curTexLocBeg, texID, curTexLocEnd, texDataSize)
                print(texLine)
                curTexLocBeg = curTexLocEnd
                if curTexLocBeg > 0x92000:
                    exitScript(" Data passing 0x92000 memory space.")
                fext.write(inFile.read(texDataSize))
                inFile.close()
            # if curTexLocBeg < 0x0CD14000:
            #     effeff = 0xFF
            #     diff = 0x0CD04000 - curTexLocBeg
            #     for i in range(0, diff):
            #         fext.write(effeff.to_bytes(1, 'little'))
        print(spD + '0x0000 0x0000 0x00 0x00 0x0000 0x00000000 0x00000000 ; END')
        fext.close()
    except ExitError as e:
        fext.close()
        print(" Failed:", e)

