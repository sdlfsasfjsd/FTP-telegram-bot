import os

#API ID & API Hash -----> my.telegram.org
api_id = 8002628
api_hash = '0805d45de882197f254fd11b3105409a'

#Bot Token -----> @BotFather
token = '7212730524:AAHxOd47ZxyVwuMZA8ce9N4CreDoH1wXnSA'

#Session Name -----> optional
session_name = 'FTP_Manager'


#The robot admin (the person who can give orders to the robot.) -----> @myidbot
admins = [1133933758]

# Chat id to send technical logs
dev = -1001593556762

# When a file is sent to the bot, first that file is downloaded from the Telegram repository and stored in the bot's server.
# Here you need to specify its temporary storage path
# For example, I set the bot to save the downloaded file in the current path (the path where config.py file is located).
dl_path = os.path.abspath(os.getcwd()) + '/'


# The upload path where we give FTP access to the bot.
ftp_path = '/home/bicvgast/madflixes.xyz/madflix2x7'

# The files are temporarily downloaded after they are on the bot server. They are uploaded to another host through FTP.
# Here we have to give FTP access to the bot.
ftp_ip = '37.27.108.55'
ftp_username = 'madflix2x7@madflixes.xyz'
ftp_password = '@Yasir24x7'
ftp_domain = 'ftp.madflixes.xyz'
