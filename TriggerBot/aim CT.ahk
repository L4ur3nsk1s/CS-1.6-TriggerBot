c::
    MouseGetPos, MouseX, MouseY
    PixelGetColor, c, %MouseX%, %MouseY%

    MsgBox, %c%


o::

    Loop {
        PixelSearch, Px, Py, 679, 380, 687, 388, 0x132849, 1, Fast
        PixelSearch, Px, Py, 679, 380, 687, 388, 0x133CA5, 1, Fast
        PixelSearch, Px, Py, 679, 380, 687, 388, 0x182C52, 1, Fast
        PixelSearch, Px, Py, 679, 380, 687, 388, 0x21385A, 1, Fast
        PixelSearch, Px, Py, 679, 380, 687, 388, 0x05142B, 1, Fast
        PixelSearch, Px, Py, 679, 380, 687, 388, 0x1E52C1, 1, Fast
        PixelSearch, Px, Py, 679, 380, 687, 388, 0x1440A4, 1, Fast
        PixelSearch, Px, Py, 679, 380, 687, 388, 0x0F3688, 1, Fast
        PixelSearch, Px, Py, 679, 380, 687, 388, 0x18345A, 1, Fast
        PixelSearch, Px, Py, 679, 380, 687, 388, 0x0C2C84, 1, Fast
        PixelSearch, Px, Py, 679, 380, 687, 388, 0x123A76, 1, Fast
        PixelSearch, Px, Py, 679, 380, 687, 388, 0x102C52, 1, Fast




        if (ErrorLevel = 0) {


            click left
        }
    }
    k::reload
