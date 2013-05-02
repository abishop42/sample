require 'rubygems'
require 'selenium-webdriver'


def google_search(term,browser)
	puts "google_search"
	google = "www.google.com.au"
	results = []
	begin
		browser.get google
		sleep 3
	# 	browser.text_field(:id,"gbqfq").set search_term
	# 	puts "google search term set -> #{search_term}"
	# 	sleep 5
	# 	@browser.button(:id,"gbqfb").click
	# 	puts "google search term button clicked"
	# 	sleep 20
	# 	count = @browser.divs(:id,"ires")[0].lis.count
	# 	while count > 0
	# 		pos = count - 1
	# 		results << @browser.divs(:id,"ires")[0].lis[pos].link.href
	# 		count = pos
	# 	end
	# rescue Watir::Exception::UnknownObjectException
	# 	puts "something busted therefore given up on this search"
	rescue => e
	 	puts "i have not sure what I was todo therefore i am back"
	end
	results
end

def bing_search(term,browser)
	puts "bing_search"
	bing = "www.bing.com"
	results = []
	puts browser.current_url
	begin
	# 	bing = "www.bing.com"
	# 	puts "going to #{bing}"
		browser.get bing
		sleep 3
	# 	browser.text_field(:id,"sb_form_q").set search_term
	# 	puts "bing search term set -> #{search_term}"
	# 	sleep 5
	# 	@browser.button(:id,"sb_form_go").click
	# 	puts "bing search term button clicked"
	# 	sleep 20
	# 	puts @browser.divs(:id,"results").count
	# 	count = @browser.divs(:id,"results").uls.count
	# 	puts "results counted #{count}"
	# 	while count > 0
	# 		pos = count - 1
	# 		results << @browser.divs(:id,"wg0")[0].uls[pos].link.href
	# 		count = pos
	# 	end
	# rescue Watir::Exception::UnknownObjectException => e
	# 	puts "something busted therefore given up on this search"
	rescue => e
	 	puts "somthing has happend, returning to you regular scheduled program"
	end
	results
end

class Browser_Test
	
	attr_accessor :browser, :search_engines
  	
  	def initialize(t)
		@browser = Selenium::WebDriver.for t
		@search_engines = {}
	end
	
	def add_engine(name, function)
		@search_engines[name] = function
	end

	def search(term,engine="google")
		@search_engines[engine].call(term,@browser)
	end

	def visit(url)
		begin
			puts "going to #{url}"
			@browser.goto url
			sleep 15	
		rescue Selenium::WebDriver::Error::WevbDriverError => e
			puts "I could not find, therefore I look for something else"
		rescue => e
			puts "i have waited too long therefore I give up"			
		end
	end

	def close()
		@browser.close
	end
end

a = Browser_Test.new (:ie)

a.add_engine("google",method(:google_search))
a.add_engine("bing",method(:bing_search))

a.search("www.nba.com","google")
a.search("www.nba.com","bing")