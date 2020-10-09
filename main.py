#!/usr/bin/python3


def avg_setting(indx):

	f = open("settings.txt", "r")

	setting_list = []

	for l in f:
		try:
			a = l[l.index(indx) + len(indx):]
			stting = int(a.split()[0])
			setting_list.append(stting)
		except:
			continue

	if indx == ':':
		print("DPI\t\t", sum(setting_list) / len(setting_list))
	else: 
		print("In-Game\t\t", sum(setting_list) / len(setting_list))



print("Average from: https://www.reddit.com/r/leagueoflegends/comments/i6mzi2/the_longest_list_of_pro_players_mouse_settings/")
avg_setting(':')
avg_setting('/')
