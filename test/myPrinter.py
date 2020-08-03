from escpos.printer import File
printer = File(devfile='/dev/usb/lp0')
printer.text("سبسلبلبلل\n")
printer.text("some text\n")
printer.text("some text\n")
printer.text("سبلبلباال\n")

# printer.set(codepage='pc864')
printer.profile.media['width']['pixels'] = 575
printer.image("images/logo-text-small.png", center=True)
# printer.image("images/logo-text-small.png")
# printer.set(align=u'center')
printer.text("Far" + "\n\n")
# printer.text(total_price + " Toman" + "\n")
printer.qr('total_price', size=8, center=True)
# printer.qr(str(self.total_price), size=8)
# printer.text(mobile_number + "\n")
printer.text("farazist.ir" + "\n")
# printer.text(datetime)
printer.cut()