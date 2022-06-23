import tkinter as tk
import sys
import subprocess
import platform
# import importlib
import os

VersionNo = "1.03"



class Diy_Upgrade(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master, height=669, width=969)
		self.entry = tk.Entry(self)
		self.entry.focus()
		self.title="Primo Ager DIY upgrade 1.5"
		toolbar = tk.Frame(self)
		toolbar.pack(side="top", fill="x")


		b0 = tk.Button(self, text="0. Welcome ", command=self.step0)
		b1 = tk.Button(self, text="  1. Init  ", command=self.step1)
		b2 = tk.Button(self, text="2. GetFiles", command=self.step2)
		b3 = tk.Button(self, text="   3. USB  ", command=self.step3)
		b4 = tk.Button(self, text=" 4. Flash  ", command=self.step4)
		b5 = tk.Button(self, text=" 5. Check  ", command=self.step5)

		b0.pack(in_=toolbar, side="left")
		b1.pack(in_=toolbar, side="left")
		b2.pack(in_=toolbar, side="left")
		b3.pack(in_=toolbar, side="left")
		b4.pack(in_=toolbar, side="left")
		b5.pack(in_=toolbar, side="left")

		self.text = tk.Text(self, wrap="word")
		self.text.pack(side="top", fill="both", expand=True)
		self.text.tag_configure("stderr", foreground="#b22222")
		self.text.tag_configure("stdout", foreground="#009900")

		sys.stdout = TextRedirector(self.text, "stdout")
		sys.stderr = TextRedirector(self.text, "stderr")

		# b1["state"] = "disabled"
		# b2["state"] = "disabled"
		# b3["state"] = "disabled"
		# b4["state"] = "disabled"

	def step0(self):
		# self.tk.b0["state"]="disabled"
		# self.children("b0")["state"]="disabled"
		print ("welcome...")
		print ("this simple program made by: Miles, 2022-06-08 (c)")
		print ("i will guide you to do the DIY upgrade, on Mac/Win...")
		print (" ")
		print ("First, create a folder, name it as 'primoager_1.51' on your desktop")
		print ("                                    or anywhere convenient for you.")
		print ("and place me, this executing file as the ONLY file in the above folder")

		print ("current working directory:  " + os.getcwd() )
		print ("Then, click the buttons above in sequence... ")

		print (" ")
		print (" ")
		print ("=================================================================== done, step 0")



	def step1(self):
		exit_code_1 = subprocess.check_call([sys.executable, "-m", "pip", "install", "wget"])
		if (exit_code_1==0):
			print("install tools: wget ... done!")
		else:
			sys.stderr.write("cannot install wget")

		exit_code_2 = subprocess.check_call([sys.executable, "-m", "pip", "install", "esptool"])
		if (exit_code_2==0):
			print("install tools: esptool ... done!")
		else:
			sys.stderr.write("cannot install esptool")

		exit_code_3 = subprocess.check_call([sys.executable, "-m", "pip", "install", "download"])
		if (exit_code_1==0):
			print("install tools: download ... done!")
		else:
			sys.stderr.write("cannot install download")


		if (exit_code_1==0 and exit_code_2==0 and exit_code_3==0):
			print("step 1 done, you may proceed to step 2.")
			print("step 2 will download required files, ")
			print("it may take one minute or some, depends on your internet connection")
			print ("=================================================================== done, step 1")
		else:
			sys.stderr.write("Some errors, cannot get some required components")
			sys.stderr.write("please check your internet connection and try again.")
			sys.stderr.write("until you see the words 'done, step 1' ")


	# create this bar_progress method which is invoked automatically from wget
	def bar_progress(self, current, total, width=80):
		progress_message = "Downloading: %d%% [%d / %d] bytes " % (current / total * 100, current, total)
	#     # Don't use print() as it will print in new line every time.
		sys.stdout.write("\r\n" + progress_message)
	# #     sys.stdout.flush()

	def step2(self):

		my_os = platform.system()
		if (my_os == "Windows"):
			import ssl
			ssl._create_default_https_context = ssl._create_unverified_context
			import wget

			try:
				print("start downloading:primoager-v1.51.bin --------------------------------------")
				print ("... ")
				wget.download("https://github.com/miles-hong/primo-ager/raw/main/primoager-v1.51.bin", "primoager-v1.51.bin", bar=self.bar_progress)
				print ("... ")
				print("DONE downloading:primoager-v1.51.bin --------------------------------------")
				print (" ")
				print (" ")
			except:
				sys.stderr.write("cannot use wget to download primoager-v1.51.bin\n")

			try:
				print("start downloading:primoager-1.5-display-v1.02.tft --------------------------------------")
				print ("... ")
				wget.download("https://github.com/miles-hong/primo-ager/raw/main/primoager-1.5-display-v1.02.tft", "primoager-1.5-display-v1.02.tft", bar=self.bar_progress)
				print ("... ")
				print("DONE downloading:primoager-1.5-display-v1.02.tft ---------------------------")
				print (" ")
				print (" ")
			except:
				sys.stderr.write("cannot use wget to download primoager-1.5-display-v1.02.tft\n")

			try:
				print("start downloading USB driver for Windows: -----------------------------------")
				print ("...")
				wget.download("https://www.silabs.com/documents/public/software/CP210x_Windows_Drivers.zip", "CP210x_Windows_Drivers.zip" , bar=self.bar_progress)
				print ("...")
				print("DONE downloading: CP210x_Windows_Drivers.zip -----------------------------------")
			except:
				sys.stderr.write("cannot use wget to download the driver for OS: " + my_os + "\n")


			print (" ")
			print (" ")
			print (" ")

			print ("=================================================================== done, step 2")

		if (my_os == "Darwin"):
			try:
				# testing for Mac
				# subprocess.check_call([sys.executable, "-m", "pip", "install", "certifi"])
				import ssl
				ssl._create_default_https_context = ssl._create_unverified_context

				import download

				try:
					print("start downloading:primoager-v1.51.bin --------------------------------------")
					print ("... ")
					download.download("https://github.com/miles-hong/primo-ager/raw/main/primoager-v1.51.bin", os.getcwd() + "/primoager-v1.51.bin")
					print ("... ")
					print("DONE downloading:primoager-v1.51.bin --------------------------------------")
					print (" ")
					print (" ")
				except:
					sys.stderr.write("cannot use download to download primoager-v1.51.bin\n")

				try:
					print("start downloading:primoager-1.5-display-v1.02.tft --------------------------------------")
					print ("... ")
					download.download("https://github.com/miles-hong/primo-ager/raw/main/primoager-1.5-display-v1.02.tft",  os.getcwd() + "/primoager-1.5-display-v1.02.tft")
					print ("... ")
					print("DONE downloading:primoager-1.5-display-v1.02.tft ---------------------------")
					print (" ")
					print (" ")
				except:
					sys.stderr.write("cannot use download to download primoager-1.5-display-v1.02.tft\n")

				try:
					print("start downloading USB driver for Mac: -----------------------------------")
					print ("...")
					download.download("https://www.silabs.com/documents/public/software/Mac_OSX_VCP_Driver.zip", os.getcwd() + "/Mac_OSX_VCP_Driver.zip")
					print ("...")
					print("DONE downloading: Mac_OSX_VCP_Driver.zip -----------------------------------")
				except:
					sys.stderr.write("cannot use download to download primoager-1.5-display-v1.02.tft\n")
			except:
				sys.stderr.write("error before downloading files, cannot import ssl or download!!! \n")





	def step3(self):
		print (" ")
		print (" ")
		print (" ")
		print ("Please go the folder, ")
		my_os = platform.system()
		if (my_os == "Windows"):
			print(" go to the folder, double click  'CP210x_Windows_Drivers.zip'")
			print (" extract and install the USB driver")

		if (my_os == "Darwin"):
			print(" go to the folder, double click  'Mac_OSX_VCP_Driver.zip'")
			print (" extract and run 'SiLabsUSBDriverDisk.dmg'")

		print (" ")
		print (" ")
		print (" follow the steps to install the USB/UART driver")
		print (" ")

		print ("... ")
		print ("... ")
		print ("... ")
		print ("After the driver was installed, connect an USB cable to the CPU ")
		print ("Note: the USB cable must be a DATA cable, ")
		print ("      NOT a power-charging-only cable.")
		print (" ")
		print (" ")

		print ("=============================================== if that is done, go to next step")
		print (" ")
		print (" ")
		print ("We are ready to flash the CPU,")
		print ("Please note: the flashing process may take about 60 seconds,")
		print ("")
		print ("click the button 4.Flash and wait...")

	def step4(self):

		try:
			import esptool
		except ImportError:
			sys.stderr.write('import error caught, cannot import esptool')
			subprocess.check_call([sys.executable, "-m", "pip", "install", "esptool"])
		finally:
			import esptool

		# detect and list usb com port ready, if not quit and show error

		try:
			# print(esptool.detect_chip())

			# ports = esptool.get_port_list()
			# for port in ports:
			#     print(port)

			# subprocess.check_call([sys.executable, "-m", "esptool", "--port COM3 --baud 115200 --before default_reset --after hard_reset --chip esp32 write_flash 0x10000 ./primoager-v1.51.bin"])
			my_os = platform.system()
			if (my_os == "Windows"):
				subprocess.check_call([sys.executable, "-m", "esptool", "write_flash", "0x10000", "./primoager-v1.51.bin"])
			if (my_os == "Darwin"):
				subprocess.check_call([sys.executable, "-m", "esptool", "write_flash", "0x10000", os.getcwd() + "/primoager-v1.51.bin"])

			# esptool.py --port /dev/cu.usbserial-AC01WJQX -b 921600 write_flash 0x10000 ./my_firmware.bin
			# esptool.write_flash("0x10000 primoager-v1.51.bin", esp=any)
			# -p (PORT) -b 460800 --before default_reset --after hard_reset --chip esp32  write_flash --flash_mode dio --flash_size detect --flash_freq 40m  0x10000 primoager-v1.51.bin
			print ("=========================================================flash done, step 4")
		except:
			sys.stderr.write("Cannot flash the CPU")


	def step5(self):
		print("please check you monitor display.")
		print("if all steps completed, please flash your display monitor program.")

	def print_stderr(self):
		sys.stderr.write("this is stderr\n")

class TextRedirector(object):
	def __init__(self, widget, tag="stdout"):
		self.widget = widget
		self.tag = tag

	def write(self, str):
		self.widget.configure(state="normal")
		self.widget.insert("end", str, (self.tag,))
		self.widget.configure(state="disabled")
		self.widget.see("end")

	# def flush(self):
	#     self.widget.delete(1.0)



# =======================================================================================================
# =======================================================================================================
# =======================================================================================================
# =======================================================================================================
# =======================================================================================================

root = tk.Tk()

my_os = platform.system()
if (my_os == "Windows"):
	root.title("Primo Ager DIY Upgrade 1.51 --- for Windows --- //miles " + VersionNo)
if (my_os == "Darwin"):
	root.title("Primo Ager DIY Upgrade 1.51 --- for Mac --- //miles " + VersionNo)

Diy_Upgrade(root).pack(expand=True, fill='both')
root.mainloop()

