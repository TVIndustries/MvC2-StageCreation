; SFA3_RyuStage_v000.asm
; sh4_asm.exe SFA3_RyuStage_v000.asm SFA3_RyuStage_v000.bin 0x00

; Main_Header_SFA3_RyuStage_v000:
    #data 0x00000001    ;  Obj Format
    #data 0x00000003    ;  Flags
    #data 0x00000000    ;  Centroid X
    #data 0x00000000    ;  Centroid Y
    #data 0x00000000    ;  Centroid Z
    #data 0x49A1C0FE    ;  Radius?

; SFA3_RyuStage_Sunset_Header:
    #data 0x8000002C    ; Mesh Param [Param/Flags]?
    #data 0x82000000    ; [Param/Flags]
    #data 0x9488047B    ; [Param/Flags]
    #data 0x08000000    ; [Param/Flags]
    #data 0x00000000    ; Centroid X [Float]
    #data 0x00000000    ; Centroid Y [Float]
    #data 0x00000000    ; Centroid Z [Float]
    #data 0x48A1C0FE    ; Radius     [Float]
    #data 0x00000002    ; TextureID  [UINT-8]
    #data 0xFFFFFFFF    ; TexHandle
    #data 0x3F800000    ; ?????????
    #data 0x3F800000    ; Base Alpha [Float]
    #data 0x3F800000    ; Base Red   [Float]
    #data 0x3F800000    ; Base Green [Float]
    #data 0x3F800000    ; Base Blue  [Float]
    #data 0x00000000    ; Offs Alpha [Float]
    #data 0x00000000    ; Offs Red   [Float]
    #data 0x00000000    ; Offs Green [Float]
    #data 0x00000000    ; Offs Blue  [Float]
; SFA3_RyuStage_Sunset_Data:
    #module "include/SFA3_RyuStage_Sunset_00.asm"

; SFA3_RyuStage_MG_Header:
    #data 0x8200002C    ; Mesh Param [Param/Flags]?
    #data 0x82000000    ; [Param/Flags]
    #data 0x9480047D    ; [Param/Flags]
    #data 0x00000000    ; [Param/Flags]
    #data 0x00000000    ; Centroid X [Float]
    #data 0x00000000    ; Centroid Y [Float]
    #data 0x00000000    ; Centroid Z [Float]
    #data 0x48A1C0FE    ; Radius     [Float]
    #data 0x00000001    ; TextureID  [UINT-8]
    #data 0xFFFFFFFF    ; TexHandle
    #data 0x3F800000    ; ?????????
    #data 0x3F800000    ; Base Alpha [Float]
    #data 0x3F800000    ; Base Red   [Float]
    #data 0x3F800000    ; Base Green [Float]
    #data 0x3F800000    ; Base Blue  [Float]
    #data 0x00000000    ; Offs Alpha [Float]
    #data 0x00000000    ; Offs Red   [Float]
    #data 0x00000000    ; Offs Green [Float]
    #data 0x00000000    ; Offs Blue  [Float]
; SFA3_RyuStage_MG_Stuff_Data:
    #module "include/SFA3_RyuStage_MG_00.asm"

; SFA3_RyuStage_Floor_Header:
    #data 0x8200002C    ; Mesh Param [Param/Flags]?
    #data 0x82000000    ; [Param/Flags]
    #data 0x9480047D    ; [Param/Flags]
    #data 0x00000000    ; [Param/Flags]
    #data 0x00000000    ; Centroid X [Float]
    #data 0x00000000    ; Centroid Y [Float]
    #data 0x00000000    ; Centroid Z [Float]
    #data 0x48A1C0FE    ; Radius     [Float]
    #data 0x00000000    ; TextureID  [UINT-8]
    #data 0xFFFFFFFF    ; TexHandle
    #data 0x3F800000    ; ?????????
    #data 0x3F800000    ; Base Alpha [Float]
    #data 0x3F800000    ; Base Red   [Float]
    #data 0x3F800000    ; Base Green [Float]
    #data 0x3F800000    ; Base Blue  [Float]
    #data 0x00000000    ; Offs Alpha [Float]
    #data 0x00000000    ; Offs Red   [Float]
    #data 0x00000000    ; Offs Green [Float]
    #data 0x00000000    ; Offs Blue  [Float]
; SFA3_RyuStage_MG_Floor_Data:
    #module "include/SFA3_RyuStage_Floor_00.asm"

; SFA3_RyuStage_v000_End: 
    #data 0x00000000
    #data 0x00000024
