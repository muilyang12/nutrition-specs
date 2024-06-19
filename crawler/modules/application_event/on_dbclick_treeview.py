import webbrowser


def on_dbclick_treeview(event, tree):
    item = tree.identify("item", event.x, event.y)

    if not item:
        return

    url = tree.item(item, "values")[2]
    webbrowser.open(url)
