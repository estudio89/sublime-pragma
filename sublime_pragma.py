import sublime
import sublime_plugin

class SublimePragmaListCommand(sublime_plugin.TextCommand):
    PRAGMA_MARK_SYMBOLS = ["//:", "#:", "<!-- :", "/*:"]
    END_COMMENT_SYMBOLS = ["-->", "*/"]
    LEVEL_SYMBOL = ":"

    def run(self, edit):
        content = self.view.substr(sublime.Region(0, self.view.size() - 1))

        pragma_marks = []
        levels = [0]
        for line_no,line in enumerate(content.split("\n")):
            line = line.strip()
            for symbol in self.PRAGMA_MARK_SYMBOLS:
                if line.startswith(symbol):

                    # Cleaning up line
                    line = line.replace(symbol, "")
                    for end_symbols in self.END_COMMENT_SYMBOLS:
                        line = line.replace(end_symbols, "")

                    line = line.strip()

                    # Counting levels
                    level_symbol_count = 1
                    for c in line:
                        if c == self.LEVEL_SYMBOL:
                            level_symbol_count += 1
                        else:
                            break
                    line = line[(level_symbol_count - 1)::]

                    # Adjusting levels array
                    while len(levels) < level_symbol_count:
                        levels.append(0)

                    while len(levels) > level_symbol_count:
                        levels.pop(-1)

                    levels[-1] += 1

                    print("levels", levels)
                    if len(levels) == 1:
                        level_text = str(levels[0]) + ": "
                    else:
                        level_text = "\t" * (len(levels) - 2) + " \u21B3 "

                    pragma_marks.append(
                        {"name": level_text + line, "line_no": line_no}
                    )


        def on_go_to_line(selected):
            if selected == -1:
                return

            window = sublime.active_window()

            window.open_file(
                self.view.file_name() + ":" + str(pragma_marks[selected]["line_no"] + 1),
                group=window.active_group(),
                flags=sublime.TRANSIENT | sublime.ENCODED_POSITION | sublime.FORCE_GROUP)

        window = sublime.active_window()
        if pragma_marks:
            window.show_quick_panel([pragma["name"] for pragma in pragma_marks], on_select=on_go_to_line, on_highlight=on_go_to_line)
        else:
            self.view.set_status("pragma_marks", "No pragma marks!")
            sublime.set_timeout(lambda : self.view.set_status("pragma_marks", ""), 2000)
