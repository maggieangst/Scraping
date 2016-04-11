import csv, mechanize
from bs4 import BeautifulSoup

# Get the output file ready
#output = open('output.csv', 'w')
#writer = csv.writer(output)

# Get the HTML of the page
br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx')


# Put this up here so you can loop over it
option_values = ['001', '003', '005', '007', '009', '011', '013', '015', '017', '019', '021', '023', '025', '027', '029', '031', '033', '035', '037', '039', '041', '043', '045', '047', '049', '051', '053', '055', '057', '059', '061', '063', '065', '067', '069', '071', '073', '075', '077', '079', '081', '083', '085', '087', '089', '091', '093', '095', '097', '099', '101', '095A', '103', '105', '107', '109', '111', '113', '115', '117', '119', '121', '123', '125', '127', '129', '131', '133', '135', '137', '139', '141', '143', '145', '147', '149', '151', '153', '155', '157', '159', '161', '163', '165', '167', '169', '171', '173', '175', '177', '179', '181', '195', '197', '199', '201', '203', '205', '183','185', '187', '189', '510', '188', '207','209', '211', '213', '215', '217', '219', '221', '223', '225', '227', '229']
i = 0
# You want to loop over that option_values list and basically execute almost the exact code we already went over
# in class. Difference is, you're executing it multiple times -- one for each county.

# Here's this, to refresh your memory: https://github.com/cjdd3b/advanced-data-journalism/blob/master/2016-03-21-week10/results.py#L9-L29
for value in option_values: 
    br.select_form(nr=0) # Same as example
    br.form['ctl00$MainContent$cboElectionNames'] = ['750003566'] # Same as example

    # Now do the same here with the county dropdown and set it to the value of the loop iteration.
    br.form['ctl00$MainContent$cboCounty'] = [option_values[i]]

    # You got this part right. That's the button you want to submit. Again, similar to class example.
    br.submit('ctl00$MainContent$btnCountyChange')
    html = br.response().read() # Same as example

    # ... and so on. You can draw pretty heavily from the class example to get you most of the way beyond this.
    # Just remember you're executing your code within the loop because you want it to execute once for each county.

    # Transform the HTML into a BeautifulSoup object
    soup = BeautifulSoup(html, "html.parser")


    # Find the main table using both the "align" and "class" attributes
    main_table = soup.find('table',
        {'id': 'MainContent_dgrdResults'}
    )

    # Now get the data from each table row
    for row in main_table.find_all('tr'):
        data = [cell.text for cell in row.find_all('td')]
        
        if data:
            if data[0] in ['Hillary Clinton', 'Ted Cruz', 'Donald J. Trump', 'Bernie Sanders', 'John R. Kasich']: 
                print option_values[i], data[0], data[3]
         #writer.writerow(data)
    
    i=i+1
    if i == len(option_values):
        break

