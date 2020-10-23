from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenAction import OpenAction
from subprocess import PIPE, Popen
from xdg import Mime
import os.path

class BalooExtension(Extension):

    def __init__(self):
        super(BalooExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        # call Baloo
        query = event.get_argument()

        if query is None:
            return RenderResultListAction(items)

        # prepare query
        if extension.preferences['tags'] == "Yes":
            query = query.replace("#f", "type:Folder")
            query = query.replace("#img", "type:Image")
            query = query.replace("#doc", "type:Document")
            query = query.replace("#txt", "type:Text")
            query = query.replace("#audio", "type:Audio")
            query = query.replace("#z", "type:Archive")
            query = query.replace("#video", "type:Video")
            query = query.replace("#pres", "type:Presentation")
            query = query.replace("#ss", "type:Spreadsheet")

        # search
        out, err = Popen(["baloosearch", "-l", extension.preferences['limit_results'], query], stdout=PIPE).communicate()
        results = out.splitlines()

        # remove duplicates
        lines = list(dict.fromkeys(results))

        for line in lines:

            # extract path
            path = line.decode("UTF-8")

            # properties
            name = os.path.basename(path)
            mime = Mime.get_type2(path)

            # icon
            icon_path = "%s/%s.svg" % (extension.preferences['icons_path'], str(mime).replace("/", "-"))
            icon = icon_path if os.path.exists(icon_path) else "images/default.svg"

            # items
            item_name = name.replace("&", "&amp;")
            item_description = path.replace("&", "&amp;")

            items.append(ExtensionResultItem(icon=icon,
                                             name=item_name,
                                             description=item_description,
                                             on_enter=OpenAction(path)))

        return RenderResultListAction(items)

if __name__ == '__main__':
    BalooExtension().run()
