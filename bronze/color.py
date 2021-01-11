from colorama import Back, Fore


stars = Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX
red = Back.LIGHTRED_EX
white = Back.LIGHTWHITE_EX

reset = Back.RESET + Fore.RESET

print(stars + '* ٭ * ٭ * ٭ * ٭ * ٭ *' + reset + red)
print(stars + '* ٭ * ٭ * ٭ * ٭ * ٭ *' + reset + white)
print(stars + '* ٭ * ٭ * ٭ * ٭ * ٭ *' + reset + red)
print(stars + '* ٭ * ٭ * ٭ * ٭ * ٭ *' + reset + white)
print(stars + '* ٭ * ٭ * ٭ * ٭ * ٭ *' + reset + red)
print(stars + '* ٭ * ٭ * ٭ * ٭ * ٭ *' + reset + white)
print(stars + '*   *   *   *   *   *' + reset + red)


print(white + '                                          ' + reset)
print(red + '                                          ' + reset)
print(white + '                                          ' + reset)
print(red + '                                          ' + reset)
print(white + '                                          ' + reset)
print(red + '                                           ' + reset)

stars = Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX
red = Back.LIGHTRED_EX
white = Back.LIGHTWHITE_EX

reset = Back.RESET + Fore.RESET
print('╔═════════════════════════════════════════╗')
print(stars + '* ٭ * ٭ * ٭ * ٭ * ٭ *' + reset  + '║' + red)
print(stars + '* ٭ * ٭ * ٭ * ٭ * ٭ *' + reset + '║' + white, end='\n')
print(stars + '* ٭ * ٭ * ٭ * ٭ * ٭ *' + reset  + '║' + red)
print(stars + '* ٭ * ٭ * ٭ * ٭ * ٭ *' + reset + '║' + white)
print(stars + '* ٭ * ٭ * ٭ * ٭ * ٭ *' + reset  + '║' + red)
print(stars + '* ٭ * ٭ * ٭ * ٭ * ٭ *' + reset + '║' + white)
print(reset + '║'+stars + '*   *   *   *   *   *' + reset + red)

print(white + '\x1b[49m\x1b[39m║\x1b[107m                                          \x1b[49m\x1b[39m║' + reset)
print(red + '\x1b[49m\x1b[39m║\x1b[101m                                          \x1b[49m\x1b[39m║' + reset)
print(white + '\x1b[49m\x1b[39m║\x1b[107m                                          \x1b[49m\x1b[39m║' + reset)
print(red + '\x1b[49m\x1b[39m║\x1b[101m                                          \x1b[49m\x1b[39m║' + reset)
print(white + '\x1b[49m\x1b[39m║\x1b[107m                                          \x1b[49m\x1b[39m║' + reset)
print(red + '\x1b[49m\x1b[39m║\x1b[101m                                          \x1b[49m\x1b[39m║' + reset)
print('╚══════════════════════════════════════════╝')
