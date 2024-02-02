Title: Use an Apple keyboard on Linux
Date: 2014-10-31
Category: Computer
Tags: computer, apple, linux
Slug: 2014-10-apple-keyboard

I have to admit that I use a Mac at home as my primary workstation. I also like
the Apple keyboard (the one with a cable). That keyboard is hard-wired for
Macs, which means that on a PC

- one cannot use the function keys without pressing _fn_
- the tilde (in the English/International layout) is not left of the _1 key_ but
  right of the left _Shift_ key
- _Alt_ and _Windows_ are swapped (if you type blindly and ignore the labels).

The good news is that Linux comes with a `hid_apple` kernel driver which can
“fix“ that issues. By default, that driver doesn't change the behavior, you
have to set some kernel parameters. On recent Linux distributions, all you have
to do is to create a file `/etc/modprobe.d/hid-apple.conf` with following
contents:

```
options hid_apple fnmode=2 iso_layout=0 swap_opt_cmd=1
```

When the driver is loaded in initramfs (e.g. you have an encrypted root
partition, so you need to enter your password in the early boot phase), then
you have to re-create the initramfs, e.g. by `mkinitcpio -p linux` on [Arch
Linux](http://www.archlinux.org).
