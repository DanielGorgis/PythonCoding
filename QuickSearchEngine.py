import webbrowser

#Quick python search engine

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path)
#Choice input is read here
Choice = input('What would you like to search for?:  ').strip()

#Adds your Choice to the google.com url
New_Url =("https://www.google.com/search?dcr=0&source=hp&ei=zXcUWtuUIYeD6QThhK24Bw&q="+Choice+"&oq="+Choice+"&gs_l=psy-ab.3..0i131k1j0l9.3294.5654.0.5871.16.10.6.0.0.0.145.641.0j5.7.0....0...1.1.64.psy-ab..3.11.677.0...163.4YXiFNXuTSY")

#opens new browser and inserts choice + url
webbrowser.get(chrome_path).open(New_Url)
