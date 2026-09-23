import curses
def spill(terminal):
    x = 0
    y = 0
    emoji = ":)"
    while True:
        terminal.clear()
        terminal.addstr(y, x, emoji)
        terminal.refresh()
        høyde, bredde = terminal.getmaxyx()
        bokstav = terminal.getch()
        if bokstav == ord("q"):
            break
        elif bokstav == ord("w"):
            y = max(0, y - 1)
        elif bokstav == ord("s"):
            y = min(høyde - len(emoji), y + 1)
        elif bokstav == ord("a"):
            x = max(0, x - 1)
        elif bokstav == ord("d"):
            x = min(bredde - len(emoji), x + 1)
        elif bokstav == ord(" "):
            if emoji == ":)":
                emoji = ":("
            else:
                emoji = ":)"
curses.wrapper(spill)


# 1.
# wasd flytter smilefjeset rundt

# space gjør om emojien til og fra smil/sur fjes

# q avslutter program

# 2.
# if-testene sjekker input og utfører det som passer

# while løkken lar spillet fortsette helt til q er tastet

# min max brukes til å sjekke hva som er størst/minst av hvor figuren vil gå og grensene til spillebrettet slik at figuren holdes innenfor

# terminal.addstr printer emojien rett sted

# terminal.getch gir deg input character når du trykker på en knapp på tastaturet
