# pesterquest-modsuite v0.6.0
Tools for modifying and extending pesterquest, and adding your own routes
WIP tools for adding your own routes to pesterquest without breaking the base game or needing a standalone engine!

Design goals:

- Cross-platform (Win/Mac/Linux)
- Easy to write and distribute fan volumes
- Hyper-simple for users to play fan volumes
- Mix-and-match: Put all the fan volumes you want and play routes without conflicts

![Example menu](./doc/2019-11-04_22_02_41-Pesterquest.png)

![Example animation](./doc/pq-ms-2.gif)

## Technical notes:

This does not overwrite any game files and should be compatable with all future updates!
The only content this overrides is the main menu to add a menu option. (Here, just a plain `> ` for now.)
You cannot use any of this to pirate pesterquest. 

## Guide for users:

Download this repository, put the fan volumes you want in the `src/custom_volumes` folder, and run `launcher.py` with a recent version of Python.

## Guide for developers:

Incomplete, please see the demo packages in `src/custom_volumes/`.

It's basically the same as extending ren'py using the base game, with a few exceptions for the package manager:
- Each subfolder in the `custom_volumes` folder is a **package**.
- Each package can have any number of **volumes**, or **routes**. These are the icons that appear on the selection page, and they take you to labels in the code.
- You hook your route into the main menu by making sure you've done the following:
    - Your package has a meta.json file that identifies each volume
    - Your source code has a line like `label {{package_entrypoint}}_vid:` where `vid` is the volume ID
- Source files in `{package}/*.rpy` are copied to `{pesterquest}/game/custom_vol_{package_id}_*.rpy`
- Assets in `{package}/assets` are copied to `{pesterquest}/game/custom_assets_{package_id}/`
- Assets in `{package}/assets_common` are copied to `{pesterquest}/game/custom_assets/`
- For each route/volume, you should have a `volumeselect_{tileid}_idle.png` and `volumeselect_{tileid}_small.png` image for the character select screen in its assets folder.

Please see the implementation in `launcher.py` and the demo route for more details.
Updates and contributions to this guide, as well as suggestions for logic rework are all very much appreciated. 

## Example

To demonstrate the simplicity of this system, the vriska mod, in its entirety, is less than 100 lines.

That's all you need to do for setup! Now, just start writing!

l33t hacker notes:
- The system data is loaded first, so any custom volume content can replace it. You can use this to reskin the menu and other system assets. 
- launcher.py is a preprocess that, among other features, runs a simple substitution based on subtable.json *on your whole script*. 
