from rubpy import Client, filters, utils
from rubpy.types import Updates
from requests import get,post
from asyncio import run
from random import choice,randint
from time import sleep
#from PIL import Image
import time
import datetime
from datetime import datetime

NameGroup = "♡•<-𝙼𝚘𝚛𝙵𝚒𝚗->•♡"
admins = open("admins.txt","r",encoding='utf-8').read().split("\n")
black_list = open("black.txt","r",encoding='utf-8').read().split("\n")
member = ''
bot = Client("Robi")
@bot.on_message_updates()
async def updates(client: Updates):
	guid = client.author_guid
	text = client.text
	target = client.object_guid
	message_id = client.message_id
	print(text)
	if client.author_guid in black_list:
		message_id = client.message_id
		await bot.delete_messages(target,message_id)
		print("Dell-Sokot")
	if text.startswith("G @"):
		try:
			me_id = client.message_id
			username = text.split("G @")[1]
			guid_group = "g0FWDPn0f516cafb0592e01ce28666ff"
			result = await bot.get_object_by_username(username)
			result = result.to_dict.get('user').get('user_guid')
			await bot.add_group_members(guid_group, result)
			jj = await client.reply("با موفقیت افزوده شد.")
			ll = jj['message_update']['message_id']
			await bot.delete_messages(guid_group, me_id)
			await bot.delete_messages(guid_group, ll)
		except:
			await client.reply("انجام نشد.")
	if text.startswith("Ch @"):
		try:
			me_id = client.message_id
			username = text.split("Ch @")[1]
			guid_group = "c0CZyKd0be130a0170146e3c44313b4a"
			result = await bot.get_object_by_username(username)
			result = result.to_dict.get('user').get('user_guid')
			await bot.add_channel_members(guid_group, result)
			jj = await client.reply("با موفقیت افزوده شد.")
			ll = jj['message_update']['message_id']
			await bot.delete_messages(guid_group, me_id)
			await bot.delete_messages(guid_group, ll)
		except:
			await client.reply("انجام نشد.")
	elif client.text != None and client.text == 'ربات' or client.text == 'بات' or client.text == 'باط' or client.text == 'رباط'or client.text == 'روبی':
		R = ["جانم🥹","چیه😒","ای بابا😑","بچه جون بسع😂🚶‍♂","ولم کن دیگه نمیخوامت😣","همش گوشته..!"]
		R = list(R)
		await client.reply(choice(R))
		print("send-bot")
	elif client.text.startswith("دعوت @") or client.text.startswith("دعوت @"):
		result = await bot.get_group_admin_members(client.object_guid)
		in_chat_members = result.in_chat_members
		a = 0
		for i in in_chat_members:
			admins = i["member_guid"]
			if guid in admins:
				group_guid = client.object_guid
				mess_id = client.message_id
				username = client.text.split("دعوت @")[1]
				info = await bot.get_info(guid)
				info = info.to_dict
				namey = info.get('user').get('first_name')
				user_guidd = info.get('user').get('user_guid')
				result = await bot.get_object_by_username(username)
				result = result.to_dict
				user_guid = result.get('user').get('user_guid')
				name = result.get('user').get('first_name')
				group_title = await bot.get_group_info(group_guid)
				group_title = group_title['group']['group_title']
				link = await bot.get_group_link(group_guid)
				link = link["join_link"]
				message = await bot.send_message(user_guid, ".")
				mess = f"""سلام عزیزم🫠🫰✨

شما از طرف {namey} 👐

به گروه {NameGroup} دعوت شده اید🫶🤞

برای پیوستن روی لینک زیر بزنید 🫴❣

{link}"""
				message_id = message['message_update']['message_id']
				await bot.edit_message(user_guid, message_id, mess)
				await client.reply(f'''دعوت به کاربر:
@{username}

ارسال شد.🤒👐''')
				time.sleep(0.5)
				await bot.delete_messages(group_guid, mess_id)
				print("Ok-invite")
	elif text.startswith("دعوت به کانال"):
		id = client["message"]["reply_to_message_id"]
		link = await bot.get_messages_by_id(target, id)
		link = link["messages"][0]["text"]
		a = await bot.join_group(link)
		a = a.to_dict
		a = a["group"]["group_guid"]
		result = await bot.get_group_all_members(a)
		in_chat_members = result.in_chat_members
		n = 0
		for i in in_chat_members:
			member = i["member_guid"]
			n += 1
			time.sleep(4)
			await bot.send_message(member, '''‐ب‍‌ه‍‌ ن‍‌ام خ‍‌ال‍‌ق چ‍‌ش‍‌اش✌️🧿‐
•
‐ت‍‌ا ب‍‌ه‍‌ ق‍‌وان‍‌ی‍‌ن دل‍‌م🥂🫧‐
•
‐م‍‌ی‍‌ری‍‌م ب‍‌ال‍‌ا م‍‌ث ن‍‌رخ دل‍‌ار💸🤍‐
•

•
‐ل‍‌ف خ‍‌ز ش‍‌ده‍‌ ب‍‌ی‍‌ب ب‍‌ودن‍‌ت ق‍‌ش‍‌ن‍‌گت‍‌ره:))🫶🏻🩷‐
https://rubika.ir/joinc/DDFIGDJE0CSWDKTELIHMLFEVDTIFSAVO''')
		await client.reply(f"Number Send: {n}")
	elif text.startswith("یک عضو گروه را ترک کرد."):
		await client.reply("کراشت رل بزنه انشاالله")
		#message_id = client.message_id
#		await bot.delete_messages(target, message_id)
	elif text.startswith("بن") or text.startswith("ریم"):
		if client.reply_message_id != None:
			try:
				result = await bot.get_messages_by_id(client.object_guid, [client.reply_message_id])
				result = result.to_dict.get('messages')[0]
				if not result.get('author_object_guid') in admins:
					result = await client.ban_member(client.object_guid, result.get('author_object_guid'))
					await client.reply('کاربر مورد نظر از گروه حذف شد.')
					print("Ok-Ban")
				else:
					await client.reply('کاربر مورد نظر در گروه ادمین است.')
			except IndexError:
					await client.reply('ظاهرا پیامی که روی آن ریپلای کرده اید پاک شده است.')
	elif text.startswith("ارز"):
		res = get("http://entelbot.iapp.ir/Api/money.php").json()["result"]
		dolar = res["dolar"]
		euro = res["euro"]
		pond = res["pond"]
		derham = res["derham"]
		lir = res["lir"]
		await client.reply(f'''دلار --» {dolar}
یورو --» {euro}
پوند --» {pond}
درهم --» {derham}
لیر --» {lir}

**آخرین قیمت**''')
	elif text == "یک عضو از طریق لینک به گروه افزوده شد.":
		timr = datetime.now().strftime("%H:%M:%S")
		result = await  bot.get_group_info(client.object_guid)
		result = result.to_dict
		result = result.get("group")
		name = result.get("group_title")
		await client.reply(f'''سلام خوشگله 😘🌹 
 • به گـروه {name} خیـلی خوش اومدی 😍❤️ 
لطفا قوانین رو رعایت کن .

ساعت ورود کاربر: {timr}

 💎 برای مشاهده قوانین کافیه کلمه (قوانین) رو ارسال کنی!''')

	elif text.startswith('بیو'):
		bio = get("https://api.codebazan.ir/bio/").text
		await client.reply(bio)
		print("send-bio")
	elif text.startswith("دستورات") or text.startswith("راهنما"):
		message_id = client.message_id
		rules = open("dastorat.txt","r").read()
		await bot.send_message(target, rules)
		print("ok-dastorat")
	elif text.startswith("ویسکال") or text.startswith("کال"):
		a = await bot.create_group_voice_chat(target)
		voice_chat_id = a["group_voice_chat_update"]["voice_chat_id"]
		v = voice_chat_id.join_voice_chat()
		print(v)
	elif text.startswith("پخش"):
		a = await bot.voice_chat_player(target, "12.mp3")
		print(a)
		await client.reply("موسیقی با موفقیت در ویسکال در حال پخش است.")
	elif text.startswith("سکوت"):
		result = await bot.get_group_admin_members(client.object_guid)
		in_chat_members = result.in_chat_members
		a = 0
		for i in in_chat_members:
			admins = i["member_guid"]
		if guid in admins:
			message_id = client.message_id
			info = await bot.get_messages_by_id(target,message_id)
			info = info["messages"][0]["reply_to_message_id"]
			x = await bot.get_messages_by_id(target,info)
			x = x['messages'][0]['author_object_guid']
			open("black.txt","a").write('\n' + x)
			msg = '**کاربر به لیست سکوت اضافه شد**'
			await client.reply(msg)
			print("ok-sokot")
	elif text.startswith("حذف سکوت"):
		result = await bot.get_group_admin_members(client.object_guid)
		in_chat_members = result.in_chat_members
		for i in in_chat_members:
			admins = i["member_guid"]
		if guid in admins:
			x = ''
			open("black.txt","w",encoding='utf-8').write(str(x))
			msg = '**کاربر از لیست سکوت حذف شد**'
			await client.reply(msg)
			print("no-sokot")
		return 1
	elif text.startswith("Add to group"):
		id = client["message"]["reply_to_message_id"]
		link = await bot.get_messages_by_id(target, id)
		link = link["messages"][0]["text"]
		a = await bot.join_group(link)
		a = a.to_dict
		a = a["group"]["group_guid"]
		result = await bot.get_group_all_members(a)
		in_chat_members = result.in_chat_members
		n = 0
		for i in in_chat_members:
			member = i["member_guid"]
			n += 1
			time.sleep(4)
			await bot.add_group_members(target, member)
		await client.reply(f"Number Group: {n}")
		#await bot.leave_group(a)
	elif text.startswith("Add to channel"):
		guid = await bot.join_channel_by_link("https://rubika.ir/joinc/DDFIGDJE0CSWDKTELIHMLFEVDTIFSAVO")
		guid = guid.to_dict
		tar = guid["channel"]["channel_guid"]
		id = client["message"]["reply_to_message_id"]
		link = await bot.get_messages_by_id(target, id)
		link = link["messages"][0]["text"]
		a = await bot.join_group(link)
		a = a.to_dict
		a = a["group"]["group_guid"]
		result = await bot.get_group_all_members(a)
		in_chat_members = result.in_chat_members
		n = 0
		for i in in_chat_members:
			member = i["member_guid"]
			n += 1
			time.sleep(4)
			await bot.add_channel_members(tar, member)
		await client.reply(f"Number Group: {n}")
	elif text.startswith("والیپر"):
		wall = get("https://api3.haji-api.ir/majid/fun/wallpaper/random?license=wZ1eu25ybu3iaJmLByvDiC9ZkgLKkLJZLkINfS")
		with open("Walliper.jpg","wb") as file:
			file.write(wall.content)
		await bot.send_photo(client.object_guid, "Walliper.jpg", None, client.message_id)
		print("send-walliper")
	elif text.startswith("انگیزشی"):
		angizeshi = get("http://haji-api.ir/angizeshi?license=wZ1eu25ybu3iaJmLByvDiC9ZkgLKkLJZLkINfS").text
		await client.reply(angizeshi)
	elif text.startswith("ترجمه"):
		id = client["message"]["reply_to_message_id"]
		text = await bot.get_messages_by_id(target, id)
		text = text["messages"][0]["text"]
		type = client.text.split("ترجمه")[1]
		trans = get(f"https://haji-api.ir/translate?from=fa&to={type}&text={text}&license=wZ1eu25ybu3iaJmLByvDiC9ZkgLKkLJZLkINfS").text
		await client.reply(trans)
	elif text.startswith("https://rubika.ir/post"):
		result = get(f"https://api3.haji-api.ir/majid/social/rubino/download?url={text}&license=wZ1eu25ybu3iaJmLByvDiC9ZkgLKkLJZLkINfS").json()
		result = result["result"]
		url = result["url"]
		await client.reply_video_message(url)
		await client.reply("پست شما")
	elif text.startswith("تصویر"):
		type = text.split("تصویر")[1]
		result = get(f"https://api3.haji-api.ir/majid/ai/image/dalle3?p={type}&license=wZ1eu25ybu3iaJmLByvDiC9ZkgLKkLJZLkINfS").json()
		num = range(0, 30)
		result = result["result"][0]
		await client.reply_photo(i)
	elif text.startswith("QR"):
		type = text.split("QR")[1]
		result = get(f"https://api3.haji-api.ir/majid/tools/qrcode?text={type}&size=500&license=wZ1eu25ybu3iaJmLByvDiC9ZkgLKkLJZLkINfS").json()
		url = result["result"]
		await client.reply_photo(url)
	elif text.startswith("بارکد"):
		type = text.split("بارکد")[1]
		result = get(f"https://haji-api.ir/barcode?text={type}&license=wZ1eu25ybu3iaJmLByvDiC9ZkgLKkLJZLkINfS")
		with open("barcode.jpg","wb") as file:
			file.write(result.content)
		await client.reply_photo("barcode.jpg")
	elif text.startswith("ارسال"):
		username = text.split()[1]
		result = await bot.get_messages_by_id(client.object_guid, [client.reply_message_id])
		result = result.to_dict.get('messages')[0]
		message = result.get('text')
		result = await bot.get_object_by_username(username)
		result = result.to_dict
		user_guid = result.get('user').get('user_guid')
		name = result.get('user').get('first_name')
		cap = f'''سلام خوشگله شما یه پیام ناشناس دارید🤪🤞

پیام:
||{message}||
'''
		await bot.send_message(user_guid, cap)
		await bot.send_message(user_guid, "خوشحال میشم اگه بلاک نکنید🥲🤍🫶")
		await client.reply(f'''پیام ناشناس ارسال شد به
[{name}]({user_guid})
''')
	elif text.startswith("-"):
		mt = text.split("-")[1]
		await client.reply("""کاربرگرامی لطفا کمی صبر کنید . . .""")
		try:
			res = get(f"https://api3.haji-api.ir/lic/gpt/4?q={mt}&license=wZ1eu25ybu3iaJmLByvDiC9ZkgLKkLJZLkINfS").json()["result"]
			await client.reply(res)
		except:
			await client.reply("""[❗]مشکل در پاسخ به سوال شما""")
	elif text.startswith("موسیقی"):
		message_id = client.message_id
		type = text.split("موسیقی")[1]
		text = type.replace(" ", "+")
		print(text)
		result = get(f"https://info-benyamin.liara.run/search_music?query={text}").json()
		result = result["mp3_link"]
		print(result)
		await bot.send_music(target, result, message_id)
	elif text.startswith("Music"):
		type = text.split("Music")[1]
		type = type.replace(" ", "+")
		result = get(f"https://api-free.ir/api/sr-music/?text={type}").json()
		result = result["result"]
		title = result["title"]
		song = result["song"]
		print(result)
		await bot.send_music(target, song, title, message_id)
			
	
bot.run()