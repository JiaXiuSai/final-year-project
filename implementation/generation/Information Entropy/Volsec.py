import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
import seaborn as sns
import pandas as pd
import scipy.signal
from PIL import Image
import math

from collections import Counter
from matplotlib.colors import LogNorm

sns.set_style("darkgrid")
sns.set_context("poster")

def add_value_labels(ax, thelabels, spacing=5):
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax (matplotlib.axes.Axes): The matplotlib object containing the axes
            of the plot to annotate.
        spacing (int): The distance between the labels and the bars.
    """
    count = 0
    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = thelabels[count]
        count += 1

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va, size=16)                      # Vertically align label differently for
                                        # positive and negative values.

def change_width(ax, new_value) :
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)

def bar_chart(x,y,title,x_label,y_label,top_labels,file_name,show_graph_flag):
    temp_dict = { x_label : x, y_label : y}
    df = pd.DataFrame(temp_dict)
    ax = sns.barplot(x=x_label, y=y_label, data=df)
    ax.set_ylim(top=180)
    ax.set_xticklabels(rotation=90,labels=x)
    add_value_labels(ax,top_labels)
    #ax.set_title(title)
    save_and_show_graph(plt, file_name, show_graph_flag)

def histogram(data,title,x_label,y_label,file_name,show_graph_flag):

    bins = np.linspace(math.ceil(min(data)), 
                    math.floor(max(data)),
                    20) # fixed number of bins

    #fig, ax = plt.subplots()
    #ax.axis([1, 10000, 1, 100000])
    #ax.loglog()
    #ax.set_yscale('log')
    
    plt.xlim([min(data), max(data)])

    plt.hist(data, bins=bins, alpha=0.5)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    save_and_show_graph(plt, file_name, show_graph_flag)

def histogram_log(data,title,x_label,y_label,file_name,show_graph_flag):

    bins = np.linspace(math.ceil(min(data)), 
                    math.floor(max(data)),
                    20) # fixed number of bins

    #bins = np.linspace(0, 10^1, 10,100,1000,10000)
    #plt.yscale('log')
    plt.ylim(1,600000)
    plt.xscale('log')
    #fig, ax = plt.subplots()
    #ax.axis([1, 10000, 1, 100000])
    #ax.loglog()
    #ax.set_yscale('log')
    
    plt.xlim([min(data), max(data)])

    plt.hist(data, bins=np.logspace(np.log10(0.1),np.log10(10000000000000000000)), alpha=0.5)
    plt.xlim(10000000000,10000000000000000000)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    save_and_show_graph(plt, file_name, show_graph_flag)

def histogram_y_log(data,title,x_label,y_label,file_name,show_graph_flag):

    bins = np.linspace(math.ceil(min(data)), 
                    math.floor(max(data)),
                    20) # fixed number of bins

    #bins = np.linspace(0, 10^1, 10,100,1000,10000)
    plt.yscale('log')
    #plt.xscale('log')
    #fig, ax = plt.subplots()
    #ax.axis([1, 10000, 1, 100000])
    #ax.loglog()
    #ax.set_yscale('log')
    
    plt.xlim([0, max(data)])

    plt.hist(data, bins=bins, alpha=0.5)
    plt.ylim(1,10000000)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    save_and_show_graph(plt, file_name, show_graph_flag)

def histogram_small(data,title,x_label,y_label,file_name,show_graph_flag):

    bins = np.linspace(math.ceil(min(data)), 
                    math.floor(max(data)),
                    20) # fixed number of bins

    plt.xlim([min(data), max(data)])

    print(bins)
    plt.hist(data, bins=bins, alpha=0.5)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    save_and_show_graph(plt, file_name, show_graph_flag)

def cat_plot(data,title,x_label,y_label,file_name,show_graph_flag,set_y_max=False,y_max=0,y_min=0):
    #df = pd.DataFrame(data.items(), columns=['pwm', 'value'])

    df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in data.items() ]))
    #df = pd.DataFrame([data], columns=data.keys())
    df = df.stack()
    df.name = "data"
    df = df.reset_index()
    df = df.rename(index=str, columns={"level_0": "set", "level_1": "pwm"})
    sns.set(style="ticks", color_codes=True)
    p_all = df[(df['set']=='all')]
    p_l = df[(df['set']=='l')]
    p_ls = df[(df['set']=='ls')]
    p_ld = df[(df['set']=='ld')]
    p_sd = df[(df['set']=='sd')]
    #ax = sns.scatterplot(x="pwm",y="data",hue="set",style="set",size="set",sizes=(200,200),alpha=0.5,markers=['<','>','^','v','.'],data=df)
    

    ax = sns.pointplot(x="pwm",y="data",hue="set",dodge=.7,size=8,palette=sns.xkcd_palette(['blue','orange','red','black','green']),markers=['<','>','^','v','.'],alpha=0.5,data=df)
    
    lw = ax.lines[0].get_linewidth() # lw of first line
    plt.setp(ax.lines,linewidth=.1)  # set lw for all lines
    #ax = sns.stripplot(x="pwm",y="data",hue="set",jitter=True,dodge=True,size=8,palette=sns.xkcd_palette(['blue','orange','red','black','green']),alpha=0.5,data=df)
    
    #jitter_val = .1
    #marker_size = 8
    #colors = ['blue','yellow','green','red','black']
    #ax_l = sns.stripplot(x="pwm",y="data",hue="set",jitter=jitter_val,dodge=True,size=marker_size,palette=sns.xkcd_palette(['blue']),alpha=0.5,marker='>',data=p_l)
    #ax_ls = sns.stripplot(x="pwm",y="data",hue="set",jitter=jitter_val,dodge=True,size=marker_size,palette=sns.xkcd_palette(['orange']),alpha=0.5,marker='d',data=p_ls)
    #ax_ld =sns.stripplot(x="pwm",y="data",hue="set",jitter=jitter_val,dodge=True,size=marker_size,palette=sns.xkcd_palette(['red']),alpha=0.5,marker='P',data=p_ld)
    #ax_sd = sns.stripplot(x="pwm",y="data",hue="set",jitter=jitter_val,dodge=True,size=marker_size,palette=sns.xkcd_palette(['black']),alpha=0.5,marker='.',data=p_sd)
    #ax = sns.stripplot(x="pwm",y="data",hue="set",jitter=jitter_val,dodge=True,size=marker_size,palette=sns.xkcd_palette(['green']),alpha=0.5,marker='<',data=p_all)

    if set_y_max:
        ax.set(xlabel=x_label, ylabel=y_label, title=title, ylim=(y_min, y_max))
    else:
        ax.set(xlabel=x_label, ylabel=y_label, title=title, ylim=(y_min, None))
    #handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=6)
    save_and_show_graph(plt, file_name, show_graph_flag)

def graph_cdf(list_of_vals, title, x_label, y_label, file_name,
              show_graph_flag):
    """
    Send in a python list of values and we'll make a generic cdf of it
    Args:
        list_of_vals: python list of values (floats) to graph
        title: title of graph to be listed above it
        x_label: label to be displayed on x axis
        y_label: label to be displayed on y axis
        file_name: file to save the graph to
        show_graph_flag: if True, graph will pop up on screen and saved,
            otherwise just saved
    """

    values_array = np.asarray(list_of_vals)
    sorted_vals = np.sort(values_array)
    y_vals = np.arange(len(sorted_vals)) / float(len(sorted_vals))

    data = pd.DataFrame({x_label: sorted_vals, y_label: y_vals})
    plot = make_lmplot(x_label, y_label, data, title)

    save_and_show_graph(plot, file_name, show_graph_flag)


def graph_multi_cdf(id_to_vals, title, legend_title,
                    x_label, y_label, file_name,
                    show_graph_flag):
    """
    Send in a python list of list of values and we'll make a generic cdf of it,
    graphing each list on the same plot
    Args:
        id_to_vals: Dictionary where the values are lists of vals and the key for
            each entry is the identifier of that list which will be used in the legend
        title: title of graph to be listed above it
        legend_title: title of the legend
        x_label: label to be displayed on x axis
        y_label: label to be displayed on y axis
        file_name: file to save the graph to
        show_graph_flag: if True, graph will pop up on screen and saved,
            otherwise just saved
    """
    dfs = dict()
    for vals_id, vals in id_to_vals.items():
        values_array = np.asarray(vals)
        sorted_vals = np.sort(values_array)
        y_vals = np.arange(len(sorted_vals)) / float(len(sorted_vals))

        df = pd.DataFrame({x_label: sorted_vals, y_label: y_vals})
        dfs[vals_id] = df

    markers_array = ['x','s','D','^','o','+','None','X']
    colors = ['b','g','r','c','m','y','navy','olive']
    count = 0
    fig, ax = plt.subplots()
    for df_id, df in dfs.items():
        make_regplot(x_label, y_label, df, ax=ax, markr=markers_array[count], color=colors[count], fit=False, label=df_id, bullet_size=10)
        count += 1

    #fig.suptitle(title, size=20)
    fig.subplots_adjust(top=.9)
    # Shrink current axis by 20%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    if len(id_to_vals) > 6:
        legendheight = 1.30
    elif len(id_to_vals) > 3:
        legendheight = 1.20
    else:
        legendheight = 1.13

    # Put a legend to the right of the current axis
    #legend = ax.legend(loc='upper center',bbox_to_anchor=(0.5,legendheight),ncol= 3)
    legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.21),
          fancybox=True, shadow=True, ncol=3)

    frame = legend.get_frame()
    frame.set_facecolor('white')
    frame.set_edgecolor('gray')

    save_and_show_graph(fig, file_name, show_graph_flag)


def graph_x_vs_y(x_list, y_list, title, x_label, y_label,
                 file_name, show_graph_flag, list_of_tuples=None):
    """
    Send in either list of (x, y) tuples or two separate python lists
    and we'll make a generic x vs y graph of the data
    Args:
        list_of_tuples: TODO: Make optional: CURRENT: if None, skips, if
        passed in, graphs tup[0] vs tup[1]
        x_list: if no list of tuples, these values will be the x values
        for the corresponding y_list values
        y_list: if no list of tuples, these values will be the y values
        for the corresponding x_list values
    """

    if list_of_tuples is not None:
        x_vals = [tup[0] for tup in list_of_tuples]
        y_vals = [tup[1] for tup in list_of_tuples]

        data = pd.DataFrame({x_label: x_vals, y_label: y_vals})
        plot = make_lmplot(x_label, y_label, data, title)
    else:
        if len(x_list) != len(y_list):
            raise ValueError("Length of x and y lists are different! They must be equal.")

        data = pd.DataFrame({x_label: x_list, y_label: y_list})
        plot = make_lmplot(x_label, y_label, data, title)

    save_and_show_graph(plot, file_name, show_graph_flag)


def graph_multi_x_vs_y(id_to_vals, title, legend_title, x_label, y_label,
                       file_name, show_graph_flag):
    """
        Graph multiple datasets of X-Y values onto the same plot with the same
        X and Y labels
    Args:
        id_to_vals: dictionary where the values are a single tuple with the first
            element of X-values and the second element of Y-values, and the key
            is the label for that series. There can be many key-value pairs for
            every relationship you want to plot.
            Example:
                {
                    'Relationship 1': ([1, 2, 3], [4, 5, 6]),
                    'Relationship 2': ([2, ...], [5, ...])
                    ...
                    'Relationship n': ...
                }
        title: title of the plot
        legend_title: title of the legend
        x_label: label for the X axis
        y_label: label for the Y axis
        file_name: file to save the graph to
        show_graph_flag: if True, graph will pop up on screen and saved,
            otherwise just saved
    """

    dfs = dict()
    for vals_id, x_y_vals in id_to_vals.items():
        x_vals, y_vals = x_y_vals[0], x_y_vals[1]

        if len(x_vals) != len(y_vals):
            raise ValueError("Length of x and y lists are different! They must be equal.")
        df = pd.DataFrame({x_label: x_vals, y_label: y_vals})
        dfs[vals_id] = df

    markers_array = ['x','s','D','^','o','+','None','X']
    colors = ['b','g','r','c','m','y','navy','olive']
    count = 0
    fig, ax = plt.subplots()
    for df_id, df in dfs.items():
        make_regplot(x_label, y_label, df, ax=ax, markr=markers_array[count], color=colors[count], fit=False, label=df_id)
        count += 1

    fig.suptitle(title, size=20)
    fig.subplots_adjust(top=.9)
    legend = ax.legend(loc='upper left', title=legend_title, frameon=True)
    frame = legend.get_frame()
    frame.set_facecolor('white')
    frame.set_edgecolor('gray')

    save_and_show_graph(fig, file_name, show_graph_flag)

def replace_nan_values(array):
    col_mean = np.nanmean(array,axis=0)
    inds = np.where(np.isnan(array))
    array[inds]=np.take(col_mean,inds[1])
    return array

def graph_mean_and_conf(data,confidenceIntervals,title,x_label,y_label,file_name,show_graph_flag):
    """
    Given multiple lists of samples taken at a series of times, graph the average along with confidence intervals

    Args:
        data: Dictionary with the name of each set of samples as the key and a list of lists as the value
            Ex: {
                    "Sample1" : [[t1,t2] , [[t1val1,t2val1],[t1val2,t2val2],[t1val3,t2val3]...]]
                    "Sample2" : [[t1,t2] , [[t1val1,t2val1],[t1val2,t2val2],[t1val3,t2val3]...]]
                    ...
                }

        confidenceIntervals: a list of confidence intervals to be displayed on graph - can be single or multiple
            Ex: [50] - show 50% confidence interval
                [50,95] - show both 50% and 95% confidence intervals
        title: title of the plot
        x_label: label for the X axis
        y_label: label for the Y axis
        file_name: file to save the graph to
        show_graph_flag: if True, graph will pop up on screen and saved,
            otherwise just saved
    """

    fig, ax = plt.subplots()
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.set_xlabel(x_label)

    markers_array = ['x','s','D','^','o','+','None','X']
    colors = ['b','g','r','c','m','y','navy','olive']

    count = 0
    for filename, vals in data.items():
        times = vals[0]
        values = vals[1]

        #convert to numpy array
        arr = np.array(values,dtype=np.float)

        #replace nan values with the average value within their local array
        arr = replace_nan_values(arr)
        sns.tsplot(data=arr, ax=ax, time=times,legend=True,color=colors[count],err_style="ci_band",ci=confidenceIntervals)

        count += 1
        if(count > 6):
            count = 0

    save_and_show_graph(fig, file_name, show_graph_flag)

#very strange input data format given that I just convert it
#due to how it was already being passed in - need to update at some point
#this function smooths the data and adds markers
def graph_regplot_golay(data,title,x_label,y_label,file_name,show_graph_flag):
    """
    Given multiple lists of samples taken at a series of times, graph the average along with confidence intervals

    Args:
        data: Dictionary with the name of each set of samples as the key and a list of lists as the value
            Ex: {
                    "Sample1" : [[t1,t2] , [[t1val1,t2val1],[t1val2,t2val2],[t1val3,t2val3]...]]
                    "Sample2" : [[t1,t2] , [[t1val1,t2val1],[t1val2,t2val2],[t1val3,t2val3]...]]
                    ...
                }

        confidenceIntervals: a list of confidence intervals to be displayed on graph - can be single or multiple
            Ex: [50] - show 50% confidence interval
                [50,95] - show both 50% and 95% confidence intervals
        title: title of the plot
        x_label: label for the X axis
        y_label: label for the Y axis
        file_name: file to save the graph to
        show_graph_flag: if True, graph will pop up on screen and saved,
            otherwise just saved
    """

    fig, ax = plt.subplots()
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

    markers_array = ['x','s','D','^','o','+','None','X']
    colors = ['b','g','r','c','m','y','navy','olive']

    count = 0
    for filename, vals in data.items():
        times = vals[0]
        values = vals[1]

        if isinstance(values[0],list):
            #preparing to calculate golay values
            #need to transform data
            y_pregolay = []
            for i in range(0,len(times)):
                y_pregolay.append([])
            for listvals in values:
                for i in range(0,len(times)):
                    y_pregolay[i].append(listvals[i])

            #markers will be at time,average
            y_golay = [sum(l) / float(len(l)) for l in y_pregolay]
            if len(y_golay) > 31:
                y_golay = scipy.signal.savgol_filter(np.asarray(y_golay),31,3)
            else:
                y_golay = scipy.signal.savgol_filter(np.asarray(y_golay),5,3)
        else:
            y_golay = values

        #signal.savgol_filter including negative values - quick fix
        #no neg values in original data as of writing this
        for i in range(0,len(y_golay)):
            if y_golay[i] < 0:
                y_golay[i] = 0

        if len(y_golay) > 10:
            markervalues = y_golay[0::int(len(y_golay)/float(10))]
        else:
            markervalues = y_golay
        if len(times) > 10:
            markertimes = times[0::int(len(times)/float(10))]
        else:
            markertimes = times

        #plot data
        ax.plot(times,y_golay,color=colors[count])
        #plot markers
        sns.regplot(np.asarray(markertimes),np.asarray(markervalues), ax=ax, fit_reg=False, marker=markers_array[count], label=filename,
                    scatter_kws={"s": 200}, color=colors[count])

        count += 1
        if(count > 6):
            count = 0

    #fig.suptitle(title, size=20)
    fig.subplots_adjust(top=.9)
    # Shrink current axis by 20%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    if len(data) > 6:
        legendheight = 1.30
    elif len(data) > 3:
        legendheight = 1.20
    else:
        legendheight = 1.13

    # Put a legend to the right of the current axis
    legend = ax.legend(loc='upper center',bbox_to_anchor=(0.5,legendheight), ncol= 3)

    frame = legend.get_frame()
    frame.set_facecolor('white')
    frame.set_edgecolor('gray')

    save_and_show_graph(fig, file_name, show_graph_flag)

def graph_multi_bar(values,xlabels,title,y_label,file_name, show_graph_flag,rotate,barwidth=0.27,fontsize=20):
    """
    Graph multiple bar charts on the same graph

    Args:
        values: dictionary with legend label : bar vales as list
            Ex: {
                    'file1' : [23,45,13],
                    'file2' : [420,23,1000]
                }
        xlabels: x labels as tuple
            Ex: ('c1','c2','category3')
        labels: legend labels as tuple
            Ex: ('dataset1','d2','d3')
        title: title of the plot
        x_label: label for the X axis
        y_label: label for the Y axis
        file_name: file to save the graph to
        show_graph_flag: if True, graph will pop up on screen and saved,
            otherwise just saved
        barwidth: how wide each bar will be on the graph
    """

    N = len(next (iter (values.values())))
    ind = np.arange(N)  # the x locations for the groups
    width = barwidth       # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects = []
    labels = []

    count = 0
    patterns = [ "/" ,"-" , "+" , "x", "o", "O", ".", "*","\\","|"]
    for key, list in values.items():
        rectangles = ax.bar(ind + width*count, list, width,hatch=patterns[count])
        count += 1
        rects.append(rectangles)
        labels.append(key)

    ymax = 0
    for rectangles in rects:
        for rect in rectangles:
            h = rect.get_height()
            totalHeight = h*1.1
            if totalHeight > ymax:
                ymax = totalHeight

    #ax.set_title(title)
    ax.set_ylim([0,ymax])
    ax.set_ylabel(y_label)
    ax.set_xticks(ind+width)
    ax.set_xticklabels( xlabels )

    if len(values) > 6:
        legendheight = 1.30
    elif len(values) > 3:
        legendheight = 1.20
    else:
        legendheight = 1.13
    ax.legend( (rect[0] for rect in rects), tuple(labels),loc='upper center',bbox_to_anchor=(0.5,legendheight), ncol= 3 )

    #def autolabel(recs):
    #    for rect in recs:
    #        h = rect.get_height()
    #        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
    #                ha='center', va='bottom',rotation=rotate,size=fontsize)

    #for rectn in rects:
    #    autolabel(rectn)

    save_and_show_graph(fig, file_name, show_graph_flag)

def heatmap(data, colormap, numbins, title, x_label, y_label, file_name, show_graph_flag):
    """
    Provide a list of x,y values and a heatmap will be generated

    Args:
        data: list of x,y lists
            Ex: [
                    [x1,x2,x3...],
                    [y1,y2,y3...]
                ]
        cmap: color map that will be used for the heatmap
        numbins: Number of bins for the histogram
        title: title of graph to be listed above it
        x_label: label to be displayed on x axis
        y_label: label to be displayed on y axis
        file_name: file to save the graph to
        show_graph_flag: if True, graph will pop up on screen and saved,
            otherwise just saved
    """
    fig, ax = plt.subplots()
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.set_xlabel(x_label)

    heatmap, xedges, yedges = np.histogram2d(data[0], data[1], bins=numbins)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    im = ax.imshow(heatmap.T, extent=extent, aspect='auto', origin='lower',cmap=colormap,norm=LogNorm())
    plt.colorbar(im)

    save_and_show_graph(fig, file_name, show_graph_flag)

def barchart_binned(list_of_vals,binsarray, title, x_label, file_name, show_graph_flag):
    chartdata = []
    for val in list_of_vals:
        if val == 0:
            chartdata.append("0")
        elif val <= 10:
            chartdata.append("1e1")
        elif val <= 100:
            chartdata.append("1e2")
        elif val <= 1000:
            chartdata.append("1e3")
        elif val <= 10000:
            chartdata.append("1e4")
        elif val <= 100000:
            chartdata.append("1e5")
        elif val <= 1000000:
            chartdata.append("1e6")
        elif val <= 10000000:
            chartdata.append("1e7")

    counter = Counter(chartdata)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_ylabel("Count")
    ax.set_title(title)
    ax.set_xlabel(x_label)

    frequencies = counter.values()
    names = list(counter.keys())

    x_coordinates = np.arange(len(counter))
    ax.bar(x_coordinates, frequencies, align='center')

    ax.xaxis.set_major_locator(plt.FixedLocator(x_coordinates))
    ax.xaxis.set_major_formatter(plt.FixedFormatter(names))

    save_and_show_graph(fig, file_name, show_graph_flag)


def graph_histogram(list_of_vals, title, x_label, file_name, show_graph_flag):
    """
    Send in a regular python list of values and we'll make a generic
    histogram for you, using automatic bins from matplotlib
    Args:
        list_of_vals: python list of values (floats) to graph
        title: title of graph to be listed above it
        x_label: label to be displayed on x axis
        y_label: label to be displayed on y axis
        file_name: file to save the graph to
        show_graph_flag: if True, graph will pop up on screen and saved,
            otherwise just saved
    """

    values_array = np.asarray(list_of_vals)

    plot = make_distplot(x_label, values_array, title)
    save_and_show_graph(plot, file_name, show_graph_flag)

def graph_bar(list_of_vals, labels, title, x_label, y_label, file_name, show_graph_flag):

    indexes = np.arange(len(labels))
    width = 1

    plt.bar(indexes, list_of_vals, width)
    plt.xticks(indexes + width * 0.5, labels)
    save_and_show_graph(plt, file_name, show_graph_flag)

def graph_bar_error(vals,labels,title,x_label,y_label,file_name,show_graph_flag,show_error,std=None):
    N = len(vals)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.2       # the width of the bars

    fig, ax = plt.subplots()
    plt.xticks(rotation=90)
    if show_error:
        ax.bar(ind, vals, width, color='g', yerr=std)
    else:
        ax.bar(ind, vals, width, color='g')

    # add some text for labels, title and axes ticks
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)

    save_and_show_graph(plt, file_name, show_graph_flag)


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')


def make_distplot(x_label, x_vals, title, title_size=20):
    """
    Wrapper around Seaborn's distplot function.
    Args:
        x_label: Label for X axis
        x_vals: X values
        title: Title of the plot
        title_size: Size of the tile
    Returns:
        Matplotlib plot object
    """

    data = pd.Series(x_vals, name=x_label)
    plot = sns.distplot(data)

    plot.figure.suptitle(title, size=title_size)
    plot.figure.subplots_adjust(top=.9)

    return plot


def make_lmplot(x_label, y_label, data, title, hue=None, title_size=20, fit=False,
                order=1, size=7, aspect=1.5, bullet_size=100, legend=True):
    """
    Wrapper around Seaborn's lmplot function, which generates a pretty graph
    with sane defaults and returns the plot object.
    Args:
        x_label: Label for X axis
        y_label: Label for Y axis
        data: Pandas dataframe of data
        title: Title of the plot
        hue: Which column of the Pandas dataframe to make the color based on
        title_size: Size of the title
        fit: Whether to fit a line to the plot
        order: Which order of polynomial to fit the plot with
        size: Size of the plot
        aspect: Aspect ratio of the plot
        bullet_size: Size of the bullets
        legend: Whether to display a legend
    Returns:
        Matplotlib plot object
    """

    if hue is not None:
        plot = sns.lmplot(x_label, y_label, data=data, hue=hue, fit_reg=fit,
                          order=order, size=size, aspect=aspect,
                          scatter_kws={"s": bullet_size}, legend=legend)
    else:
        plot = sns.lmplot(x_label, y_label, data=data, fit_reg=fit, size=size,
                          order=order, aspect=aspect,
                          scatter_kws={"s": bullet_size})
    plot.fig.suptitle(title, size=title_size)
    plot.fig.subplots_adjust(top=.9)

    return plot


def make_regplot(x_label, y_label, data, fit=False,
                 order=1, size=7, aspect=1.5, bullet_size=10,
                 ax=None, label='', markr='o',color='r'):
    """
    Wrapper around Seaborn's regplot function, which generates a pretty graph
    with sane defaults and returns the Axes object.
    Args:
        x_label: Label for X axis
        y_label: Label for Y axis
        data: Pandas dataframe of data
        title: Title of the plot
        fit: Whether to fit a line to the plot
        order: Which order of polynomial to fit the plot with
        size: Size of the plot
        aspect: Aspect ratio of the plot
        bullet_size: Size of the bullets
        ax: Matplotlib axes object to graph on
    Returns:
        Matplotlib plot object
    """

    #Sample 10 evenly spaced rows from dataframe for placing the markers
    if len(data) > 10:
        df2 = data.iloc[::(int(len(data.index)/10)), :]
    else:
        df2 = data.iloc[::(int(len(data.index)/5)), :]

    #draw the line
    axes = sns.regplot(x_label, y_label, data=data, fit_reg=fit,
                       order=order,
                       scatter_kws={"s": bullet_size}, color=color, ax=ax)

    #draw the markers
    sns.regplot(x_label, y_label, data=df2, marker=markr, fit_reg=fit,
                       order=order, label=label,
                       scatter_kws={"s": 200}, color=color, ax=ax)

    return axes


def save_and_show_graph(fig,file_name, show_graph_flag):
    """
    Title and save the graph, showing it if specified
    Args:
        file_name: file name to save as:
        show_graph_flag: determines whether or not to bring up the graph for
        the user to see immediately
    Returns:
        Nothing
    """

    if fig is None:
        pass
    #standardize image size by first setting figure size
    #fig.set_size_inches([7,5])

    plt.savefig(file_name,dpi=300, bbox_inches='tight')

    #Convert to gray scale
    #Image.open(file_name).convert('L').save(file_name)

    if show_graph_flag:
        plt.show()

    plt.clf()
    plt.close()