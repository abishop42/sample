require 'rubygems'
require 'selenium-webdriver'


def google_search(term,browser)
	puts "google_search"
	google = "www.google.com.au"
	results = []
	begin
		browser.get google
		sleep 5
	 	#browser.find_element(:id,"gbqfq").sendKeys(term)
	 	#sleep 5
	 	#@browser.find_element(:id,"gbqfb").click
	 	#sleep 5
	 	#count = @browser.find_element(:id,"ires")[0].lis.count
	 	#while count > 0
	 	#	pos = count - 1
	 	#	results << @browser.find_element(:id,"ires")[0].lis[pos].link.href
	 	#	count = pos
	 	#end
	rescue => e
	 	puts "i have gone wrong"
	 	puts e.backtrace
	end
	results
end

def bing_search(term,browser)
	puts "bing_search"
	bing = "www.bing.com"
	results = []
	begin
		browser.get bing
		sleep 5
	 	#browser.find_element(:id,"sb_form_q").sendKeys(term)
	 	#sleep 5
	 	#@browser.find_element(:id,"sb_form_go").click
	 	#sleep 5
	 	#puts @browser.find_element(:id,"results").count
	 	#count = @browser.find_element(:id,"results").uls.count
	 	#puts "results counted #{count}"
	 	#while count > 0
	 	#	pos = count - 1
	 	#	results << @browser.find_element(:id,"wg0")[0].uls[pos].link.href
	 	#	count = pos
	 	#end
	rescue => e
	 	puts "somthing has happend"
	 	puts e.backtrace
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
			@browser.get url
			sleep 15	
		rescue Selenium::WebDriver::Error::WevbDriverError => e
			puts "I could not find, therefore I look for something else"
			puts e.backtrace
		rescue => e
			puts "i have waited too long therefore I give up"			
		end
	end

	def close()
		@browser.close
	end
end

a = Browser_Test.new (:firefox)

a.add_engine("google",method(:google_search))
a.add_engine("bing",method(:bing_search))

a.visit("http://www.theage.com.au")
a.search("http://www.nba.com","google")
a.search("http://www.nba.com","bing")