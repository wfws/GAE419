import webapp2
import time
import os 
import db_defs
from google.appengine.ext import ndb
from jinja2 import Environment, PackageLoader
#from django.http import HttpResponse
#import jinja2
#code adapted from CS496 week 2 lectures 
	
#from jinja2 documentation
env = Environment(loader=PackageLoader('main', 'templates'))

template_variables = {}  

def render(self, template, template_variables={}):
		template = env.get_template(template)
		self.response.write(template.render(template_variables))

def set_temp_vals(self):
	template_variables['items'] = [{'name': x.name, 'key': x.key.id()} for x in db_defs.Item.query().fetch()]
	#template_variables['categories'] = [{'name': x.name, 'key': x.key.id()} for x in db_defs.Category.query().fetch()]
	#template_variables['businesses'] = [{'name': x.name, 'key': x.key.id()} for x in db_defs.Business.query().fetch()]
	return template_variables 
	
class MainPage(webapp2.RequestHandler):
	template_variables = {}  
   
	
	def get(self): 
		template_variables = set_temp_vals(self)
		render(self, 'business.html', template_variables)
		return
		
			
	def post(self):
		new_bus = db_defs.Business()
		new_bus.name = self.request.get('name')
		new_bus.phone = self.request.get('phone')
		new_bus.address = self.request.get('address')
		new_bus.website = self.request.get('website')
		
		items = self.request.get_all('add_items[]')

		if items: 
		#for each item being added, append its Item object to the list of items
			
			for it in items: 
				item_key = ndb.Key(db_defs.Item, int(it))
				new_bus.items.append(item_key)

		bus_key = new_bus.put() 
		
		if items: 
		#for each item being added, append its Item object to the list of items
			
			for i in items: 
				it_key = ndb.Key(db_defs.Item, int(i))					
				add_item = it_key.get() 
				add_item.businesses.append(bus_key)
				add_item.put()
				
		render(self, 'success.html',{'message': 'Success: Saved results for ' + str(add_item) + ' to the database', 'return': '/add_business'})
