    import os
    env = os.environ#using the os library to output on the terminal
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))#checking if the user can import all this stuff to run the program
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)#make the terminal window parameters as global
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)#open the terminal window
            cr = ioctl_GWINSZ(fd)
            os.close(fd)#close the windows and the interactive session
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))#get certain lines from the user on where to start

    return int(cr[1]), int(cr[0])


