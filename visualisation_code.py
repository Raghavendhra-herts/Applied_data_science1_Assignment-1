# required libraries which are required to run this code
import pandas as pd
import matplotlib.pyplot as plt


def prepare_data():
    '''
    Here, I'm reading the .csv file data through pd.read_csv()'
    I have downloaded the dataset in .csv format with file-name "IDA_Credits___Grants_for_Haiti__Colombia__Mexico__Peru__Chile.csv"
    
    '''
    # read the .csv file through pd.read_csv()
    data = pd.read_csv("IDA_Credits___Grants_for_Haiti__Colombia__Mexico__Peru__Chile.csv")
    # removing the unnecessary columns from dataset, to make data tabel more readable
    data = data.drop(columns=['Credit Number', 'Country Code', 'Credit Status', 'Service Charge Rate', 'Project ID', 'Undisbursed Amount', 'Due to IDA', 'Exchange Adjustment', "Borrower's Obligation", 'Sold 3rd Party', 'Repaid 3rd Party',
                   "Due 3rd Party", "Credits Held", "Agreement Signing Date", "Last Disbursement Date" ,"Effective Date (Most Recent)", "Board Approval Date", "First Repayment Date", "Last Repayment Date"])
    # print(data)      # reading data
    # print(len(data.columns))   # getting total length of columns
    return data



def show_line_plot(data):
    """
    In this function, I'm plotting line graph with the choosen data set.
    I have chosen IDA Credits & Grants for Haiti, Colombia, Mexico, Peru, Chile.
    Here IDA is **International Development Association**
    """
    # reading & displaying data in a tabel(rows & columns)
    df = pd.DataFrame(data)
    # assigning necessary columns to a new variable 
    get_y_axis = ['Original Principal Amount','Disbursed Amount','Repaid to IDA', 'Cancelled Amount']
    # changing "Closed Date (Most Recent)" column data-type of Object to to_datetime()
    df['Closed Date (Most Recent)'] = pd.to_datetime(df['Closed Date (Most Recent)'], infer_datetime_format=True)
    # generating line plot
    df.plot(x = 'Closed Date (Most Recent)', y = get_y_axis, style="-o",  figsize = (19,9))
    # display the title on line-graph using plt.title()
    plt.title("IDA Statement of Credits and Grants '$' ", fontsize=18)
    # display the label on x-axis using plt.xlabel()
    plt.xlabel("Years with credits", fontsize=18)
    # display the label on y-axis using plt.ylabel()
    plt.ylabel("Funds/Amount by World Bank Group '$'", fontsize=18)
    # legends used to show the labels (indicates the lines and each color represents different label)
    plt.legend()
    # saving the plot image in a .png format
    plt.savefig("line_plot.png")
    # to show/display the graph using plt.show() 
    plt.show()
    


def show_bar_plot(data):
    '''
    In this function, I'm plotting bar graph with the choosen data set.
    to show the results in bar graph I have chosen few coulmns from the dataset,
    
    '''
    # choosen and fetching columns from the dataset to represent the results in bar graph
    data = {
        'Closed Date (Most Recent)': data['Closed Date (Most Recent)'],
        'Original Principal Amount' : data['Original Principal Amount'],
        'Disbursed Amount': data['Disbursed Amount'],
        'Repaid to IDA': data['Repaid to IDA'],
        'Cancelled Amount': data['Cancelled Amount']      
            }
    # reading & displaying data in a tabel(rows & columns)
    df = pd.DataFrame(data)
    # changing "Closed Date (Most Recent)" column data-type of Object to to_datetime()
    df['Closed Date (Most Recent)'] = pd.to_datetime(df['Closed Date (Most Recent)'], infer_datetime_format=True)
    # sorting the years to represent them in x-axis on bar plot
    df.sort_values('Closed Date (Most Recent)').plot.bar(x ='Closed Date (Most Recent)', figsize = (20, 10))
    # display the title on bar-graph using plt.title()
    plt.title("IDA Statement of Credits and Grants '$'" , fontsize=18)
    # display the label on x-axis using plt.xlabel()
    plt.xlabel("Years with closing dates", fontsize=18)
    # display the label on y-axis using plt.ylabel()
    plt.ylabel("Funds/Amount by World Bank Group '$'", fontsize=18)
    # Setting the data limit range for the better representation of the graph
    plt.xlim(20.5,40.5)
    # saving the plot image in a .png format
    plt.savefig("bar_plot.png")
    # to show/display the graph using plt.show() 
    plt.show()



def show_hist_graph(data):
    '''
    
    In this function, I'm plotting histogram graph with the choosen data set.
    to show the results in histogram graph, I am using subplots to show each 
    column data.

    '''
    # reading & displaying data in a tabel(rows & columns)
    df = pd.DataFrame(data)
    # Assigning the figure size
    plt.figure(figsize=(20, 15))
   
    
    # to show the graph in index-1 using subplot
    plt.subplot(2,2,1)
    values, bins, bars = plt.hist(data['Original Principal Amount'], bins = 10, label = 'Original Principal Amount')
    # min and max amount
    print("max:",data['Original Principal Amount'].max(), "\t", "min:",data['Original Principal Amount'].min())
    # using bars in a histogram represents the quantity of data points that fall within that bin
    plt.bar_label(bars, fontsize = 10, color = "green")
    # legends used to show the labels 
    plt.legend()
    # display the title on hist-graph using plt.title()
    plt.title("Principal amount from IDA", fontsize=18)
    # display the label on x-axis using plt.xlabel()
    plt.xlabel("Original principal amount ($)", fontsize=15)
    
    
    # to show the graph in index-2 using subplot
    plt.subplot(2,2,2)
    # using bins to displays numerical data by grouping data into "bins" of equal width.
    # plotting the histogram graph
    values, bins, bars = plt.hist(data['Disbursed Amount'], bins = 10, label = 'Disbursed Amount')
    # min and max amount
    print("max:",data['Disbursed Amount'].max(), "\t", "min:",data['Disbursed Amount'].min())
    # using bars in a histogram represents the quantity of data points that fall within that bin
    plt.bar_label(bars, fontsize = 10, color = "green")
    # legends used to show the labels
    plt.legend()
    # display the title on hist-graph using plt.title()
    plt.title("Amount disbursed from IDA", fontsize=18)
    # display the label on x-axis using plt.xlabel()
    plt.xlabel("Disbursed Amount from IDA ($)", fontsize=15)
    
    
    # to show the graph in index-3 using subplot
    plt.subplot(2,2,3)
    # using bins to displays numerical data by grouping data into "bins" of equal width.
    # plotting the histogram graph
    values, bins, bars = plt.hist(data['Repaid to IDA'], bins = 10, label = 'Repaid to IDA')
    # min and max amount
    print("max:",data['Repaid to IDA'].max(), "\t", "min:",data['Repaid to IDA'].min())
    # using bars in a histogram represents the quantity of data points that fall within that bin
    plt.bar_label(bars, fontsize = 10, color = "green")
    # legends used to show the labels
    plt.legend()
    # display the title on hist-graph using plt.title()
    plt.title("Amount repaid to IDA", fontsize=18)
    # display the label on x-axis using plt.xlabel()
    plt.xlabel("Repaid amount to IDA ($)", fontsize=15)

    
    # to show the graph in index-4 using subplot
    plt.subplot(2,2,4)
    # using bins to displays numerical data by grouping data into "bins" of equal width.
    # plotting the histogram graph
    values, bins, bars = plt.hist(data['Cancelled Amount'], bins = 10, label = 'Cancelled Amount')
    # min and max amount
    print("max:",data['Cancelled Amount'].max(), "\t", "min:",data['Cancelled Amount'].min())
    # using bars in a histogram represents the quantity of data points that fall within that bin
    plt.bar_label(bars, fontsize = 10, color = "green")
    # legends used to show the labels
    plt.legend()
    # display the title on hist-graph using plt.title()
    plt.title("cancelled amount to IDA", fontsize=18)
    # display the label on x-axis using plt.xlabel()
    plt.xlabel("Amount cancelled by IDA($)", fontsize=15)
    
    # displaying common title on sub-plots
    plt.suptitle("IDA Statement of Credits and Grants '$'" , fontsize=18)
    # saving the plot image in a .png format
    plt.savefig('hist2.png')
    # to show/display the graph using plt.show() 
    plt.show()
    
    
# calling main function here
if __name__ == "__main__":
    print("Reading the data")
    # calling the prepare_data function and return the data by the function
    data = prepare_data()
    print("calling line plot function..!")
    # calling the show_line_plot function for line graph by passing the data attribute
    show_line_plot(data)
    print("calling bar plot function..!")
    # calling the show_bar_plot function for bar graph by passing the data attribute
    show_bar_plot(data)
    print("calling histogram plot function..!")
    # calling the show_hist_graph function for histgram graph by passing the data attribute
    show_hist_graph(data)