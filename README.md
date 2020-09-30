# Baloo extension for ULauncher

This extension search for files in the Baloo indexes (on KDE/Plasma) for instant results.

![alt text](https://github.com/briceio/ulauncher-baloo/blob/master/overview.png?raw=true)

## Usage

**The default trigger keyword is "?".**

The query syntax is the one offered by Baloo.

For example, to search for all the files/folders containing "draft", type "? draft".

## Index setup

To benefit from this extension you have to check that baloo is enabled (balooctl) and that your indexes are correctly setup.

This can be done two ways:
- Using Plasma general settings (sub settings Search / File Search)
- Using balooctl (https://community.kde.org/Baloo)

## Extension settings

### Keyword

Change the search keyword trigger. 

Default is "?".

### Limits results

Override the limit results of ULauncher for the results on this extension. 

Default is 10.

### Icons path

The icons path to use in the search results. You have to define a path where the MIME-types icons of your theme are kept. Use the 64x64 icons for better visual quality.

For eg. MIME-type icons are named: "application-x-blender.svg" or "text-css.svg". 

Default is: /usr/share/icons/breath2-dark/mimetypes/64

### Simplify queries

> Work in progress...

If enabled, it reduces the size of the query for faster typing. For eg. it allows you to replace the "type:" parameter of your query to "t:" to search for files, folder or documents. So instead of having to type "type:folder" you can type "t:folder".