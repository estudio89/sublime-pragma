# Sublime Pragma Marks Plugin

## Installation

Clone this repository and create a symlink to it in your Sublime Text packages directory. To figure out your Sublime Text packages directory location, simply open Sublime Text and go to **Sublime Text** >> **Preferences** >> **Browse Packages**. Then, create the symlink via the command line:

`ln -s <path/to/cloned/directory/> <path/to/sublime/packages/directory/>`

## How to

To add a pragma mark, simply add a comment with a colon right after the comment start symbol:

- `#: This is a python pragma mark`
- `<!-- : This is an HTML pragma mark -->`
- `//: This is a javascript pragma mark`
- `/*: This is a CSS pragma mark */`

To view all pragma marks, open the command pallete and run the command `List pragma marks`. You can also assign a shortcut by going to **Sublime Text** >> **Preferences** >> **Key bindings** and adding the following:

`{ "keys": ["ctrl+alt+p"], "command": "sublime_pragma_list"},`

You can modify the shortcut keys as you wish.