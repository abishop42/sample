require 'rubygems'
require 'watir-webdriver'
require 'watir-webdriver-performance'



class Browser_Test
	
	attr_accessor :browser
  	
  	def initialize(t)
		@browser = Watir::Browser.new t
	end
	
	def check_loadtime(url, count)
		results = []
		while count > 0
			@browser.goto url
			results << browser.performance.summary
			count = count - 1 
		end
		results
	end

	def close()
		@browser.close
	end

	#run a search
	#search enginge then phrase
	#return list of links that are results

	def search(term,engine="google")
		results = []
		case engine
			when "google"
				results = google_search term
			when "bing"
				results = bing_search term
			else
				"puts invalid engine"
		end
		results
	end

	def visit(url)
		begin
			puts "going to #{url}"
			@browser.goto url
			sleep 15	
		rescue => e
			puts "something happened,  giving up on search #{url}"			
		end
	end

	def bing_search(search_term)
		results = []
		begin
			bing = "www.bing.com"
			puts "going to #{bing}"
			visit bing
			browser.text_field(:id,"sb_form_q").set search_term
			puts "bing search term set -> #{search_term}"
			sleep 5
			@browser.button(:id,"sb_form_go").click
			puts "bing search term button clicked"
			sleep 20
			puts @browser.divs(:id,"results").count
			count = @browser.divs(:id,"results").uls.count
			puts "results counted #{count}"
			while count > 0
				pos = count - 1
				results << @browser.divs(:id,"wg0")[0].uls[pos].link.href
				count = pos
			end
		rescue Watir::Exception::UnknownObjectException => e
			puts "something busted therefore given up on this search"
		rescue => e
			puts "i have waited too long therefore I give up"
		end
		results
	end

	def google_search(search_term)
		results = []
		begin
			google = "www.google.com.au"
			visit google
			browser.text_field(:id,"gbqfq").set search_term
			puts "google search term set -> #{search_term}"
			sleep 5
			@browser.button(:id,"gbqfb").click
			puts "google search term button clicked"
			sleep 20
			count = @browser.divs(:id,"ires")[0].lis.count
			while count > 0
				pos = count - 1
				results << @browser.divs(:id,"ires")[0].lis[pos].link.href
				count = pos
			end
		rescue Watir::Exception::UnknownObjectException
			puts "something busted therefore given up on this search"
		rescue Timeout::Error
			puts "i have waited too long therefore I give up"
		end
		results
	end

end


def test_runs()
	urls = ["www.google.com.au","www.theage.com.au","www.abc.com.au"]
	browsers = [:ie,:firefox,:chrome]
	rowsers = [:ie]
	results  = []
	browsers.each do |b|
		d = Browser_Test.new(b)
		urls.each do |u|
			res = d.check_loadtime u, 20
			results << {"browser" => b, "url" => u, "results" => res}
		end
		d.close
	end

	results.each do |r|
		puts "======================================"
		puts "browser => #{r["browser"]}"
		puts "url     => #{r["url"]}"
		puts "times   => #{r["results"]}"
	end
end

def write_file(file_name,data)
	w = open(file_name, 'w')
  	data.each do |d|
  		w.write(d)
  		w.write("\n")
  	end
end

def search_runs()
	search = [
		"how not to search for things on the internet","idiots guide to betting on horses","why does it hurt when I fall over",
		"where am I right now","how to write a book","blah blah blah blah", "errorcode 42 => what is the meaning of life",
		"where are all the donut shops in melbourne", "how to pick up chicks without actually picking them up",
		"i am a donut a jelly filled donut","the best donut is a free donut",
		"pie squared is just more pie","tacos tacos tacos","how to play two up", "pago rock", "ahmar rock",
		"the walking dead comics","i have a lovely bunch of coconuts", "why is the killing so dam good",
		"douglas adams","the finder","beer","rugby union","crickect","funny tshirts","garfield","dilbert",
		"how to pick a footy quad","suits","I am a sleep","beer tasting","supernova","the end of the other end",
		"funny funny haha",	"I am a search term also","click me","click without clicking","future weapons",
		"how to do something without actually doing it","101 ways to eat a donut","george carlin","epic fail",
		"look at this search term","fartlek", "define: define", "this is the term I want to search for","what tv shows are worth watching",
		"wacked on scooby snacks","raised fist","pearl jam","meshugga","why cant I see my feet"]
	results = []
	b = Browser_Test.new :ie
	search.each do |s|
		puts  "running search -> #{s}"
		#results = results +  b.search(s,"bing")
		#break
		results = b.search(s,"google")
		results.each do |r|
			b.visit(r)
		end
		
	end
	b.close
end

search_runs