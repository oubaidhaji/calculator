import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


# initializing the kivy version
kivy.require('2.0.0')

# calling the kv file
Builder.load_file('layout.kv')


class MyContent(Widget):
	def clear(self):
		self.ids._entry.text = '0'
		
	def set_value(self, value):
		the_number = self.ids._entry.text
		if the_number == '0':
			self.ids._entry.text = ''
			self.ids._entry.text = f'{value}'
		else:
			self.ids._entry.text = f'{the_number}{value}'
	
	def set_operation(self, operation):
		num = self.ids._entry.text
		if self.ids._entry.text != '':
			self.ids._entry.text = f'{num}{operation}'
			
	def remove(self):
		num = self.ids._entry.text
		num = num[:-1]
		self.ids._entry.text = num
		
	def equal(self):
		try:
			num = self.ids._entry.text
			result = eval(num)
			if num != '' and num != '0':
				self.ids._entry.text = str(result)
		except:
			self.ids._entry.text = 'Error...'

class MyApp(App):
	def build(self):
		return MyContent()
		
if __name__ == '__main__':
	MyApp().run()