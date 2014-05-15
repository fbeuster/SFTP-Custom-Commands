import re, sublime, sublime_plugin

class SyncDownTabsCommand(sublime_plugin.WindowCommand):
	def run(self):

		# current window
		win = self.window

		# number of views in window
		vs = len(win.views())

		# current view
		vc = win.active_view()

		for v in win.views():
			# switch view
			win.focus_view(v)

			# only sync sftp files
			name = v.file_name()
			if name != None:
				if re.match('.*sublime-sftp-browse.*', name):
					win.run_command('sftp_sync_down')

		# select init view
		win.focus_view(vc)

class SyncDownWindowsCommand(sublime_plugin.WindowCommand):
	def run(self):

		# current window and view
		cWin = self.window
		cView = cWin.active_view()

		for win in sublime.windows():
			for v in win.views():
				# switch view
				win.focus_view(v)

				# only sync sftp files
				name = v.file_name()
				if name != None:
					if re.match('.*sublime-sftp-browse.*', name):
						win.run_command('sftp_sync_down')

		# select init view
		cWin.focus_view(cView)
