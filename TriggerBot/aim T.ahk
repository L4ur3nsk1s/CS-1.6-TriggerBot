c::
    MouseGetPos, MouseX, MouseY
    PixelGetColor, c, %MouseX%, %MouseY%

    MsgBox, %c%


    i::

        Loop {
            PixelSearch, Px, Py, 679, 380, 687, 388, 0xA40A04, 1, Fast
            PixelSearch, Px, Py, 679, 380, 687, 388, 0x950804, 1, Fast
            PixelSearch, Px, Py, 679, 380, 687, 388, 0x730404, 1, Fast
            PixelSearch, Px, Py, 679, 380, 687, 388, 0x870404, 1, Fast
            PixelSearch, Px, Py, 679, 380, 687, 388, 0x510504, 1, Fast
            PixelSearch, Px, Py, 679, 380, 687, 388, 0x760404, 1, Fast
            PixelSearch, Px, Py, 679, 380, 687, 388, 0x660404, 1, Fast
            PixelSearch, Px, Py, 679, 380, 687, 388, 0x370404, 1, Fast
            PixelSearch, Px, Py, 679, 380, 687, 388, 0x280404, 1, Fast
            PixelSearch, Px, Py, 679, 380, 687, 388, 0x530404, 1, Fast




            if (ErrorLevel = 0) {


                click left
            }
        }
        k::reload
