Title: Swap Alt and Windows key in Windows
Date: 2014-08-25
Category: Reisen
Tags: computer, windows
Slug: 2014-08-alt-swap-windows

I use VirtualBox on Mac OS. Windows guest, Mac OS host. On the Mac, the
keyboard layout is a bit different: While on the PC the three first keys in the
last row on the keyboard are Ctrl, Windows and Alt, the Mac has Ctrl, Alt and
Command. From the key code perspective, Command and Windows are the same.

The problem is now that the Windows guest gets the key codes, i.e. Alt and
Windows are swapped. Of course the label stays, the same, but if you type
blind, this doesn't matter. So to use Alt+Tab (to switch between different
windows) one needs to press the second key, not the third key. Maybe some
people like that behavior, but I don't. There are [feature
requests](https://www.virtualbox.org/ticket/3640), but VirtualBox developers
don't want to implement it.

So I decided to look for a solution inside the VM. There are many tools in
Windows to swap keys, but most of them are way too overloaded. Searching around
in the web, I found a much simpler solution which consists only of adding a
value in the registry.

There's a so-called _Scan-code mapper for keyboards_ described in the [MSDN
documentation](https://docs.microsoft.com/de-de/windows-hardware/drivers/hid/keyboard-and-mouse-class-drivers#Scan_code_mapper_for_keyboards).
All you need to do is to add a value called
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout\Scancode
Map` with following value:

```
00 00 00 00  00 00 00 00 
03 00 00 00  38 00 5b e0
5b e0 38 00  00 00 00 00
```

After that, just reboot. No need to install tools, no autostart. If you want to
get rid of the behavior, just delete the registry key and you're done.
