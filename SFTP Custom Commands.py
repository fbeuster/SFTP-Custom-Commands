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
			if re.match('.*sublime-sftp-browse.*', v.file_name()):
				win.run_command('sftp_sync_down')

		# select init view
		win.focus_view(vc)
