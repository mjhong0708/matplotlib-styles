# matplotlib-styles
My collection of matplotlib stylesheets


## Installation (Linux, macOS)

To install, run following commands in shell.

```console
user@example.com:~$ cd ~/.config/matplotlib # if does not exist, create one.
user@example.com:~/.config/matplotlib$ git clone https://github.com/mjhong0708/matplotlib-styles.git
user@example.com:~/.config/matplotlib$ cd matplotlib-styles
user@example.com:~/.config/matplotlib/matplotlib-styles$ python install.py
```

## Usage

Simply add `plt.style.use("{style_name}")` in your plotting script. See `examples` for example usage.

The stylesheet uses Arial as default font, so you may need to install it first. Otherwise, matplotlib will use fallback fonts.
