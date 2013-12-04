import easywatch
import sh


def handler(event_type, src_path):
    print event_type, src_path 
    if event_type == "modified":
        sh.make()

easywatch.watch("src", handler)
