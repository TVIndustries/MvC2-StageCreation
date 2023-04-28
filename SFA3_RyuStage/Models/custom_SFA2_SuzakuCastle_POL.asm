; custom_SFA2_SuzakuCastle_POL.asm
; sh4_asm.exe custom_SFA2_SuzakuCastle_POL.asm build/STG02POL.BIN 0x0CEA0000
BEG:
    #data ModelTable 0x00000001 TextureTable Model_000

ModelTable:
    #data Model_000
    #data 0x00000000 ; EndModelTable
    #align16

TextureTable:
    #data 0x0400 0x0040 0x01 0x0D 0x0000 0x0CC00000 0x00000000 ; 0x00, Ends @ 0x0CC20000, Size: 0x00020000
    #data 0x0400 0x0200 0x00 0x0D 0x0000 0x0CC20000 0x00000000 ; 0x01, Ends @ 0x0CD20000, Size: 0x00100000
    #data 0x0000 0x0000 0x00 0x00 0x0000 0x00000000 0x00000000 ; END
    
Model_000:
    #import_raw_data "SFA2_SuzakuCastle_v000.bin"

STG_END:
    #data 0x00000000
    #align16